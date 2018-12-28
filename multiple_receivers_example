#使用谷歌邮箱发送中文邮件（群发不同内容）
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass
import time

#接口设置

gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#登录邮箱:登陆之前必须开启谷歌账户‘对安全性较低的应用的访问权限’，试完代码后记得关掉
while True:
    try:
        #输入用户信息
        user = input('请输入邮箱账号：')
        password = getpass.getpass('请输入邮箱密码：')
        gmail.login(user, password)
        print('登陆成功')
        break
    except:
        choice = input('认证未通过，是否重新输入用户信息？y/n\n')
        if choice == 'y':
            continue
        else: 
            print('登陆成功')
            break

#提取txt文本内容
with open ('chengji.txt', 'r', encoding="utf-8") as chengji:
    txt = chengji.read()
txt = txt.strip('\ufeff')
txt_list = txt.split('\n')
#print(len(txt_list))
print(txt_list)

#编辑好群发邮件的标题
subject = 'python考试成绩通知（假的，代码测试邮件）'


#根据不同收件人编辑发送信息和发送对象
i = 0
while i < len(txt_list):
    #输入发送信息
    to = txt_list[i] 
    text = "您的python考试成绩是" + txt_list[i + 2]
    message = MIMEText(text,'plain','utf-8')
    message['Subject'] = Header(subject,'utf-8')
    
    #发送邮件
    result = gmail.sendmail(user,to,message.as_string())
    print(result)
    
    #下一个收件人
    i += 3
    time.sleep(15)

gmail.close()
