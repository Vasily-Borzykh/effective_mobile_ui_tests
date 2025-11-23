import pytest
from page_objects.home_page import HomePage

links = list(HomePage.LINKS_MAP)

@pytest.mark.parametrize("link_text, expected_fragment", links)
def test_main_page_links(page, link_text, expected_fragment):
    home = HomePage(page)
    home.open()
    home.link_by_text(link_text)
    page.wait_for_load_state('networkidle')
    assert expected_fragment in page.url