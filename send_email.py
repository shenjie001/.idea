import  smtplib
import  os.path
import time
from email.mime.text import MIMEText
from  email.header import Header
import  HtmlTestRunner


def sendemail(connect,title,from_name,from_adress,to_adress,severport,severip,username,password):
    msg = MIMEText(connect,_subtype='html',_charset='utf-8')
    msg['subject']=Header(title,'utf-8')
    msg['to']= ','.join(to_adress)
    msg['from']= from_name
    try:
        s = smtplib.SMTP_SSL(severip,severport)
        s.login(username,password)
        s.sendmail(from_adress,to_adress,msg.as_string())
        print('%s---发送邮件成功'&time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except Exception:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        print(Exception)
def info():
    to = ['jie.shen@melot.cn']
    config={
        "from":"jie.shen@melot.cn",
        "from_name":'web自动化测试报告',
        "to_adress":to,
        "serverip":"smtp.exmail.qq.com",
        "serverport":"465",
        "username":"jie.shen@melot.cn",
        "password":"nTbau9bcGe669a8N"

    }
    title = 'web自动化测试报告'
    report_path = "E:\\result.html"
    # report_path  =
    f = open(report_path,'rb')
    mail_date = f.read()
    f.close()
    sendemail(mail_date,title,config['from_name'], config['from'], config['to_adress'], config['serverport'],
                config['serverip'],config['username'], config['password'])



