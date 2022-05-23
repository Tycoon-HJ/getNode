from logging import handlers
import requests
from lxml import etree
import datetime
import time

# 在当前py文件的目录中创建文件《节点.txt》
file = open("节点.txt","w")

# 格式化时间
def ftime(f = ''):
    return time.strftime('%Y%m%d', time.localtime()) 

# 模拟浏览器请求
handlers = {'ser-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

# 要爬去的目标网址
baseUrl = "https://www.cfmem.com";
res = requests.get(baseUrl,handlers)
content = res.content
html = etree.HTML(content)

# 获取文章的标题
baseTitle = html.xpath('//*[@id="Blog1"]/div[1]/article[1]/div[1]/h2/a')

# 得到里面的参数
urlParm = baseTitle[0].text.split(" ")[1]

# 今年
year = urlParm[0:4]

# 一共有多少条数据
count = urlParm[urlParm.find('点')+1:urlParm.find('条')]

# 4K
otherParm = urlParm[urlParm.find('清')+1:urlParm.find('上')]

# 今天的时间
today =  datetime.datetime.now()

# 链接需要的参数
todayParm = year + count + otherParm

# 爬起指定网址
url = "https://www.cfmem.com/"+ftime()[0:4]+"/"+ftime()[4:6]+"/"+str(today.year)+str(today.month)+str(today.day)+"-"+todayParm.lower()+"-v2rayclash-vpn.html"
res = requests.get(url,handlers)
content = res.content
html = etree.HTML(content)

# 数据解析
for k in range(1,int(count)+1):
    title = html.xpath('//*[@id="post-body"]/div[4]/pre/span['+str(k)+']')
    for i in range(0,len(title)):
        #处理元素获得节点
        descText = title[i].xpath('string(.)')
        # 将节点信息写入文件中
        file.write(descText+"\n")
# 关闭文件流        
file.close()