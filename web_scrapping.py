from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import requests
import pandas as pd

def function(url):
    try:
        page = requests.get(url)
        bs = BeautifulSoup(page.content,'html.parser')
        l1 = []
        l2 = []
        for tag in bs.find_all('img',alt=True):
            if(tag['alt']!='loading' and tag['alt']!='list image'):
                l1.append(tag['alt'])
        for i in  bs.find_all('span',attrs={'class':{'lister-item-year text-muted unbold'}}):
            k = i.get_text()
            if("I" not in k):
                k = k[1:5]
            else:
                k = k[5:9]
            l2.append(k)
        return l1,l2
    except HTTPError as e:
        return None
    except URLError as e:
        return None

print("Select one from below : ")
print("1. Top Grossing Movies")
print("2. Most watched film")
d = {
1:'https://www.imdb.com/list/ls000021718/',
2:'https://www.imdb.com/list/ls053826112/'
}
ans1,ans2 = function(d[int(input())])
if(ans1==None or ans2==None):
    print("Error Occured")
else:
    df = pd.DataFrame(list(zip(ans1,ans2)),columns=['Movie Name','Year'])
    print(df)
