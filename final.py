
# -*- coding: cp949 -*-

import requests,os,sys
from bs4 import BeautifulSoup
from collections import Counter
import re


class Final:
    

    def __init__(self,url):
        self.url = url
        

    def content(self):
        
        res = requests.get(self.url)
        return res.content

    def soup(self,content):
        s = BeautifulSoup(content,"html.parser")
        return s
    
class Song_Text(Final):

    def submit(self,r,cla):
        my_song_list = []
        submits = r.find_all(id=cla)
        for submit in submits:
            my_song_list.append(submit.get_text())
        return my_song_list
    
class Funtion:

    def __init__(self,filename):
        self.filename = filename
        
    
    
    def helper(self):
      with open(self.filename,'r') as f:
        words = f.read().split()
        
      res = []  
      rd={}
      for word in words:
        word = re.sub('[().\',]','',word)
        word=word.lower()
        res.append(word)
        
      for my_word in res:
        rd[my_word] = res.count(my_word)
        
      return rd
    
  
    def print_word(self,helper):

      print helper
      
        
    def length(self,x):
        return x[1]
    
    def print_top(self,helper,point):
      target = helper
      res =target.items()
      
      res.sort(key=point,reverse=True)
      p = 0
      for t1,t2 in res:
        if p == 5 :
          break
        else:
          print t1,t2
          p=p+1

    def print_histogram(self,helper):
      target = helper
      for t1,t2 in target.items():
        print t1,":\t"+"*"*t2+"\n"
      
    
def main():
    
    
    if len(sys.argv) == 3:
        my_result = Funtion(sys.argv[2])
        my_helper= my_result.helper()
        my_point = my_result.length
    else:
        print 'usage: python [파일이름] {옵션1 | 옵션2 | 옵션3} [대상파일]'
        sys.exit(1)

    option = sys.argv[1]
    
    
    if option == '-c':
        my_result.print_word(my_helper)
    elif option == '-t':
        my_result.print_top(my_helper,my_point)
    elif option == '-h':
        my_result.print_histogram(my_helper)
    else:
        print 'unknown option'
        sys.exit(1)

    


if __name__ == "__main__":

    
    Bohe = Song_Text('https://www.songtexte.com/songtext/freddie-mercury/bohemian-rhapsody-23982857.html')
    res=Bohe.content()
    soup=Bohe.soup(res)
    song=Bohe.submit(soup,"lyrics")
    path = os.path.dirname(__file__)
    total = os.path.join(path,"attachments/sample.txt")
    with open(total, 'w') as f:
        f.write(song[0])
    main()
    

    
    
    
    
   

    
    
