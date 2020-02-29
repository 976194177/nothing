import requests
import json
import hashlib

class Get_GPA(object):

    def __init__(self,account,passward):

        self.account = account
        self.passward = passward
        self.session = requests.session()
        self.list_url = 'http://bkjws.sdu.edu.cn/b/cj/cjcx/xs/lscx'  # 查询历史成绩的url地址
        self.list_url1 = 'http://bkjws.sdu.edu.cn/b/cj/cjcx/xs/list'  # 查询本学期成绩的url地址

    def login(self):

        # 将密码进行md5加密
        m= hashlib.md5()
        m.update(self.passward.encode())
        sign = m.hexdigest()

        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
        data = {'j_username': self.account, 'j_password': sign}

        login_url = 'http://bkjws.sdu.edu.cn/b/ajaxLogin' # 登录的请求地址
        get_detail = 'http://bkjws.sdu.edu.cn/b/grxx/xs/xjxx/detail' # 获取学生姓名的地址

        html = self.session.post(url=login_url, data=data, headers=self.headers)
        if html.text == '"success"':
            print('登陆成功')
            detail_response = self.session.post(get_detail, headers=self.headers)
            self.name = json.loads(detail_response.text)['object']['xm']
        else:
            print(html.text)
            exit()

    def get_page(self):
        """
        该函数用来查询历史成绩和当前学期成绩的页数，并返回
        :return: 历史成绩和当前成绩的页数
        """

        data = {'aoData': '[{"name":"sEcho","value":1},{"name":"iColumns","value":10},{"name":"sColumns","value":""},{"name":"iDisplayStart","value":0},{"name":"iDisplayLength","value":20},{"name":"mDataProp_0","value":"xnxq"},{"name":"mDataProp_1","value":"kch"},{"name":"mDataProp_2","value":"kcm"},{"name":"mDataProp_3","value":"kxh"},{"name":"mDataProp_4","value":"xf"},{"name":"mDataProp_5","value":"kssj"},{"name":"mDataProp_6","value":"kscjView"},{"name":"mDataProp_7","value":"wfzjd"},{"name":"mDataProp_8","value":"wfzdj"},{"name":"mDataProp_9","value":"kcsx"},{"name":"iSortCol_0","value":5},{"name":"sSortDir_0","value":"desc"},{"name":"iSortingCols","value":1},{"name":"bSortable_0","value":false},{"name":"bSortable_1","value":false},{"name":"bSortable_2","value":false},{"name":"bSortable_3","value":false},{"name":"bSortable_4","value":false},{"name":"bSortable_5","value":true},{"name":"bSortable_6","value":false},{"name":"bSortable_7","value":false},{"name":"bSortable_8","value":false},{"name":"bSortable_9","value":false}]'}
        data1 = {'aoData': '[{"name":"sEcho","value":1},{"name":"iColumns","value":10},{"name":"sColumns","value":""},{"name":"iDisplayStart","value":0},{"name":"iDisplayLength","value":-1},{"name":"mDataProp_0","value":"function"},{"name":"mDataProp_1","value":"kch"},{"name":"mDataProp_2","value":"kcm"},{"name":"mDataProp_3","value":"kxh"},{"name":"mDataProp_4","value":"xf"},{"name":"mDataProp_5","value":"kssj"},{"name":"mDataProp_6","value":"kscjView"},{"name":"mDataProp_7","value":"wfzjd"},{"name":"mDataProp_8","value":"wfzdj"},{"name":"mDataProp_9","value":"kcsx"},{"name":"iSortingCols","value":0},{"name":"bSortable_0","value":false},{"name":"bSortable_1","value":false},{"name":"bSortable_2","value":false},{"name":"bSortable_3","value":false},{"name":"bSortable_4","value":false},{"name":"bSortable_5","value":false},{"name":"bSortable_6","value":false},{"name":"bSortable_7","value":false},{"name":"bSortable_8","value":false},{"name":"bSortable_9","value":false}]'}

        lscj_response = self.session.post(self.list_url,headers=self.headers,data=data)
        dqcj_response = self.session.post(self.list_url1,headers=self.headers,data=data1)

        lscj_pages = int(json.loads(lscj_response.text)["object"]["iTotalRecords"])
        dqcj_pages = int(json.loads(dqcj_response.text)["object"]["iTotalRecords"])

        return lscj_pages//20,dqcj_pages//20

    def search_GPA(self):
        """
        总学年绩点根据当前学期成绩和历史学期成绩加权平均得来
        :return:
        """

        zjd=0
        zxf=0
        zkscj = 0

        lscj_pages,dqcj_pages = self.get_page() #获取成绩的页数
        print(lscj_pages,dqcj_pages)

        for i in range(lscj_pages+1):

            # 为请求的data加上偏移项
            data = {'aoData': '[{"name":"sEcho","value":%s},{"name":"iColumns","value":10},{"name":"sColumns","value":""},{"name":"iDisplayStart","value":%s},{"name":"iDisplayLength","value":20},{"name":"mDataProp_0","value":"xnxq"},{"name":"mDataProp_1","value":"kch"},{"name":"mDataProp_2","value":"kcm"},{"name":"mDataProp_3","value":"kxh"},{"name":"mDataProp_4","value":"xf"},{"name":"mDataProp_5","value":"kssj"},{"name":"mDataProp_6","value":"kscjView"},{"name":"mDataProp_7","value":"wfzjd"},{"name":"mDataProp_8","value":"wfzdj"},{"name":"mDataProp_9","value":"kcsx"},{"name":"iSortCol_0","value":5},{"name":"sSortDir_0","value":"desc"},{"name":"iSortingCols","value":1},{"name":"bSortable_0","value":false},{"name":"bSortable_1","value":false},{"name":"bSortable_2","value":false},{"name":"bSortable_3","value":false},{"name":"bSortable_4","value":false},{"name":"bSortable_5","value":true},{"name":"bSortable_6","value":false},{"name":"bSortable_7","value":false},{"name":"bSortable_8","value":false},{"name":"bSortable_9","value":false}]' % (i+1,i*20)}
            response = self.session.post(self.list_url, headers=self.headers, data=data)

            for dic in json.loads(response.text)['object']['aaData']:
                if dic['kcsx'] == '必修' or dic['kcsx'] == '限选':
                    try:
                        print(dic['kcm'] + '的绩点是：' + str(dic['wfzjd']) + ',百分制成绩是：' + dic['kscjView'])
                        zkscj += dic['xf'] * float(dic['kscjView'])
                        zjd += dic['xf'] * float(dic['wfzjd'])
                        zxf += dic['xf']

                    except:
                        print('****************************************************************************')
                        print(dic['kcm']+'无法计算百分制成绩，为避免差错，该门课不计入绩点计算，请自行加上')
                        print('*****************************************************************************')

        for j in range(dqcj_pages + 1):

            # 为请求的data加上偏移项
            data1 = {'aoData': '[{"name":"sEcho","value":%s},{"name":"iColumns","value":10},{"name":"sColumns","value":""},{"name":"iDisplayStart","value":%s},{"name":"iDisplayLength","value":-1},{"name":"mDataProp_0","value":"function"},{"name":"mDataProp_1","value":"kch"},{"name":"mDataProp_2","value":"kcm"},{"name":"mDataProp_3","value":"kxh"},{"name":"mDataProp_4","value":"xf"},{"name":"mDataProp_5","value":"kssj"},{"name":"mDataProp_6","value":"kscjView"},{"name":"mDataProp_7","value":"wfzjd"},{"name":"mDataProp_8","value":"wfzdj"},{"name":"mDataProp_9","value":"kcsx"},{"name":"iSortingCols","value":0},{"name":"bSortable_0","value":false},{"name":"bSortable_1","value":false},{"name":"bSortable_2","value":false},{"name":"bSortable_3","value":false},{"name":"bSortable_4","value":false},{"name":"bSortable_5","value":false},{"name":"bSortable_6","value":false},{"name":"bSortable_7","value":false},{"name":"bSortable_8","value":false},{"name":"bSortable_9","value":false}]' % (j+1,j*20)}
            response = self.session.post(self.list_url1, headers=self.headers, data=data1)
            # print(response.text)
            for dic in json.loads(response.text)['object']['aaData']:
                if dic['kcsx'] == '必修' or dic['kcsx'] == '限选':
                    try:
                        print(dic['kcm'] + '的绩点是：' + str(dic['wfzjd']) + ',百分制成绩是：' + dic['kscjView'])
                        zkscj += dic['xf'] * float(dic['kscjView'])
                        zjd += dic['xf'] * float(dic['wfzjd'])
                        zxf += dic['xf']

                    except:
                        print('**************************************************************************')
                        print(dic['kcm'] + '无法计算百分制成绩，为避免差错，该门课不计入绩点计算，请自行加上')
                        print('*********************************************************************************')

        zhjd = float(zjd) / float(zxf)
        bfzcj = zkscj / zxf

        print('\n')
        print('*'*30)
        print('*' * 30)
        print('学生姓名:' + self.name)
        print('总学分：%s' % zxf)
        print('综合绩点:%s' % zhjd)
        print('综合百分制成绩:%s' % bfzcj)
        print('*' * 30)
        print('*' * 30)


if __name__ == "__main__":
    get_gpa = Get_GPA('学号','密码') # 这边的密码必须是之前教务系统的密码，不是现在统一身份登录的密码
    get_gpa.login()
    get_gpa.search_GPA()












