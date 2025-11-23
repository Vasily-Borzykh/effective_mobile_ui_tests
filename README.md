# UI тесты для effective-mobile.ru

## Требования
- Python 3.10
- Docker (опционально)
- (если хотите смотреть Allure отчет потом) Allure CLI на хосте

## Установка локально
1. Создать виртуальное окружение (в Pycharm можно пропустить этот пункт):
   python -m venv .venv
   .venv\\Scripts\\activate  # Windows PowerShell
2. Установить зависимости:
   pip install -r requirements.txt
3. Установить браузеры Playwright:
   python -m playwright install

## Запуск тестов локально
pytest -q

Результаты Allure пишутся в папку `results/` благодаря pytest.ini.

## Запуск через Docker
Собрать образ:
docker build -t effective-tests .

Запустить (PowerShell):
docker run --rm -v "${PWD}\\results:/app/results" effective-tests

Запустить (bash):
docker run --rm -v "$(pwd)/results:/app/results" effective-tests

## Просмотр Allure-отчёта (опционально, на хосте)
### Установка Allure CLI (Windows via Scoop):
Запускаем PowerShell и пишем следующие команды:
1) Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
2) iwr -useb get.scoop.sh | iex
3) scoop install allure
4) allure serve results