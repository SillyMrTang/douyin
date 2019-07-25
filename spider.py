import re
import requests
from douyin.font import GetDouyinNum
from lxml import html


class DouyinData(object):
    def __init__(self, url):
        try:
            requests.packages.urllib3.disable_warnings()
            # url = requests.get(url).url.split("?")[0]
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/74.0.3729.169 Safari/537.36"
            }
            self.result = requests.get(url, verify=False, headers=headers).text
        except Exception as e:
            print(e)

    def dy_id(self):
        """
        抖音号
        :param:
        :return:
        """
        desc_header = re.findall('抖音ID：     (.*?)   </p>', self.result, re.S)
        desc_back = re.findall('<i class="icon iconfont ">(.*?)</i>', self.result, re.S)
        dic = GetDouyinNum(desc_back).get_num()
        res = desc_header[0]
        for i, j in dic.items():
            res = res.replace('<i class="icon iconfont "> &#' + i[1:] + '; </i>', j)
        return res

    def avater(self):
        """
        抖音头像
        :param:
        :return:
        """
        etree = html.etree
        res_html = etree.HTML(self.result)
        img_url = res_html.xpath('//*[@class="avatar"]/@src')
        if img_url:
            return img_url[0]
        return None

    def nickname(self):
        """
        抖音昵称
        :param:
        :return:
        """
        etree = html.etree
        res_html = etree.HTML(self.result)
        username = res_html.xpath('//*[@class="nickname"]/text()')
        if username:
            return username[0]
        return None

    def focus(self):
        """
        粉丝数
        :param:
        :return:
        """
        try:
            desc_header = re.findall(
                r'<span class="focus block"><span class="num">    (.*?)</span><span class="text">关注</span> </span>',
                self.result, re.S)
            desc_back = re.findall('<i class="icon iconfont follow-num">(.*?)</i>', self.result, re.S)
            dic = GetDouyinNum(desc_back).get_num()
            follower_res = desc_header[0]
            for i, j in dic.items():
                follower_res = follower_res.replace('<i class="icon iconfont follow-num"> &#' + i[1:] + '; </i>', j)
            return follower_res
        except Exception as e:
            print(e)

    def follower(self):
        """
        粉丝数
        :param:
        :return:
        """
        try:
            desc_header = re.findall(
                r'<span class="follower block"><span class="num">    (.*?)</span><span class="text">粉丝</span> </span>',
                self.result, re.S)

            desc_back = re.findall('<i class="icon iconfont follow-num">(.*?)</i>', self.result, re.S)

            dic = GetDouyinNum(desc_back).get_num()

            follower_res = desc_header[0]

            for i, j in dic.items():
                follower_res = follower_res.replace('<i class="icon iconfont follow-num"> &#' + i[1:] + '; </i>', j)
            return follower_res
        except Exception as e:
            print(e)

    def likes(self):
        """
        点赞数
        :param:
        :return:
        """
        try:
            desc_header = re.findall(
                r'<span class="liked-num block"><span class="num">    (.*?) </span><span class="text">赞</span></span>',
                self.result, re.S)
            desc_back = re.findall('<i class="icon iconfont follow-num">(.*?)</i>', self.result, re.S)
            dic = GetDouyinNum(desc_back).get_num()
            like_res = desc_header[0]
            for i, j in dic.items():
                like_res = like_res.replace('<i class="icon iconfont follow-num"> &#' + i[1:] + '; </i>', j)
            return like_res
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # http://v.douyin.com/SfPmAp/ 抖音个人首页分享链接
    dy = DouyinData("http://v.douyin.com/SfPmAp/")
    print("抖音ID:", dy.dy_id())
    print("抖音昵称:", dy.nickname())
    print("抖音头像:", dy.avater())
    print("粉丝数:", dy.follower())
    print("点赞数:", dy.likes())
    print("关注数:", dy.focus())
