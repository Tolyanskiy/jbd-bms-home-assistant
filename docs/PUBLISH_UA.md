# Як опублікувати проєкт на GitHub

1. Перевір `LICENSE`: зараз використано MIT, а власником авторських прав вказано спільноту contributors. За потреби внеси ім’я/організацію правовласника перед публікацією.
2. Запусти `python tools/static_audit.py` (потрібен `pip install pyyaml`) і ESPHome `Validate` для обох прошивок у своєму середовищі.
3. Перевір, що ти **не додаєш** `secrets.yaml`, згенеровані прошивки, приватні IP-адреси, серійні номери, скриншоти з особистими даними або приватні журнали.
4. Встанови англомовну панель, зроби скриншоти для `screenshots/` та перевір, що всі назви й статуси англійською. Якщо потрібні також англомовні динамічні статуси, використовуй `firmware/jbd-bms-en.yaml`.
5. Створи **один** публічний GitHub repository `jbd-bms-esphome-configurator` і завантаж туди **вміст папки пакета**, а не ZIP як єдиний файл. Не створюй два репозиторії: у `dashboards/` уже є обидві мови.
6. Додай опис `ESPHome JBD Smart BMS configuration, EEPROM profiles & bilingual Home Assistant dashboard` та теми `esphome`, `home-assistant`, `jbd-bms`, `lifepo4`, `esp32`, `battery-management`.
7. Перший GitHub Release назви `v0.1.0-beta`. У описі поясни, що контролер перевірено власником на конкретній платі JBD, а незалежна компіляція пакета та широкий hardware regression ще потрібні.
8. Зафіксуй конкретну версію/commit `syssi/esphome-jbd-bms` **після** перевірки цього upstream на твоїй системі. Зараз приклад використовує рухому гілку `@main`.

### Через Git у терміналі

```bash
git init
git add .
git status --short
git commit -m "Initial public beta: ESPHome JBD configurator with EN/UA dashboards"
git branch -M main
# After creating the repository on GitHub:
git remote add origin https://github.com/YOUR_ACCOUNT/jbd-bms-esphome-configurator.git
git push -u origin main
```

Перед `git commit` переглянь `git status --short`. Ключі API та Wi-Fi не повинні бути серед доданих файлів.
