# Script to download and export to an excel file
# Lista anunturi publicitare si Anunturi de initiere

# Imported libraries
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def create_directory(path):
    if not os.path.isdir(path):
        print('Directory created!')
        os.mkdir(path)
    else:
        print('Directory already exists!')


def change_directory():
    # Create a special directory on the desktop to store the two excel files

    user = os.getlogin()
    user_path = r"C:/Users/" + user
    desktop = user_path + "/Desktop"
    directory = 'Licitatie Excel'
    licitatie_path = os.path.join(desktop, directory)
    adv_path = os.path.join(licitatie_path, 'adv')
    scn_path = os.path.join(licitatie_path, 'scn')

    create_directory(licitatie_path)
    create_directory(adv_path)
    create_directory(scn_path)

    # Move the excel files to this directory newly created

    # Move the excel file Anunturi de initiere
    downloads_path = user_path + '/Downloads'
    destination = licitatie_path + '/licitatii.xlsx'
    source = downloads_path + '/Anunturi de initiere.xlsx'
    if not os.path.exists(destination):
        os.replace(source, destination)
    else:
        print('File already exists!')
        os.remove(destination)
        os.replace(source, destination)
        print('File replaced!')

    # Move the excel file export
    for file in os.listdir(downloads_path):
        if file.startswith("export-"):
            r = os.path.join(downloads_path, file)
            if not os.path.exists(licitatie_path + "/export.xlsx"):
                os.replace(r, licitatie_path + "/export.xlsx")
            else:
                print('File already exists!')
                os.remove(licitatie_path + "/export.xlsx")
                os.replace(r, licitatie_path + "/export.xlsx")
                print('File replaced!')
    print('Changes made!')


def download_initire():
    link_anunturi_initiere = 'https://e-licitatie.ro/pub/notices/contract-notices/list/2/1'
    # driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
    driver.get(link_anunturi_initiere)
    time.sleep(5)

    xpath = "//h4[contains(., 'Anunt de participare si')]/input"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT, 'Export').click()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT, "excel").click()
    time.sleep(10)

    # file_path = r"C:/Users/" + os.getlogin() + '/Downloads'
    # waiting = True
    # while waiting:
    #     for file in os.listdir(file_path):
    #         if file.startswith("Anunturi de initiere-"):
    #             waiting = False
    #             break
    #     time.sleep(1)
    #     print('Waiting...')
    # print("Done download anunturi initiere!!")
    driver.quit()


def download_publiciare():
    link_anunturi_publicitate = 'https://e-licitatie.ro/pub/adv-notices/list/1'
    # driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
    driver.get(link_anunturi_publicitate)
    time.sleep(5)

    driver.find_element(By.LINK_TEXT, 'Export').click()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT, "excel").click()

    user = os.getlogin()
    file_path = r'C:/Users/' + user + "/Downloads"
    waiting = True
    while waiting:
        for file in os.listdir(file_path):
            if file.startswith("export-"):
                waiting = False
                break
        time.sleep(1)
        print('Waiting...')
    print("Done download anunturi publicitare!!")

    driver.quit()
