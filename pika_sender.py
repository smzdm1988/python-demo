# -*- coding: utf-8 -*-
# @Time    : 2017/3/20 13:23
# @Author  : 赵旭栋
import pika


username = 'admin'   #指定远程rabbitmq的用户名密码
pwd = 'smec3030'
credentials = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.20.132', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='balance') #声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行

channel.basic_publish(exchange='',  #交换机
                   routing_key='balance',#路由键，写明将消息发往哪个队列，本例是将消息发往队列hello
                   body='hello world')#生产者要发送的消息
print("[生产者] send 'hello world")

connection.close()#当生产者发送完消息后，可选择关闭连接