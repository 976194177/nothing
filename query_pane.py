from PyQt5.Qt import QWidget,QApplication
from select_class_pane import Ui_Form
import APItool
from time import sleep
import json

class querypane(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def auto_select_class(self):
        # 账户及选课信息

        kch=self.kch.text()
        kxh=self.kxh.text()
        email_address=self.kxh_2.text()

        # 程序运行状态
        select_class_state = True
        try_num = 2
        while select_class_state:
            try:
                select_class_result=APItool.API.select_class(kch,kxh)

                result = json.loads(select_class_result)

                if result["result"] =='success':
                    if '你曾学过此门课' in result['msg']:
                        print(result['msg'])
                        select_class_state=False
                    elif '人数已满' in result['msg']:
                        print(result['msg']+'将在{}秒后为您进行第{}次抢课。'.format(APItool.API.time_sleep,try_num))

                        try_num+=1


                    else:
                        print('课程号：{}，课序号：{}，选课成功'.format(kch,kxh))
                        if len(email_address)>0:
                            APItool.API.send_success_email(kch=kch,kxh=kxh,email_address=email_address)
                        try_num = 2
                        select_class_state=False

                else:
                    print(result['msg'])
                    break
            except Exception as e:
                print(e)
                break
            finally:
                print('********************************************************************')
                sleep(APItool.API.time_sleep)







if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    windows=querypane()
    windows.show()
    sys.exit(app.exec_())








