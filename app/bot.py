import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
from app.set import email, pswd, photo_path, university, degree, spec, grade, position, company_name, company_geo, industry, \
    pos_desc, short_desc, skills_lst, work_experience



def Launch():
    """
    Launch the LinkedIn bot.
    """

    # Browser choice
    print('Choose your browser:')
    print('[1] Chrome')
    print('[2] Firefox/Iceweasel')

    while True:
        try:
            browserChoice = int(input('Choice? '))
        except ValueError:
            print('Invalid choice.'),
        else:
            if browserChoice not in [1, 2]:
                print('Invalid choice.'),
            else:
                break

    StartBrowser(browserChoice)


def StartBrowser(browserChoice):
    """
    Launch broswer based on the user's selected choice.
    browserChoice: the browser selected by the user.
    """

    if browserChoice == 1:
        print('\nLaunching Chrome')
        browser = webdriver.Chrome(ChromeDriverManager().install())
    elif browserChoice == 2:
        print('\nLaunching Firefox/Iceweasel')
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


    # Sign in
    browser.get('https://linkedin.com')
    time.sleep(2)
    try:
        browser.find_element(By.XPATH, '/html/body/div[1]/div/section/div/div[2]/button[1]').click()
        time.sleep(1)
    except:
        pass
    browser.find_element(By.XPATH, '/html/body/footer/ul/li[11]/div/button').click()
    time.sleep(5)
    browser.find_element(By.XPATH, "/html/body/footer/ul/li[11]/div/ul/li[5]/button").click()
    time.sleep(3)
    browser.find_element(By.LINK_TEXT, 'Sign in').click()  #Need to change on Sign In
    time.sleep(2)
    emailElement = browser.find_element(By.ID, 'username')
    emailElement.send_keys(email)
    passElement = browser.find_element(By.ID, 'password')
    passElement.send_keys(pswd)
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@type = 'submit']").click()
    print('Signing in...')
    time.sleep(5)  # This time sleep can be lower. I made it because of the LinkedIn verification. It happens smtms.
    soup = BeautifulSoup(browser.page_source, "html.parser")
    if soup.find('div', {'class': 'alert error'}):
        print('Error! Please verify your username and password.')
        browser.quit()
    elif browser.title == '403: Forbidden':
        print('LinkedIn is momentarily unavailable. Please wait a moment, then try again.')
        browser.quit()
    else:
        print('Success!\n')

        # LinkedInBot(browser)
    # Enter profile
    browser.find_element(By.CLASS_NAME, "ember-view.block").click()
    time.sleep(2)
    cur_url = browser.current_url  # save profile url for faster navigation
    # Photo block
        # checking if photo exists already
    if len(browser.find_elements(By.CLASS_NAME, 'pv-top-card__edit-photo-button')) > 0:
        browser.find_element(By.CLASS_NAME, 'pv-top-card__edit-photo-button').click()
    else:
        browser.find_element(By.CLASS_NAME, 'ember-view.profile-photo-edit__preview').click()
        browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/footer/button[2]').click()
        time.sleep(2)
    browser.find_element(By.XPATH, "//*[@id='image-selector__file-upload-input']").send_keys(photo_path)
    time.sleep(2)
    browser.find_element(By.CLASS_NAME,
             "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.profile-photo-cropper__apply-action")\
            .click()
    time.sleep(3)
    # About block
    browser.get(cur_url + 'edit/forms/summary/new/?profileFormEntryPoint=PROFILE_COMPLETION_HUB')
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(work_experience)
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@type = 'button']").click()
    time.sleep(2)
    # Education block
    browser.get(cur_url+'edit/forms/education/new/?profileFormEntryPoint=PROFILE_COMPLETION_HUB')
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/input')\
                        .send_keys(university)
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/input')\
                        .send_keys(Keys.RETURN)
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div/input')\
                            .send_keys(degree)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div/div/div/input')\
                        .send_keys(spec)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/'
                                   'fieldset[1]/div/span[1]/select/option[10]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/'
                                   'fieldset[1]/div/span[2]/select/option[12]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/'
                                   'fieldset[2]/div/span[1]/select/option[7]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/'
                                   'fieldset[2]/div/span[2]/select/option[17]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[5]/div/div/div/'
                                   'div[1]/div/input').send_keys(grade)
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()
    time.sleep(3)
    browser.get(cur_url+'edit/forms/position/new/?profileFormEntryPoint=PROFILE_COMPLETION_HUB')
    time.sleep(2)
    # Job block
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/input')\
                        .send_keys(position)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/input')\
                        .send_keys(Keys.RETURN)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/'
                                   'select/option[2]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div/div/div/input')\
                        .send_keys(company_name)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div/div/div/input')\
                        .send_keys(Keys.RETURN)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[4]/div/div/div/div/input') \
                        .send_keys(company_geo)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[4]/div/div/div/div/input') \
                        .send_keys(Keys.RETURN)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[5]/div/div/div/select/'
                                   'option[4]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[7]/div/div/div/div[1]/'
                                   'fieldset[1]/div/span[1]/select/option[2]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[7]/div/div/div/div[1]/'
                                   'fieldset[1]/div/span[2]/select/option[2]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[8]/div/div/div[1]/div/input')\
                        .clear()
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[8]/div/div/div[1]/div/input')\
                        .send_keys(industry)
    time.sleep(1)
    browser.find_element(By.TAG_NAME, 'textarea').clear()
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(pos_desc)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[10]/div/div/div/div[1]/'
                                   'div/input').clear()
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[10]/div/div/div/div[1]/'
                                   'div/input').send_keys(short_desc)
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()
    time.sleep(3)
    # Skills block
    for i in skills_lst:
        browser.get(cur_url+'edit/forms/skills/new/?profileFormEntryPoint=PROFILE_COMPLETION_HUB')
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/input')\
                            .send_keys(i)
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/input')\
                            .send_keys(Keys.RETURN)
        time.sleep(2)
        browser.find_element(By.CLASS_NAME,
                             'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()
        time.sleep(3)
    time.sleep(1)
    print('Done!')

