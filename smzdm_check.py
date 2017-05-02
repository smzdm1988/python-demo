# -*- coding: utf-8 -*-
# @Time    : 2017/4/7 8:28
# @Author  : 赵旭栋
import requests
import sys

UserName = '460513666@qq.com'  # 用户名或者邮箱
PassWord = 'smec3030'  # 密码


class smzdm:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0',
                        'Host': 'zhiyou.smzdm.com',
                        }
        self.session = requests.session()

    def login(self):
        data = {
            'captcha': "",
            'redirect_url': 'http://www.smzdm.com',
            'rememberme': 'on',
        }
        data['username'] = self.username
        data['password'] = self.password
        loginURL = 'https://zhiyou.smzdm.com/user/login/ajax_check'
        try:
            req = self.session.post(loginURL, data=data, headers=self.headers)
            return req.json()['error_code']
        except Exception, e:
            print 'login error', e
            sys.exit(1)

    def checkin(self):
        signURL = 'http://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        checkinREQ = self.session.get(signURL, headers=self.headers)
        print '%s:%s'%('check in',checkinREQ.json())
        return checkinREQ.json()['data']

    def start(self):
        loginData = self.login()
        if loginData == 0:
            print '登陆成功'
            print '签到中....'

        checkinData = self.checkin()
        print checkinData
        if checkinData:
            print '签到成功'
            print '本次签到增加积分:', checkinData['add_point']
            print '连续签到次数:', checkinData['checkin_num']
            print '总积分:', checkinData['point']
        else:
            print '签到失败,请检查用户名和密码后重新运行.'


if __name__ == "__main__":
    smzmdLogin = smzdm(UserName, PassWord)
    smzmdLogin.start()