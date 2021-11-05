# Python Keylogger
**Disclaimer:** this project is for education purposes only! I'm not responsible for any unethical use of my code.

This script copies victims keystrokes and inputs it into a log file. From here it sends an email everyday with the log file attached.

**Note:** This script will be detected as a keylogger by anti virus so you'll need to diable that.

---
#### Update Variables
Prior to running the script you'll need to update the below variables in the [keylogger script](/keylogger.py):
- **s_email** to your senders email
- **s_pwd** to your senders password
- **r_email** to your recipients email
- **log_dir** to the directory where your log file will be stored (optional) 

---
#### Configuring Gmail
Under your Gmail account go to **Security** and turn on **Less secure app access**

![image](https://user-images.githubusercontent.com/70701922/140437395-f1e503f7-28b0-415a-961a-396d29f02d7b.png)
---
#### Auto Startup
In Windows type **Windows_key+R** then **shell:startup**. In this new window drag and drop your keylogger script.

![image](https://user-images.githubusercontent.com/70701922/140437834-e3f34e13-115f-4c41-8c37-3553afe25417.png)


Done! 
