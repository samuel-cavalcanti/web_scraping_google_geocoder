from selenium import webdriver
from bs4 import BeautifulSoup
from itertools import cycle
import time


class Geocoder:
    __google_maps = "https://google-developers.appspot.com/maps/documentation/utils/geocoder/embed"

    def __init__(self):
        self.__driver = webdriver.Chrome()

        self.__driver.get(self.__google_maps)
        time.sleep(3)

    def __del__(self):
        self.__driver.close()

    def __find_element(self):
        element = None
        while element is None:
            try:
                element_test = self.__driver.find_element_by_id("map")
                element_test = element_test.find_elements_by_css_selector("*")[0].find_element_by_class_name("gm-style")
                element_test = element_test.find_element_by_class_name("control-ui")
                element_test.find_element_by_id("query-input").send_keys("test")
                element_test.find_element_by_id("query-input").clear()
                element_test.find_element_by_id("geocode-button")
                element = element_test

            except:
                time.sleep(0.5)

        return element

    def geocoding(self, address: str) -> list:
        element = self.__find_element()

        element.find_element_by_id("query-input").send_keys(address)
        element.find_element_by_id("geocode-button").click()

        if self.__response():
            location = self.__get_location()

        else:
            location = []

        element.find_element_by_id("query-input").clear()

        self.__driver.refresh()

        return location

    def __get__status(self) -> bool or None:
        soup = BeautifulSoup(self.__driver.page_source, features="html5lib")

        status = soup.find("span", {"class": "OK"})
        if status:
            return True

        status = soup.find("span", {"class": "ZERO_RESULTS"})
        if status:
            return False

        return None

    def __response(self) -> bool:

        status = self.__get__status()

        while status is None:
            status = self.__get__status()
            time.sleep(0.1)

        return status

    def __get_location(self) -> list:
        soup = BeautifulSoup(self.__driver.page_source, features="html5lib")

        div = soup.find("div", {"class": "active-result", "id": "result-0"})
        location_html = div.find("p", {"class": "result-location"}).text

        location = str(location_html).replace("\n", "").replace(" ", "").replace("Location:", "").split(",")

        return location


def test():
    address_list = ["Unidade Básica de Saúde do Centro", "Unidade Básica do Conjunto Cônego Monte",
                    "Posto de saúde do DNR"]
    geo = Geocoder()
    for address in cycle(address_list):
        location_gps = geo.geocoding(address)
        print(location_gps)


if __name__ == '__main__':
    test()
