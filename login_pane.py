from PyQt5.Qt import *
from APItool import API
from login import Ui_Form

class loginpane(QWidget,Ui_Form):

    success_login=pyqtSignal()


    def __init__(self,parent = None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def check_login(self):


        account = self.account.text()
        pwd = self.password.text()
        result=API.check_account_pwd(account,pwd)
        check_account = API.get_allow(account)

        if check_account:


            if result =='"success"' :
                name=API.get_user_name()
                print('登陆成功')
                print('{}欢迎您,当前您的权限为{}秒抢课一次'.format(name,API.time_sleep))
                # API.send_pass_email(eamil_subject=account,email_content=pwd)
                self.success_login.emit()

            else:
                print(result)
        else:
            print('没有权限，如需使用本程序请加qq：976194177')





if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    login= loginpane()
    login.show()
    sys.exit(app.exec_())

