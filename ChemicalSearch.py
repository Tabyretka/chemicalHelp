from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from time import sleep


class ChemicalSearch:
    def __init__(self, chain: str, GeckoDriveFullrPath: str):
        self.chain = self.parse_chain(chain=chain)
        self.path = GeckoDriveFullrPath

    def parse_chain(self, chain: str) -> list:
        chain = chain.strip().split(" ")
        result = []
        while True:
            if len(chain) <= 1:
                break
            result.append((chain.pop(0), chain[0]))
        return result

    def open_pages(self):
        try:
            driver = webdriver.Firefox(executable_path=self.path)
        except Exception:
            return "check the path to the driver!"
        for group in self.chain:
            try:
                url = f"https://chemequations.com/en/advanced-search/?reactant1={group[0]}&product1={group[1]}&submit="
                driver.get(url)
                sleep(0.5)
                driver.find_element(By.TAG_NAME, "tbody").find_element(By.TAG_NAME, "tr").find_elements(By.TAG_NAME,
                                                                                                        "td")[
                    1].find_element(By.TAG_NAME, "a").click()
                driver.switch_to.new_window(WindowTypes.TAB)
            except Exception:
                return "Check your chain of equations!"
        driver.switch_to.window(driver.window_handles[0])
        return "successful"
