"""
TODO: docstring
"""
import selenium.webdriver

class Main:
    """
    TODO: docstring
    """
    def main():
        """
        TODO: docstring
        """
        options = selenium.webdriver.firefox.options.Options()
        options.binary_location = 'C:\\Program Files\\Tor Browser\\Browser\\firefox.exe'
        service = selenium.webdriver.firefox.service.Service('.\\geckodriver.exe')
        driver = selenium.webdriver.Firefox(service=service, options=options)
        url = ''
        driver.get(url)
        driver.close()
        driver.quit()

if __name__ == '__main__':
    Main.main()
