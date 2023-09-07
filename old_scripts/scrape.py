import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def extract_info(driver):
    # Extract information from the Übersicht section
    uebersicht = driver.find_element(By.ID, 'content-übersicht')
    initiative = uebersicht.find_element(By.XPATH, '//label[text()="Initiative:"]/following-sibling::span').text
    beratungsstand = uebersicht.find_element(By.XPATH, '//label[text()="Beratungsstand:"]/following-sibling::span').text
    
    # Extract information from the Wichtige Drucksachen and Plenum sections
    wichtige_drucksachen = []
    plenum = []
    documents = driver.find_elements(By.XPATH, '//label[text()="Wichtige Drucksachen"]/following-sibling::ul/li')

    for doc in documents:
        date = doc.find_element(By.XPATH,'./div/div').text
        title = doc.find_element(By.XPATH,'./div/div/a').text
        link = doc.find_element(By.XPATH,'./div/div/a').get_attribute('href')
        if 'BT-Drucksache' in title:
            wichtige_drucksachen.append({'date': date, 'title': title, 'link': link})
        elif 'BT-Plenarprotokoll' in title:
            plenum.append({'date': date, 'title': title, 'link': link})
    
    return {
        'initiative': initiative,
        'beratungsstand': beratungsstand,
        'wichtige_drucksachen': wichtige_drucksachen,
        'plenum': plenum
    }

def download_file(url, date):
    doc_type = date.split('(')[1].split()[0]
    local_filename = f'Drucksachen/{doc_type}.pdf'
    
    # Create the Drucksachen folder if it doesn't exist
    if not os.path.exists('Drucksachen'):
        os.makedirs('Drucksachen')
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename



url = "https://dip.bundestag.de/vorgang/verbot-von-%C3%B6l-und-gasheizungen-verhindern-priorisierung-der-w%C3%A4rmepumpen/298662"

driver = webdriver.Firefox()

try:
    # Navigate to the page
    driver.get(url)

    # Wait for the page to load completely
    driver.implicitly_wait(10)

    # Extract the information
    info = extract_info(driver)

    # Download wichtige_drucksachen documents
    for doc in info['wichtige_drucksachen']:
        url = doc['link']
        date = doc['date']
        local_filename = download_file(url, date)
        print(f'Downloaded {local_filename}')

finally:
    # Close the browser window
    driver.quit()
