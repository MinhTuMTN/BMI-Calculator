from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


test_cases = [
    {
        'weight': 70,
        'height': 175,
        'bmi_score': 22.86,
        'status': 'Normal'
    },
    {
        'weight': 50,
        'height': 160,
        'bmi_score': 19.53,
        'status': 'Normal'
    },
    {
        'weight': 90,
        'height': 180,
        'bmi_score': 27.78,
        'status': 'Overweight'
    },
    {
        'weight': 120,
        'height': 190,
        'bmi_score': 33.24,
        'status': 'Obese'
    },
    {
        'weight': 40,
        'height': 150,
        'bmi_score': 17.78,
        'status': 'Underweight'
    },
    {
        'weight': 60,
        'height': 0,
        'bmi_score': 'Error',
        'status': 'Error'
    }
]

driver.get('https://minhtumtn.github.io/BMI-Calculator/')
txt_weight = driver.find_element(By.ID, 'weight')
txt_height = driver.find_element(By.ID, 'height')

bmi_score_result = driver.find_element(By.CSS_SELECTOR, '#result > div:nth-child(1)')
bmi_status_result = driver.find_element(By.CSS_SELECTOR, '#result > div:nth-child(2)')
for index, test_case in enumerate(test_cases):
    txt_weight.send_keys(Keys.CONTROL,"a", Keys.DELETE)
    txt_height.send_keys(Keys.CONTROL,"a", Keys.DELETE)
    txt_weight.send_keys(test_case['weight'])
    txt_height.send_keys(test_case['height'])

    sleep(1)

    print('Test case #{}'.format(index + 1))
    # Expected result
    print('Expected result: ')
    print('BMI score: {}'.format(test_case['bmi_score']))
    print('BMI status: {}'.format(test_case['status']))

    # Actual result
    print('Actual result: ')
    print('BMI score: {}'.format(bmi_score_result.text.split(' ')[-1]))
    print('BMI status: {}'.format(bmi_status_result.text.split(' ')[-1]))

    # Test case result
    print('Test case result: ', end='')
    if float(bmi_score_result.text.split(' ')[-1]) == test_case['bmi_score'] and bmi_status_result.text.split(' ')[-1] == test_case['status']:
        # Print passed with green color
        print('\033[92m' + 'Passed' + '\033[0m')
    else:
        # Print failed with red color
        print('\033[91m' + 'Failed' + '\033[0m')
    
    print('----------------------------------------')

    
driver.quit()