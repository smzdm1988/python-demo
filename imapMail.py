# -*- coding: utf-8 -*-
# @Time    : 2017/3/20 14:25
# @Author  : 赵旭栋

import imaplib
import email
import re
from email.header import decode_header

username = '460513666@qq.com'
password = 'vjcvmuegcveabhjg'


#字符编码转换方法
def my_unicode(s, encoding):
    if encoding:
        return unicode(s, encoding)
    else:
        return unicode(s)


def decode_multiline_header(s):
  ret = []

  for b, e in header.decode_header(re.sub(r'\n\s+', ' ', s)):
    if e:
      if e.lower() == 'gb2312':
        e = 'gb18030'
      b = b.decode(e)
    elif isinstance(b, bytes):
      b = b.decode('utf-8')
    ret.append(b)

  return ''.join(ret)


def getNewMail():
        conn = imaplib.IMAP4_SSL('imap.qq.com')
        conn.login(username, password)
        conn.select()
        resp, data = conn.search(None, 'UNSEEN')
       # print data
        #print data[0].split()
        for i in data[0].split():
            # get information of email
            resp, mailData = conn.fetch(i, "(RFC822)")
            mailText = mailData[0][1]
            msg = email.message_from_string(mailText)
            ls = msg["Subject"].split(' ')
            for j in ls:
                print decode_header(j)
            print ls




          #  print subject




if __name__ == '__main__':
  getNewMail()
 #print decode_header("=?utf-8?B?6L2m6L295ZC45bCY5ZmoMjkuOeWFjemCru+8geaxvei9puWbm+Wtow==?=\r\n")
