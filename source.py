from dataclasses import dataclass


@dataclass
class Pages:
    theprotocol = 'https://theprotocol.it/'
    pracujpl = 'https://pracuj.pl'
    indeed = 'https://pl.indeed.com/'


class PagePracujpl(Pages):
    # Pracuj.pl
    page = 'https://pracuj.pl'

    @dataclass
    class Xpath:
        accept_button = '//*[@id="__next"]/div[7]/div/div/div[3]/div/button[1]'

        # front page
        position_front = '//*[@id="__next"]/section[1]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/input'
        category_front = '//*[@id="__next"]/section[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/input'
        localization_front = '//*[@id="__next"]/section[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div/input'
        range_in_km_front = '//*[@id="__next"]/section[1]/div[2]/div[2]/div/div[1]/div[4]/div/div/div/input'
        search_front = '//*[@id="__next"]/section[1]/div[2]/div[2]/div/div[2]/button'
        select_localization_front = '//*[@id="__next"]/section[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div/div[2]/ul/li[1]'

        # standard page
        position_standard = '//*[@id="relative-wrapper"]/div[1]/div/div/div/div[1]/div[1]/div/div/div/input'
        category_standard = '//*[@id="relative-wrapper"]/div[1]/div/div/div/div[1]/div[2]/div/div/div/input'
        localization_standard = '//*[@id="relative-wrapper"]/div[1]/div/div/div/div[1]/div[3]/div/div/div/input'
        range_in_km_standard = '//*[@id="relative-wrapper"]/div[1]/div/div/div/div[1]/div[4]/div/div/div/input'
        search_standard = '//*[@id="relative-wrapper"]/div[1]/div/div/div/div[2]/div/button'
        articles_table = '//*[@id="relative-wrapper"]/div[2]/div[2]/div[2]/div[4]/div[2]'

    @dataclass
    class Css:
        # search bar clear css selectors
        clear_position_standard = '#relative-wrapper > div.wx9saw > div > div > div > div.core_bvgive4 > div:nth-child(1) > div > div > div > div > span > svg > path'
        clear_localization_standard = '#relative-wrapper > div.wx9saw > div > div > div > div.core_bvgive4 > div:nth-child(3) > div > div > div > div > span > svg > path'

        # clear bar list
        clear_bar_list = [clear_position_standard, clear_localization_standard]


class PageIndeed(Pages):
    # Indeed.com
    page = 'https://pl.indeed.com/'

    @dataclass
    class Xpath:
        # Indeed
        indeed_position = '//*[@id="text-input-what"]'


class PageTheprotocol(Pages):
    #Theprotocol.it
    page = 'https://theprotocol.it/'

    @dataclass
    class Xpath:
        # The protocol
        accept_button = '//*[@id="__next"]/div/div[2]/div/div[5]/div/aside/div/div[2]/div[2]/div[2]/button[1]/div'

        theprotocol_random_search = '//*[@id="search"]'



