# GitHub: покрокова публікація для першого репозиторію

## 0. Підготовка

1. Розпакуй ZIP. Відкрий папку **`jbd-bms-esphome-configurator-github-ready`** — саме **її вміст**, а не ZIP, потрібно завантажити на GitHub.
2. Переглянь `README.md`, `README_UA.md`, `LICENSE`, `SUPPORT.md`. У LICENSE заміни авторські реквізити, якщо хочеш вказати своє ім’я/псевдонім.
3. Відкрий `firmware/jbd-bms-ua.yaml` та `firmware/jbd-bms-en.yaml` у ESPHome і перевір **Validate** (краще перевірити обидва). Тут виконано лише статичну перевірку.
4. Не додавай `secrets.yaml`, реальні паролі Wi-Fi, API-ключ, приватні криптоключі, приватні логи або резервні копії Home Assistant. Файл `secrets.yaml.example` можна публікувати.
5. Зроби скриншоти з англомовного Dashboard з підключеною BMS, перевір чи немає приватних даних, збережи в `screenshots/` (PNG/JPG). Файл `screenshots/README.md` можна залишити.

## 1. Реєстрація GitHub

1. Перейди на <https://github.com/signup> (або увійди на <https://github.com/login>).
2. Підтверди електронну пошту. Рекомендовано одразу ввімкнути 2FA у Settings → Password and authentication.

## 2. Створення репозиторію

1. Відкрий <https://github.com/new>.
2. **Owner:** твій обліковий запис.
3. **Repository name:** `jbd-bms-esphome-configurator`.
4. **Description:** `JBD Smart BMS ESPHome configurator with EEPROM profiles and EN/UA Home Assistant dashboards`.
5. **Public:** увімкнути.
6. **НЕ** позначай `Add a README file`, `.gitignore`, `Choose a license`: усе вже в ZIP.
7. Натисни **Create repository**.

## 3. Завантаження файлів через браузер

1. У створеному порожньому репозиторії натисни **uploading an existing file** або **Add file → Upload files**.
2. Відкрий розпаковану папку, виділи **всі файли та папки всередині** й перетягни їх на сторінку завантаження (не саму зовнішню папку).
3. Переконайся, що GitHub бачить вкладені `firmware/`, `dashboards/`, `docs/`, `screenshots/` і **приховану `.github/`**. `README.md` має бути в корені, а не на другому рівні.
4. Якщо браузер не переносить приховані елементи (`.github`, `.gitignore`), скористайся GitHub Desktop (інструкція нижче) або створи їх згодом через Add file → Create new file.
5. Введи commit message: `Initial public beta with stable UART settings and bilingual dashboards`.
6. Натисни **Commit changes** (або відповідну кнопку підтвердження).
7. На головній сторінці репозиторію перевір, що README відкривається, а обидва Dashboard і firmware лежать у своїх каталогах.

## 3b. Альтернатива через GitHub Desktop (Windows)

1. Встанови GitHub Desktop з <https://desktop.github.com/> і авторизуйся.
2. **File → Add Local Repository → Choose** та обери розпаковану папку. Якщо Git там не ініціалізований, вибери **Create a Repository here**.
3. Перевір список змін у лівій частині. `secrets.yaml` там бути не повинно.
4. В полі Summary введи `Initial public beta`, натисни **Commit to main**.
5. Обери **Publish repository**. Ім'я `jbd-bms-esphome-configurator`, зніми прапорець **Keep this code private**. Якщо пропонується вже створений репозиторій з браузерного кроку — замість публікації заново треба зв’язати локальну копію з наявним репозиторієм; для першої публікації простіше обрати **або браузер, або Desktop**, не обидва способи одночасно.

## 4. Оформлення

1. На головній сторінці репозиторію натисни ⚙ поруч із **About** (правий бік), додай Description та Topics: `esphome`, `home-assistant`, `jbd-bms`, `esp32-c3`, `lifepo4`, `battery-management-system`, `uart`.
2. Переконайся, що `README.md` — англійською, а `README_UA.md` відкривається за посиланням.
3. За бажанням додай скриншоти та посилання на них у README.
4. У вкладці **Actions** перевір, що статична перевірка проходить. Якщо GitHub попросить увімкнути workflow, уважно прочитай його в `.github/workflows/static-audit.yml`.

## 5. Перший Release

1. Відкрий репозиторій → **Releases** → **Draft a new release**.
2. **Choose a tag → Create new tag**: `v0.1.0-beta` з поточної гілки `main`.
3. **Release title:** `JBD BMS ESPHome Configurator v0.1.0-beta`.
4. **Description:** `First public beta. UART monitoring configured at 5 s interval, 300 ms timeout and WARN logging. EN/UA dashboards and profiles. Hardware validation is limited to the listed JBD/ESP32 test configuration.`
5. Познач **Set as a pre-release**, після перевірки натисни **Publish release**.

## 6. Sponsor / donations

1. Переглянь `docs/SUPPORT_OPTIONS_UA.md` та створи обраний спосіб отримання внесків. Не використовуй вигаданий URL або адресу.
2. В `SUPPORT.md` додай робочі посилання, назву криптовалюти і мережу для адрес.
3. Створи `.github/FUNDING.yml` за прикладом `.github/FUNDING.yml.example`, заповни **тільки справжні, перевірені** URL/handles. Це створить Sponsor button у репозиторії.
4. Зроби тестовий невеликий внесок, перевір зарахування до того, як рекомендувати підтримку іншим.

## 7. Відповіді користувачам

- GitHub → **Issues**: повідомлення про проблеми та пропозиції.
- **Pull requests**: зміни коду від інших розробників.
- Наступні виправлення роби окремими commits і Releases, щоб користувачі бачили історію.
