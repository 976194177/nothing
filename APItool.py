from requests import session,get
import hashlib
import smtplib
from email.mime.text import MIMEText  # 发送文本
from email.utils import formataddr
from email.header import Header
import re
import pymysql


class API(object):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    session = session()



    @classmethod
    def send_success_email(cls, kch:str,kxh:str,email_address:str) -> int:  # gqqenpwjffmybchj
        try:
        # 构造邮件的内容  plain:表示发送的是文本；HTML：表示发送的超文本
            message = MIMEText('课程号：'+kch+',课序号：'+kxh+'抢课成功', 'plain', 'utf-8')
            # 主题
            message['Subject'] = Header('恭喜您，抢课成功', 'utf-8')
            message['From'] = formataddr(['抢课程序', '976194177@qq.com'])
            message['To'] = formataddr([email_address, email_address])

            # 构造发送邮件的对象smtp，实例化SMTP()
            smtp = smtplib.SMTP()
            # 连接邮箱服务器 host 和 port
            smtp.connect('smtp.qq.com', 25)  # 可以简写  smtp=smtplib.SMTP('smtp.qq.com',25)
            # 登陆邮箱  第二个参数是qq邮箱授权码
            smtp.login('此处填入你的邮箱', '此处填入你的邮箱授权码')
            # 发送方，接收方（可以有多个['接收地址1'，'接收地址2'，....]），发送的消息（字符串类型，使用邮件格式）
            # message.as_string() 将MIMEText对象变为str
            smtp.sendmail('976194177@qq.com', email_address, message.as_string())
            # 退出邮箱,结束SMTP会话
            smtp.quit()
            print('发送邮件成功')

        except Exception as e:
            print('发送失败',e)

    @classmethod
    def check_account_pwd(cls,account,password):
        m = hashlib.md5()
        m.update(password.encode())
        sign = m.hexdigest()

        data = {
            'j_username': account,
            'j_password': sign
        }

        # 登录
        html = API.session.post(url='http://bkjwxk.sdu.edu.cn/b/ajaxLogin', data=data, headers=API.header)

        return html.text


    # 该程序用来抢课
    @classmethod
    def select_class(cls,kch,kxh):

        url = 'http://bkjwxk.sdu.edu.cn/b/xk/xs/add/'+kch+'/'+kxh

        response = API.session.post(url, headers=API.header)

        return response.text



    @classmethod
    # 这边通过mysql添加了程序使用权限，可自行修改
    def get_allow(cls,account):
        db = pymysql.connect(host='ip地址', user='root', password='root', port=3306,
                             db='test')
        cursor = db.cursor()

        sql = "SELECT * FROM allow_account where student_id = %s" %account
        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) == 0:
            return False
        else:
            cls.time_sleep = data[0][1]
            return True

    @classmethod
    def get_user_name(cls):
        try:
            response = API.session.get('http://bkjwxk.sdu.edu.cn/f/common/main',headers = API.header)
            compile = re.compile('class="username">(.*?)</span></a></li>')
            name = re.findall(compile,response.text)[0]
            return name


        except:
            return None







