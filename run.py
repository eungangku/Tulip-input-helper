import os
from webdriver_auto_update import check_driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# download & update chromedriver
current_path = os.getcwd()
check_driver(current_path)

browser = webdriver.Chrome()
browser.get("https://liblas.cnu.ac.kr/FN/app/index.html")

# manually login

# price input
# document.querySelector("#mainframe_VFrames_HFrames_MDIForms_form-ACQ003003-1_popup_modal_29486_form_txtPrice_input")

# author input
# document.querySelector("#mainframe_VFrames_HFrames_MDIForms_form-ACQ003003-1_popup_modal_29486_form_txtAuthor_input")

# publisher nput
# document.querySelector("#mainframe_VFrames_HFrames_MDIForms_form-ACQ003003-1_popup_modal_29486_form_txtPublisher_input")

# isbn input
# document.querySelector("#mainframe_VFrames_HFrames_MDIForms_form-ACQ003003-1_popup_modal_29486_form_txtISBN_input")

# pub year input
# document.querySelector("#mainframe_VFrames_HFrames_MDIForms_form-ACQ003003-1_popup_modal_29486_form_txtPubYear_input")
