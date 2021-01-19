#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import requests

links = []


def getLinkFriends(link):
    r"""获取bf友链页面的链接

    :param link: 你的友链地址
    """
    html = requests.get(url=link).content
    links.extend(re.findall(re.compile(r'<a href="https://(.*?)"'), str(html)))


def getGiteeFriends(user, repo):
    r"""获取Gitee友链

    :param user: Gitee用户名
    :param repo: Gitee友链仓库
    """
    gitee_repo = "https://gitee.com/api/v5/repos/" + user + "/" + repo + "/issues?state=open&sort=created&direction=asc&page=1&per_page=100"
    gitee_links = requests.get(url=gitee_repo).json()
    for gitee_link in gitee_links:
        try:
            if gitee_link['labels']:
                link = re.findall(re.compile('//(?:[-\w.]|(?:%[\da-fA-F]{2}))+'), gitee_link['body'])[0].replace("/","")
                links.append(link)
        except Exception:
            raise Exception('Gitee友链格式错误,请检查格式！！！')


def downloadFriends(url_prefix="https://image.thum.io/get/width/400/crop/800/allowJPG/wait/20/noanimate/https://",
                    url_suffix="", suffix="jpg"):
    r"""根据links里的友链下载到指定文件夹

    :param url_prefix: 截图网站前缀
    :param url_suffix: 截图网站后缀(如果有)
    :param suffix: 下载图片的后缀
    """
    os.system("mkdir img")
    for link in links:
        os.system("curl " + url_prefix + link + url_suffix +" -o ./img/" + link + "." + suffix)


if __name__ == '__main__':
    getLinkFriends("https://blog.zykjofficial.top/link/")
    getGiteeFriends("zykjofficial", "friends")
    downloadFriends()
