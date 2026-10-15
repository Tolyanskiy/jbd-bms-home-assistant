# Як приймати подяки за open-source проєкт

> Актуальність: жовтень 2026. Перед реєстрацією перевір актуальні умови платформ і свого банку. Реквізити у публічних файлах мають бути **лише ті, які ти підтвердив**.

## Найпрактичніші варіанти

| Інструмент | Формат | Що знати для України |
|---|---|---|
| **Patreon** | Регулярна підтримка і можлива разова | У Patreon є варіанти виплат через Payoneer/банківський переказ, включно з UAH; фактичну доступність перевірити в налаштуваннях. PayPal/Hyperwallet payout для українських авторів недоступний. |
| **monobank Банка** | Разова подяка | Застосунок дозволяє створити Банку на будь-які цілі й поділитися посиланням; можна використовувати окреме посилання для донатів. |
| **Криптовалюта** | Прямий переказ | Немає платформи-посередника, але слід вказати криптовалюту, **конкретну мережу**, публічну receiving-адресу. Транзакції незворотні; історія адреси публічна. |
| **GitHub Sponsors** | Разова / щомісячна | На жовтень 2026 **України немає у списку країн отримувачів GitHub Sponsors**. Зараз не додавай `github: username`, поки не схвалений акаунт/не підтверджена доступність. |
| **Buy Me a Coffee** | Разова / членство | За офіційним переліком країн виплат (Stripe) **Україна не вказана**. Не рекомендується як основний спосіб. |
| **Ko-fi** | Разова | Працює через Stripe/PayPal; доступність отримання платежів для конкретного українського акаунта слід перевіряти, перш ніж додавати кнопку. |

## Рекомендована стратегія для репозиторію

1. Опублікуй проєкт **без будь-яких адрес**, але з `SUPPORT.md`, де написано, що підтримка налаштовується.
2. Обери основний варіант: **Patreon** (якщо доступні виплати) або **monobank Банка** для разової подяки.
3. Якщо хочеш крипту, створи окрему адресу **тільки для отримання** підтримки. Можна обрати BTC або стейблкоїн, але пиши мережу точно: USDT на різних мережах — це різні адреси/правила переказу.
4. Спочатку зроби маленький тестовий переказ і перевір зарахування. **Ніколи не викладай seed phrase, private key, приватний QR-гаманець із seed, чи доступ до біржі**. Публікувати дозволено лише receiving-адресу.
5. Додай перевірені посилання в `SUPPORT.md`.
6. Коли посилання готові, створи `.github/FUNDING.yml` із прикладу `.github/FUNDING.yml.example`.

## Приклади синтаксису FUNDING.yml (замінити на реальні дані)

```yaml
patreon: YOUR_PATREON_USERNAME
custom:
  - https://YOUR_VERIFIED_SUPPORT_PAGE
```

Для криптовалюти краще вказувати **посилання на SUPPORT.md або окрему донат-сторінку**, а не адресу напряму у `FUNDING.yml`.

## Офіційні джерела

- GitHub Sponsor button: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository
- GitHub Sponsors supported regions: https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors
- Patreon payouts: https://support.patreon.com/hc/en-us/articles/115004029783-Adding-your-payout-details
- Patreon payouts international: https://support.patreon.com/hc/en-us/articles/39694936541965-Payouts-guide-for-creators-outside-of-the-US
- monobank Банка: https://monobank.ua/banka
- Buy Me a Coffee supported countries: https://help.buymeacoffee.com/en/articles/6258038-supported-countries-for-payouts-on-buy-me-a-coffee
