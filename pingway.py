import time
import os
def ping(address):
    out = os.popen('ping '+address+' -n 1').read()
    return(out)

count = 0

def jiankong(address):
  global count
  while True:
    oneping = ping(address)
    # print(oneping)
    if 'ms' in oneping:
        count = 0
        print('ping成功')
    else:
        count += 1
        print('ping失败。'+'连续失败次数:'+str(count))
    if count > 19:
        print('连续失败次数20次，杀死自身')
        os.popen('taskkill /f /im python.exe')
        os.popen('taskkill /f /im pythonw.exe')
    time.sleep(5)


jiankong('www.baidu.com')
    
