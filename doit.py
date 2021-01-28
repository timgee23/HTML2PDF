'''
Created on Jan 27, 2021

@author: timmygee
'''
import requests
from bs4 import BeautifulSoup as BS
import pdfkit
import time



def doit(directory,list_to_process):
    numtodo=len(list_to_process)
    numnext=1
    try:
        for url in list_to_process:
            url=url.strip()
            print("-----------------\nNow processing %s" % url)
            print("Number %d of %d" % (numnext,numtodo))
            code = requests.get(url)
            plain = code.text
            s=BS(plain,"html.parser")
            article=s.article
            footer=s.footer
# now strip all the links
            links=footer.findAll('a')
            for l in links:
                l.extract()
            todo="<meta charset='utf-8'ex/>"+str(article)+str(footer)
            #build the filename
            
            name=url.split('/')[-2]
            outfile=directory+"/"+name+"_"+str(numnext)+".pdf"
            pdfkit.from_string(todo,outfile)
            numnext+=1
            #time.sleep(3)
    except Exception:
        print("Error processing %s" % url)
        fn=open("failed_save.txt","w")
        fn.write(todo)
        fn.close()
        return 2
            

        
    

