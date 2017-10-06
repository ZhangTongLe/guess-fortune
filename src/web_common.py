#!提供网页操作的公共方法
from urllib.request import urlretrieve

#!抓取网页数据
def download(url, process):  
    try:
        retval = urlretrieve(url)[0]
    except IOError as error:
        print(error)
        retval = None
        return -1

    if retval:
        return process(retval)
