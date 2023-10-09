from selenium import webdriver
from selenium.webdriver.common.by import By

# Installeer de webdriver voor jouw browser (bijv. Chrome of Firefox) en geef het pad naar het webdriver-uitvoerbaar bestand aan
driver = webdriver.Chrome(r'C:\Users\g521104.CORP\Desktop\temp\test\drivers\chromedriver-win64\chromedriver.exe')

class webpages:
    def __init__(self):
        self.items = []

    def append(self, webpage):
        if isinstance(webpage, str):
            if webpage not in [item.get("webpage") for item in self.items]:
                self.items.append({"webpage": webpage, "checked": False})
                
    def append_from_list(self,Webpages):
        for page in Webpages:
            self.append(page)
    
    def checked(self, webpage):
        for item in self.items:
            if item["webpage"] == webpage:
                return item
        return None

    def get_full_list(self):
        return self.items
    
    def get_page(self, webpage):
        for item in self.items:
            if item["webpage"] == webpage:
                return item
        return None

def get_links_on_page(driver):
    links = []
    for link_element in driver.find_elements(By.TAG_NAME, 'a'):
        href = link_element.get_attribute('href')
        if href and href.startswith('http'):
            links.append(href)
    return links

def analyse_website():
    driver.get(url)
    driver.implicitly_wait(5)

    web_index = webpages()
    web_index.append_from_list(found_links)

    driver.quit()

# Roep de functie aan met de URL van de pagina die je wilt indexeren
url = 'https://risqit.nl'
web_index = webpages()
found_links = analyse_website(url)


for x in web_index.get_full_list():
    print(x)
