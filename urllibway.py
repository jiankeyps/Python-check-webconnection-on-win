import urllib.request
import time
import os
def req(address):
    try:
       urllib.request.urlopen(address)
       return True
    except:
       return False

count = 0

def jiankong(address):
  global count
  while True:
    oneping = req(address)
    # print(oneping)
    if oneping == True:
        count = 0
        print('联网成功')
    else:
        count += 1
        print('联网失败。'+'连续失败次数:'+str(count))
    if count > 10:
        print('连续失败次数10次，杀死自身，重启网络程序')
        os.popen('taskkill /f /im python.exe')
        os.popen('taskkill /f /im pythonw.exe')
    time.sleep(10)


jiankong('http://www.baidu.com')
    
