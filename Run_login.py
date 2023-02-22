'''
test--淘宝商品数据抓取
Author：DouZ
Date:2022/06/19
'''
from Get_Cookies import create_chrome_drive,add_cookies

brower = create_chrome_drive()
brower.get('https://www.taobao.com')
add_cookies(brower,'taobao1.json')
# 搜索
# brower.get('https://s.taobao.com/search?q=switch')
brower.get('https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA')