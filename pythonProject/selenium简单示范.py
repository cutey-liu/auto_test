from selenium简单示范 import webdriver
import time

class Mytest(object):
#初始化操作
def __init__(self):
    #创建浏览器
    self.driver = webdriver.Firefox()
    #将浏览器最大化
    self.driver.maximize_window()
    pass
    # 访问指定的url
def open_url(self,url):
    #访问我们的网页
    self.driver.get(url)
    #隐式等待 或者是全局等待时间 10秒钟 只要网页加载完 就跳转 不一定是10秒钟
    self.driver.implicitly_wait(10)
    #关闭浏览器的方法
    def close_driver(self):
    #close() 关闭当前窗口
    self.driver.close()
    pass
    # 结束的时候 会有清理的函数

def __del__(self):
    time.sleep(3)
    #关闭所有窗口
    self.driver.quit()
    pass
    pass


#在 主函数 里调用 封装的方法
if __name__ == '__main__':
# Common 进行实例化
my = Mytest()
my.open_url('http://www.baidu.com')
my.open_url('http://bilibili.com')
time.sleep(5)
#手动关闭 我们的网页
my.close_driver()