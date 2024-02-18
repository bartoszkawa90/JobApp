from page_objects import *


# We want to search and scrap specific data from The:protocol
if __name__ == '__main__':
    # if we want to run withoud popup window
    # from selenium.webdriver.chrome.options import Options
    # options = Options()
    # options.add_argument('--headless=new')

    web_operator = Pracujpl(PagePracujpl())
    # web_operator = PageOperations(PageTheprotocol())
    web_operator.search_front_page(position='python', localization='Kraków')
    # web_operator.search_frontpage(position='python dev', localization='Kraków')
    web_operator.get_offers_list()


    print('')

