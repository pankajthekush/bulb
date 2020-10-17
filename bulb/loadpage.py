from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from pyvirtualdisplay import Display


def selenium_page_source(url):
    
    dict_data = dict()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=0")  # this
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--no-zygote') # should be used with no sandbox
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--no-proxy-server')
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-gl-drawing-for-tests")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--hide-scrollbars")
    chrome_options.add_argument("--disable-breakpad")

    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(300)
    
    try:
        driver.get(url)
        sleep(3)
        try:
            alert = driver.switch_to_alert()
            alert.accept()
        except Exception:
            pass
                            
        dict_data['current_url'] = driver.current_url
        dict_data['page_source'] = driver.page_source
    except Exception as e:
        dict_data['current_url'] = 'error'
        dict_data['page_source'] = str(e) 


    driver.close()
    driver.quit()
    display.stop()
    return dict_data 


if __name__ == "__main__":
    dcit_data = selenium_page_source('https://zeenews.india.com/india/bus-pickup-collision-in-up-s-pilibhit-cm-yogi-adityanath-announces-ex-gratia-of-rs-5-lakhs-2318035.html')
    print(dcit_data)
