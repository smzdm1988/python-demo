# -*- coding: utf-8 -*-
# @Time    : 2017/3/14 14:54
# @Author  : 赵旭栋
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((\
        Header(name, 'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'zhaoxudong@smec-cn.com'
password = 'notes'
to_addr = 'zhaoxudong@smec-cn.com'
cc_addr = 'zhaoxudong@smec-cn.com'
smtp_server = 'oaserver01.smec-cn.com'

msg = MIMEText('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Content-Style-Type" content="text/css"/>'+
  '<meta name="generator" content="Aspose.Words for .NET 15.1.0.0" />'+
  '<title></title>'+
 '</head>'+
 '<body>'+
 '<div>'+
   '<p style="margin:0pt; orphans:0; widows:0"><span style="font-family:宋体; font-size:14pt">各位领导、同事：</span><span style="font-family:宋体; font-size:14pt"> </span></p>'+
   '<p style="margin:0pt; orphans:0; widows:0"><span style="width:21pt; text-indent:0pt; display:inline-block"></span><span style="width:75pt; text-indent:0pt; display:inline-block"></span><span style="font-family:宋体; font-size:14pt"> </span><span style="font-family:宋体; font-size:14pt">烦请各位于本周之内提供各条线的最新新闻，用于公司网站，若暂时没有新闻，也请您于本周内发送邮件告知于我，公司网站新闻更新的工作重要，请各位领导、同事务必重视此项工作，谢谢各位支持。</span></p>'+
   '<p style="margin:0pt; orphans:0; widows:0"><span style="width:95pt; text-indent:0pt; display:inline-block"></span><span style="font-family:宋体; font-size:14pt"> </span><span style="font-family:宋体; font-size:14pt">请各位在回复时，务必在邮件中加入以下这段话：</span></p>'+
   '<p style="margin:0pt; orphans:0; text-align:justify; widows:0"><span style="width:21pt; text-indent:0pt; display:inline-block"></span><span style="width:70pt; text-indent:0pt; display:inline-block"></span><span style="color:#ff0000; font-family:宋体; font-size:24pt">新闻已经由本部长</span><span style="color:#ff0000; font-family:宋体; font-size:24pt">/</span><span style="color:#ff0000; font-family:宋体; font-size:24pt">主任</span><span style="color:#ff0000; font-family:宋体; font-size:24pt">/</span><span style="color:#ff0000; font-family:宋体; font-size:24pt">总经理同意对外发布。</span></p>'+
   '<p style="margin:0pt; orphans:0; text-align:justify; widows:0"><span style="font-family:宋体; font-size:10pt">Best Regards,</span><br /><br /><span style="font-family:宋体; font-size:10pt">--------------------------------------</span><br /><span style="font-family:宋体; font-size:10pt">赵旭栋</span><br /><span style="font-family:宋体; font-size:10pt">企业管理部</span><span style="font-family:宋体; font-size:10pt"> </span><br /><span style="font-family:宋体; font-size:10pt">上海三菱电梯有限公司</span><span style="font-family:宋体; font-size:10pt"> </span><br /><span style="font-family:宋体; font-size:10pt">Zhao </span><span style="font-family:宋体; font-size:10pt">Xudong</span><br /><span style="font-family:宋体; font-size:10pt">Enterprise Management Department</span><br /><span style="font-family:宋体; font-size:10pt">SHANGHAI MITSUBISHI ELEVATOR CO., LTD</span><span style="font-family:宋体; font-size:10pt">.</span><br /><span style="font-family:宋体; font-size:10pt">E-mail:zhaoxudong@smec-cn.com</span><br /><span style="font-family:宋体; font-size:10pt">Web :www.smec-cn.com</span><br /><span style="font-family:宋体; font-size:10pt">Tel :021-24083477</span><br /><span style="font-family:宋体; font-size:10pt">Fax :021-24083044</span></p>'+
  '</div>'+
 '</body>'+
'</html>','html', 'utf-8')
msg['From'] = _format_addr(u'赵旭栋<%s>' % from_addr)
msg['To'] = to_addr
msg['Cc'] = cc_addr
msg['Subject'] = Header(u'一周外网新闻更新', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr,cc_addr], msg.as_string())
server.quit()