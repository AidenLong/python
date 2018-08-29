#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''''
__Author__:沂水寒城
功能: 对URL进行分割，基于urlparse, publicsuffix, urllib编写
'''
from urlparse import urlparse
import codecs
from publicsuffix import PublicSuffixList
from urllib import splitport
import re


def domain_split(server_domain):
    '''''
    server_domain为网站所用服务名+域名
    分割域名, 得到前缀(服务名)、主机域名、后缀(顶级域名)
        输入www.baidu.com，输出'www', 'baidu', 'com'
        输入172.31.137.240，输出'', '172.31.137.240', ''
    '''
    PSL_FILE = codecs.open('public_suffix_list.dat', encoding='utf8')
    psl = PublicSuffixList(PSL_FILE)
    domain = psl.get_public_suffix(server_domain)
    # 取域名的第一个字段，即第一个'.'之前的为主机域名, 后面为顶级域名，前面为所使用的服务
    if '.' in domain:
        server = server_domain[:-len(domain)]
        host = domain[:domain.index('.')]
        top = domain[domain.index('.'):]
        hostname = server + host + top
    else:  # 说明提取域名失败，例如172.31.137.240等IP形式，此时全部当作主机域名
        server = ''
        host = server_domain
        top = ''
        hostname = server_domain
    return server, host, top, hostname


def url_split_new(url):
    '''''
    url分割
    '''
    if not url.startswith('http'):  # 补全协议，否则urlparse出错
        url = 'http://' + url
    parts = urlparse(url)
    # 服务+域名'www.baidu.api.com.cn'切分
    server, host, top, hostname = domain_split(parts.netloc)
    host, port = splitport(host)
    if port == None: port = ''
    return {'protocol': parts.scheme, 'hostname': hostname, 'path': parts.path}


if __name__ == '__main__':
    print
    url_split_new('http://www.baidu.com/')
