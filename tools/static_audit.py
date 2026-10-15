#!/usr/bin/env python3
"""Static repository audit. Requires PyYAML; does not compile ESPHome or interact with hardware."""
from __future__ import annotations
import argparse
import difflib
import hashlib
import re
from pathlib import Path
from collections import Counter
import yaml

ROOT = Path(__file__).resolve().parents[1]

class ESPHomeLoader(yaml.SafeLoader):
    pass
ESPHomeLoader.add_constructor('!secret', lambda loader, node: '!secret ' + loader.construct_scalar(node))

def yaml_file(file: Path, *, esphome: bool=False):
    return yaml.load(file.read_text(encoding='utf-8'), Loader=ESPHomeLoader if esphome else yaml.SafeLoader)

def keys(tree, key):
    found=[]
    if isinstance(tree, dict):
        for k,v in tree.items():
            if k == key: found.append(v)
            found.extend(keys(v, key))
    elif isinstance(tree, list):
        for item in tree: found.extend(keys(item, key))
    return found

def refs(tree):
    refs=set()
    for k in ('entity','entity_id'):
        for v in keys(tree, k):
            if isinstance(v,str):refs.add(v)
            elif isinstance(v,list):refs.update(x for x in v if isinstance(x,str))
    # Markdown card templates reference entities via Jinja functions.
    for c in keys(tree,'content'):
        if isinstance(c,str):
            refs.update(re.findall(r"(?:states|is_state)\(\s*['\"]([a-z_]+\.[a-z0-9_]+)",c))
    return refs

def cplusplus_without_strings(text):
    # Firmware variants intentionally differ only by localization of their C++ string literals.
    # C++ macros/comments/config names and numeric constants must stay identical.
    return re.sub(r'"(?:\\.|[^"\\])*"', '"STRING"', text)

def main():
    errors=[]
    fw_ua=ROOT/'firmware/jbd-bms-ua.yaml';fw_en=ROOT/'firmware/jbd-bms-en.yaml'
    ui_ua=ROOT/'dashboards/jbd-dashboard-uk.yaml';ui_en=ROOT/'dashboards/jbd-dashboard-en.yaml'
    fua=yaml_file(fw_ua,esphome=True);fen=yaml_file(fw_en,esphome=True)
    dua=yaml_file(ui_ua);den=yaml_file(ui_en)
    expected_fw={'substitutions','esphome','esp32','uart','jbd_bms','sensor','binary_sensor','text_sensor','number','globals','script','button','switch'}
    for path,d in [(fw_ua,fua),(fw_en,fen)]:
        if not expected_fw.issubset(d):errors.append('Missing firmware component keys: '+str(path))
        if len(d.get('substitutions',{}))!=10:errors.append('Project defaults not 10')
        if len(d.get('number',[]))!=20:errors.append('Expected 20 number entities')
        if len(d.get('switch',[]))!=2:errors.append('Expected 2 switches incl. discharge MOSFET')
        if 'github://syssi/esphome-jbd-bms@main' not in path.read_text():errors.append('Expected external component not found')
    ua_text=fw_ua.read_text(encoding='utf8');en_text=fw_en.read_text(encoding='utf8')
    if cplusplus_without_strings(ua_text)!=cplusplus_without_strings(en_text):
        errors.append('Firmware variants differ beyond quoted text strings')
    if re.search(r'[А-ЯҐЄІЇа-яґєії]',en_text):errors.append('English firmware contains Ukrainian text')
    # Code comments must be English; quoted run-time status text can be Ukrainian in UA firmware.
    for line in ua_text.splitlines():
        code=line.split('//',1)
        if len(code)>1 and re.search(r'[А-ЯҐЄІЇа-яґєії]',code[1]):errors.append('Non-English C++ comment')
        if line.lstrip().startswith('#') and re.search(r'[А-ЯҐЄІЇа-яґєії]',line):errors.append('Non-English YAML comment')
    if len(dua.get('views',[]))!=6 or len(den.get('views',[]))!=6:errors.append('Expected 6 views in each dashboard')
    if [v['path'] for v in dua['views']] != [v['path'] for v in den['views']]:errors.append('Dashboard path drift')
    if [v['icon'] for v in dua['views']] != [v['icon'] for v in den['views']]:errors.append('Dashboard icon drift')
    if refs(dua)!=refs(den):errors.append('Dashboard entity refs changed: '+repr((refs(dua)-refs(den),refs(den)-refs(dua))))
    for k in ('action','perform_action'):
        if Counter(keys(dua,k))!=Counter(keys(den,k)):errors.append('Dashboard action drift: '+k)
    for string in keys(den,'title')+keys(den,'name')+keys(den,'text')+keys(den,'content'):
        if isinstance(string,str) and re.search(r'[А-ЯҐЄІЇа-яґєії]',string):errors.append('English dashboard contains untranslated Cyrillic')
    for path in [fw_ua,fw_en,ui_ua,ui_en]:
        s=path.read_text(encoding='utf8')
        if re.search(r'(?im)^\s*(?:wifi_ssid|wifi_password|jbd_bms__encryption_key)\s*:\s*["\']?[^!\s][^\r\n]*',s):
            errors.append('Direct credentials suspected: '+str(path))
    for path in [fw_ua,fw_en]:
        s=path.read_text(encoding='utf8')
        for secret in ('!secret wifi_ssid','!secret wifi_password','!secret jbd_bms__encryption_key'):
            if secret not in s:errors.append('Missing secret reference '+secret)
    # Catch unintended tracking of local secret file.
    if (ROOT/'secrets.yaml').exists():errors.append('Real secrets.yaml unexpectedly present')
    print('Static YAML parse: PASS' if not errors else 'Static YAML parse: COMPLETE, errors below')
    print('Language variants: firmware=2, dashboards=2; dashboard views=6')
    print('Dashboard named entity references:', len(refs(dua)))
    print('Firmware reported data categories:',len(fua['sensor']),'sensors,',len(fua['button']),'buttons,',len(fua['switch']),'switches')
    print('Actions and entity refs:', 'MATCH' if refs(dua)==refs(den) else 'DO NOT MATCH')
    if errors:
        for e in sorted(set(errors)):print('FAIL:',e)
        raise SystemExit(1)
    print('No included plaintext credentials detected. Note: static audit is not hardware/compile validation.')

if __name__=='__main__': main()
