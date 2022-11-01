import urllib.request

import bs4
from selenium.webdriver.chrome.service import Service

input_str = """
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""


def generate_test_cases(example_str: str, function_name: str):

    examples = example_str.split("Example ")

    for example in examples:
        5

    assert 5


if __name__ == "__main__":

    leet_code_api_url = "https://leetcode.com/api/problems/algorithms/"

    # method 1
    webpage_content = str(urllib.request.urlopen(leet_code_api_url).read())

    # methode 2
    req = urllib.request.Request(
        url=leet_code_api_url,
        headers={"User-Agent": "Mozilla/106.0"}
    )
    webpage = urllib.request.urlopen(req).read()

    # method 3
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/106.0"

    opener = AppURLopener()
    response = opener.open(leet_code_api_url)

    # method 4
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # driver = webdriver.Firefox()
    driver.get(leet_code_api_url)

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(leet_code_api_url)

    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get(leet_code_api_url)

    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")


