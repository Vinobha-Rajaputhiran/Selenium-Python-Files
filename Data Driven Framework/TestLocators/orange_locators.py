"""
orange_locators.py

Program : File containing the Locators for OrangeHRM
"""


class OrangeHRM_Locators:
   username = "username"
   password = "password"
   submit_button = "//button[@type='submit']"
   logout_button="//a[text()='Logout']"
   profile_button="//span[@class='oxd-userdropdown-tab']"
   url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
   dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
   excel_file = r"C:\Users\Vinoba\Desktop\Workspace\selenium_python\TestData\test_data.xlsx"
   sheet_number = "Sheet1"
   pass_data = "TEST PASS"
   fail_data = "TEST FAILED"