# Python-Projects
This repository serves as a collection of various Python projects.

---

## Keylogger
**Summary:** This script copies the victim's keystrokes and inputs them into a log file. From here, it sends an email every day with the log file attached. For this script to successfully run, Anti Virus needs to be disabled.

**Setup:** 
- Update Variables
  - **s_email** to your sender's email
  - **s_pwd** to your sender's password
  - **r_email** to your recipient's email
  - **log_dir** to the directory where your log file will be stored (optional)
- Configure Gmail
  - Under your Gmail account, go to **Security** and turn on **Less secure app access**

- Auto Startup
  - In Windows type **Windows_key+R** then **shell:startup**. In this new window, drag and drop your keylogger script. This will automatically run your script every time the victim machine turns on.

**Disclaimer:** This project is for education purposes only! This code should not be used in any malicious or unethical ways

---

## Password Generator
**Summary:** This script takes user input and creates a random password. These passwords are securely generated using the secrets library and verify complexity requirements by using RegEx.

**No setup required**

---
