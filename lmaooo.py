import requests
from math import ceil
import os

def getposts(subreddit,number ):
    user = os.environ['reddit_username']
    passw = os.environ['reddit_passwd']

    auth = requests.auth.HTTPBasicAuth('PDIUI8AZdt825HT5KuiO9g', 'HuIr0Jy5JmLErLqw64fFZoc3jij02A')
    data = {'grant_type': 'password',
            'username': user,
            'password': passw}
    #subreddit=input("Enter subreddit: ")
    #number=int(input("Enter number of posts needed: "))
    if number>100:
        multiplier=ceil(number/100)
        number=100
    else:
        multiplier=1
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    parameters={'limit':number}
    urllist=[]
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
    for i in range(multiplier):
        res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/top?t=day",
                      headers=headers,
                      params=parameters)    
        for post in res.json()['data']['children']:
            if 'https://v.redd.it/' not in post['data']['url'] and 'https://www.reddit.com/gallery/' not in post['data']['url']:
                urllist.append(post['data']['url'])
            else:
                urllist.append('https://www.reddit.com'+post['data']['permalink'])
            #urllist.append('https://www.reddit.com'+post['data']['permalink'])
        else:
            fullname = post['kind'] + '_' + post['data']['id']
            parameters['after'] = fullname
        print(f'iteration {i+1}')
    info='['
    length=len(urllist)
    for i in range(length):
        if (i==length-1):
            info+='\''+urllist[i]+'\''+']'
        else:
            info+='\''+urllist[i]+'\''+','
    with open ('temp.txt','w',encoding='utf-8') as f:
        f.write(info)
    print(len(urllist))
