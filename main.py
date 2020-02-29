from PyQt5.Qt import *

from login_pane import loginpane
from query_pane import querypane
from APItool import API

if __name__ =='__main__':
    # API.get_beijingtime()
    import sys
    app=QApplication(sys.argv)

    login_pane=loginpane()
    query_pane = querypane()

    def success_login_slot():
        login_pane.hide()
        query_pane.show()

    login_pane.success_login.connect(success_login_slot)
    login_pane.show()

    sys.exit(app.exec_())

