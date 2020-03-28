"""
功能描述：配置邮件，实现发送邮件的功能

解析：
    1-读取配置，调用readconfig
    2-创建邮件链接配置（）
    3-创建邮件内容（添加附件report）
    4-调用发送邮件的方法
"""
from smtplib import SMTP
#发送 Html内容邮件
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
def ConfigEmail():
#----------------------------------------配置邮属性---------------------------------------
    #发送邮箱
    sender = 'yankai_hw@163.com'
    #接收邮箱
    reciver = 'yankai_yk1@163.com'
    #发送邮件主题
    t =time.strftime('%y-%m-%d %H-%M-%S',time.localtime())
    subject = '自动化测试结果时间为'+t
    #发送邮箱服务器
    smtpsever = 'smtp.163.com'
    #发送邮箱用户/密码
    username = 'yankai_hw@163.com'
    password = '123yankai'

    #组装邮件内容和标题，中文需要参数utf-8,单字字节不需要
    content = '我是文件内容啊！！！你瞅啥'
    msg = MIMEText(content,'utf-8')
    subject = '我是标题啊！！！'
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = sender
    msg['To'] = reciver

    #登录并发送邮件
    try:
        s = smtplib.SMTP()
        s.connect(smtpsever)
        s.login(username,password)
        s.sendmail(sender,reciver,msg.as_string())
    except:
        print('邮件发送失败')
    else:
        print('邮件发送成功')
    finally:
        s.quit()

#调试发送邮件
ConfigEmail()

