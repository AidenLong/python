import itchat as itchat
import requests
import time

def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation


def send_news():
    itchat.auto_login(hotReload=True)
    myfriend = itchat.search_friends(name=u'杨少伟')
    print(myfriend)
    Friend = myfriend[0]['UserName']
    message1 = str(get_news()[0])
    translation = get_news()[1]
    content = str(translation[translation.index("：") + 1:])
    print(content)
    message2 = str(content)
    message3 = '来自最爱你的人'
    itchat.send(message1, toUserName=Friend)
    itchat.send(message2, toUserName=Friend)
    itchat.send(message3, toUserName=Friend)
    time.time(100, send_news())
    print('send news success!')


if __name__ == '__main__':
    send_news()

