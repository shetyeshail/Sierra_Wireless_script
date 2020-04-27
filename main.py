#import packages
import selenium

#use Chrome driver to access website
driver = webdriver.Chrome()

#open the text file of URLs
url_file = open('urls.txt', 'r')

#FILL IN THE FOLLOWING VARIABLES:
username = ''
password = ''

for url in url_file:
  #open the website
  driver.get(URL + ':9191')

  #LOGGING INTO THE ADMIN PAGE
  #select username box
  username_box = driver.find_element_by_name('username')
  #send username info
  username_box.send_keys(username)
  #select password box
  password_box = driver.find_element_by_name('password')
  #send password info
  password_box.send_keys(password)
  #find login button
  login_button = driver.find_element_by_name('Login')
  #click login button
  login_button.click()

  #NAVIGATING TO THE ABOUT PAGE TO SCRAPE INFO
  #click About button on left sidebar
  about_button = driver.find_element_by_xpath("//span[text()='About']").click()

  #SCRAPING NECESSARY DATA FROM ABOUT PAGE
  #select element for device model
  webelement device_model_element = driver.findElement(By.id("7"))
  #get value of device model
  String device_model = element.getAttribute("value")
  #TODO: get radio firmware version element
  webelement radio_version_element = driver.findElement()
  #TODO: get value of firmware version
  String firmware_version = element.getAttribute()
  #TODO: get ALEOS version element
  webelement ALEOS_version_element = driver.findElement()
  #TODO: get value of ALEOS version
  String ALEOS_version = element.getAttribute()
  #TODO: print all values to CSV or EXCEL file

  #IF UPGRADE FLAG IS 1 THEN WILL UPGRADE FIRMWARE
  if(upgrade_flag==1):
    #   if ((device_model=='LS300')||(device_model=='GX400')||(device_model=='GX440')||(device_model=='ES440')):
    #
    #   
    #click the firmware button
    firmware_button = driver.find_element_by_id("btn_fw")
    firmware_button.click()

    #click 'choose file'
    choose_file_button = driver.find_element_by_id("file")

    #select and upload the firmware file
    firmware_file_location = 'PUT FIRMWARE FILE NAME HERE'
    choose_file_button.send_keys(firmware_file_location)

    #click 'update firmware button'
    update_firmware_button = driver.find_element_by_name("go")

  #END OPTIONAL UPGRADE
