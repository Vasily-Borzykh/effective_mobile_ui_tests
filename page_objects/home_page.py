from playwright.sync_api import Page


class HomePage:
    URL = "https://effective-mobile.ru/"
    LINKS_MAP = [
        ("О нас", "#about"),
        ("Контакты", "#contact"),
        ("Отзывы", "#testimonials"),
        ("Вакансии", "#specializations"),
    ]

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def get_current_url(self) -> str:
        return self.page.url

    def link_by_text(self, link_text: str):
        locator = self.page.get_by_text(link_text, exact=True)
        locator.first.click()
