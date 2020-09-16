#importing URL LIBRARY, Beautiful Soup and Regular Expression Checker
import urllib.request
from bs4 import BeautifulSoup
import re
from os import system
import webbrowser
import sys
import html
import time
import json

college_url="https://www.mrcet.com" 
college_page=urllib.request.urlopen(college_url)

soup = BeautifulSoup(college_page, "html")

college_html=soup.prettify()
doc_links={}
hyper_links={}
main_ref_links={}
section_ref_links={}
subsection_ref_links={}




def main_link_all(navigation_header_soup):
    count=0
    navigation_header_dict={}
    navigation_header_links=navigation_header_soup[0].ul.findAll(recursive=False)
    for i in range(len(navigation_header_links)):
        navigation_header_links[i]=navigation_header_links[i].findAll('a')    
    temp=""
    for i in navigation_header_links:
        l={}
        for j in i:
            if(j["href"]=="#"):
                temp=j.text
            else:    
                if("&" not in j["href"]):
                    if("https" in j["href"]):
                        l[j.text]=j["href"]
                    elif(".html" in j["href"]):
                        l[j.text]="https://www.mrcet.com/"+j["href"]
                    else:
                        doc_links[j.text]="https://www.mrcet.com/"+j["href"].replace(" ","%20")
                else:
                    pass
            main_ref_links[temp]=l 




main_link_all(soup.select('nav[class="navbar navbar-inverse"]'))




section_dict={}
for i in main_ref_links.values():
    for j in dict(i.items()):
        section_dict[j]=i[j]



for i in section_dict:
    hyper_links[i]=section_dict[i].strip().replace(" ","%20")




def sub_link_all(sub_url):
    try:
        sub_page=urllib.request.urlopen(sub_url,timeout=2)
    except:
        return
    sub_soup = BeautifulSoup(sub_page, "lxml")
    sub_html=sub_soup.prettify()
    section_list=[]
    anchor_list_1=[]
    anchor_dict={}
    new_link=""
    section_required=(sub_soup.find('section',{"class":re.compile("padding")}))
    if(section_required==None):
        return
    x=section_required.find("div",{"class":"container"})
    if(len(x.findAll("div",{"class":re.compile("col-md")}))!=0):
        section_list.append(x.findAll("div",{"class":re.compile("col-md")}))
        if(len(section_list)!=0):
            for i in section_list[0]:
                anchor_list_1.append(i.findAll("a"))
            if(len(anchor_list_1)!=0): 
                for i in range(len(anchor_list_1)):
                    for j in range(len(anchor_list_1[i])):
                        if(len(anchor_list_1[i][j])!=0 and (not anchor_list_1[i][j].has_attr("data-parent")) and (anchor_list_1[i][j] not in anchor_dict.values()) and (anchor_list_1[i][j]["href"]!="#")):
                            anchor_dict[anchor_list_1[i][j].text]=anchor_list_1[i][j]
                            if(anchor_list_1[i][j].text.strip()!=""):
                                if(".pdf" in anchor_list_1[i][j]["href"] or ".jpg" in anchor_list_1[i][j]["href"] or ".png" in anchor_list_1[i][j]["href"] or ".gif" in anchor_list_1[i][j]["href"]):
                                    if("mrcet.com" not in anchor_list_1[i][j]["href"] and "http" not in anchor_list_1[i][j]["href"]):
                                        doc_links[sub_url+":"+anchor_list_1[i][j].text]=college_url+"/"+anchor_list_1[i][j]["href"].replace(" ","%20")
                                    else:
                                        doc_links[sub_url+":"+anchor_list_1[i][j].text]=anchor_list_1[i][j]["href"].replace(" ","%20")
                                else:
                                    if("mrcet.com" not in anchor_list_1[i][j]["href"] and "http" not in anchor_list_1[i][j]["href"]):
                                        new_link=college_url+"/"+anchor_list_1[i][j]["href"].strip().replace(" ","%20")
                                        section_ref_links[sub_url+":"+anchor_list_1[i][j].text]=new_link
                                    else:
                                        new_link=anchor_list_1[i][j]["href"].strip().replace(" ","%20")
                                        section_ref_links[sub_url+":"+anchor_list_1[i][j].text]=new_link
                                    
                            else:        
                                if(".pdf" in anchor_list_1[i][j]["href"] or ".jpg" in anchor_list_1[i][j]["href"] or ".png" in anchor_list_1[i][j]["href"] or ".gif" in anchor_list_1[i][j]["href"]):
                                    if("mrcet.com" not in anchor_list_1[i][j]["href"] and "http" not in anchor_list_1[i][j]["href"]):
                                        doc_links[sub_url+":"+anchor_list_1[i][j]["href"]]=college_url+"/"+anchor_list_1[i][j]["href"].replace(" ","%20")
                                    else:
                                        doc_links[sub_url+":"+anchor_list_1[i][j]["href"]]=anchor_list_1[i][j]["href"].replace(" ","%20")
                                else:
                                    if("mrcet.com" not in anchor_list_1[i][j]["href"] and "http" not in anchor_list_1[i][j]["href"]):
                                        new_link=college_url+"/"+anchor_list_1[i][j]["href"].strip().replace(" ","%20")
                                        section_ref_links[sub_url+":"+anchor_list_1[i][j].text]=new_link
                                    else:
                                        new_link=anchor_list_1[i][j]["href"].strip().replace(" ","%20")
                                        section_ref_links[sub_url+":"+anchor_list_1[i][j].text]=new_link
    elif(x.findAll("div",{"class":re.compile("container")})!=None):
        section_list.append(x.findAll("div",{"class":re.compile("container")}))
        if(len(section_list)!=0):
            for i in section_list[0]:
                anchor_list_1.append(i.findAll("a"))
            if(len(anchor_list_1)!=0): 
                for i in range(len(anchor_list_1)):
                    for j in range(len(anchor_list_1[i])):
                        if(len(anchor_list_1[i][j])!=0 and (not anchor_list_1[i][j].has_attr("data-parent")) and (anchor_list_1[i][j] not in anchor_dict.values()) and (anchor_list_1[i][j]["href"]!="#")):
                            anchor_dict[anchor_list_1[i][j].text]=anchor_list_1[i][j]
                            if(anchor_list_1[i][j].text.strip()!=""):
                                if(".pdf" in anchor_list_1[i][j]["href"] or ".jpg" in anchor_list_1[i][j]["href"] or ".png" in anchor_list_1[i][j]["href"] or ".gif" in anchor_list_1[i][j]["href"]):
                                    if("mrcet.com" not in anchor_list_1[i][j]["href"] and "http" not in anchor_list_1[i][j]["href"]):
                                        doc_links[sub_url+":"+anchor_list_1[i][j].text]=college_url+"/"+anchor_list_1[i][j]["href"].replace(" ","%20")
                                    else:
                                        doc_links[sub_url+":"+anchor_list[i][j].text]=anchor_list_1[i][j]["href"].replace(" ","%20")
                                else:
                                    if("mrcet.com" not in anchor_list_1[i][j]["href"] and "http" not in anchor_list_1[i][j]["href"]):
                                        new_link=college_url+"/"+anchor_list_1[i][j]["href"].strip().replace(" ","%20")
                                        section_ref_links[sub_url+":"+anchor_list_1[i][j].text]=new_link
                                    else:
                                        new_link=anchor_list_1[i][j]["href"].strip().replace(" ","%20")
                                        section_ref_links[sub_url+":"+anchor_list_1[i][j].text]=new_link                                    
                            else:        
                                if(".pdf" in anchor_list_1[i][j]["href"] or ".jpg" in anchor_list_1[i][j]["href"] or ".png" in anchor_list_1[i][j]["href"] or ".gif" in anchor_list_1[i][j]["href"]):
                                    if("mrcet.com" not in anchor_list_1[i][j]["href"] and "http" not in anchor_list_1[i][j]["href"]):
                                        doc_links[sub_url+":"+anchor_list_1[i][j]["href"]]=college_url+"/"+anchor_list_1[i][j]["href"].replace(" ","%20")
                                    else:
                                        doc_links[sub_url+":"+anchor_list_1[i][j]["href"]]=anchor_list_1[i][j]["href"].replace(" ","%20")
                                else:
                                    if("mrcet.com" not in anchor_list_1[i][j]["href"] and "http" not in anchor_list_1[i][j]["href"]):
                                        new_link=college_url+"/"+anchor_list_1[i][j]["href"].strip().replace(" ","%20")
                                        section_ref_links[sub_url+":"+anchor_list_1[i][j]["href"]]=new_link
                                    else:
                                        new_link=anchor_list_1[i][j]["href"].strip().replace(" ","%20")
                                        section_ref_links[sub_url+":"+anchor_list_1[i][j]["href"]]=new_link
    else:
        x=section_required.findAll("a")
        for i in x:
            if(i.text.strip()!=""):
                if(".pdf" in i["href"] or ".jpg" in i["href"] or ".png" in i["href"] or ".gif" in i["href"]):
                    if("mrcet.com" not in i["href"] and "http" not in i["href"]):
                        doc_links[sub_url+":"+i.text]=college_url+"/"+i["href"].strip().replace(" ","%20")
                    else:
                        doc_links[sub_url+":"+i.text]=i["href"].strip().replace(" ","%20")
                else:
                    if("mrcet.com" not in i["href"] and "http" not in i["href"]):
                        new_link=college_url+"/"+i["href"].strip().replace(" ","%20")
                        section_ref_links[sub_url+":"+i.text]=new_link
                    else:
                        new_link=i["href"].strip().replace(" ","%20")
                        section_ref_links[sub_url+":"+i.text]=new_link                    
            else:        
                if(".pdf" in i["href"] or ".jpg" in i["href"] or ".png" in i["href"] or ".gif" in i["href"]):
                    if("mrcet.com" not in i["href"] and "http" not in i["href"]):
                        doc_links[sub_url+":"+i["href"]]=college_url+"/"+i["href"].strip().replace(" ","%20")
                    else:
                        doc_links[sub_url+":"+i["href"]]=i["href"].strip().replace(" ","%20")
                else:
                    if("mrcet.com" not in i["href"] and "http" not in i["href"]):
                        new_link=college_url+"/"+i["href"].strip().replace(" ","%20")
                        section_ref_links[sub_url+":"+i["href"]]=new_link
                    else:
                        new_link=i["href"].strip().replace(" ","%20")
                        section_ref_links[sub_url+":"+i["href"]]=new_link 



for i in section_dict.values():
    sub_link_all(i)



def sub_internal_url_func(sub_internal_link):
        sub_internal_url=sub_internal_link
        sub_internal_page=urllib.request.urlopen(sub_internal_url)
        sub_internal_soup = BeautifulSoup(sub_internal_page, "lxml")
        sub_internal_html=sub_internal_soup.prettify()
        section_required=(sub_internal_soup.find('section',{"class":re.compile("padding")}))
        rex=section_required.findAll('div',class_=re.compile("col-md"))
        new_link=""
        if(len(rex)!=0):
            req=[]
            flag=0
            for i in rex:
                for k in i["class"]:
                    if("hidden" not in k):
                        flag=1
                    else:
                        flag=0
                if(flag==1):
                    req.append(i)
            anchor_list={}
            anchor_text={}
            my_dict={}
            new_link=""
            count=1
            if(req!=None):     
                for i in req:
                    x=i.find("div",{"class":"panel-group","id":"accordion"})
                    if(x!=None):
                        y=x.findAll("div",{"class":"panel panel-default"},recursive=False)
                        if(y!=None):
                            for i in range(len(y)):
                                z= y[i].findAll("a")
                                for j in range(len(z)):
                                    if(z[j].has_attr("data-parent")):
                                        pass
                                    else:
                                        if(z[j].text.strip()!=""):  
                                            if(".pdf" in z[j]["href"] or ".jpg" in z[j]["href"] or ".png" in z[j]["href"] or ".gif" in z[j]["href"]):
                                                if("mrcet.com" not in z[j]["href"] or "http" not in z[j]["href"]):
                                                    doc_links[sub_internal_link+":"+y[i].find("div",{"class":"panel-heading"}).text.strip()+z[j].text.strip()]=college_url+"/"+z[j]["href"].strip().replace(" ","%20")
                                                else:
                                                    doc_links[sub_internal_link+":"+y[i].find("div",{"class":"panel-heading"}).text.strip()+z[j].text.strip()]=z[j]["href"].strip().replace(" ","%20")
                                            else:
                                                new_link=college_url+"/"+z[j]["href"].strip().replace(" ","%20")
                                                subsection_ref_links[sub_internal_link+":"+y[i].find("div",{"class":"panel-heading"}).text.strip()+z[j].text.strip()]=new_link
                                                sub_internal_url_func(new_link)
                                        else:
                                            if(".pdf" in z[j]["href"] or ".jpg" in z[j]["href"] or ".png" in z[j]["href"] or ".gif" in z[j]["href"]):
                                                if("mrcet.com" not in z[j]["href"] or "http" not in z[j]["href"]):
                                                    doc_links[sub_internal_link+":"+y[i].find("div",{"class":"panel-heading"}).text.strip()+z[j]["href"].strip().replace(" ","%20")]=college_url+"/"+z[j]["href"].strip().replace(" ","%20")
                                                else:
                                                    doc_links[sub_internal_link+":"+y[i].find("div",{"class":"panel-heading"}).text.strip()+z[j]["href"].strip().replace(" ","%20")]=z[j]["href"].strip().replace(" ","%20")
                                            else:
                                                new_link=college_url+"/"+z[j]["href"].strip().replace(" ","%20")
                                                subsection_ref_links[sub_internal_link+":"+y[i].find("div",{"class":"panel-heading"}).text.strip()+z[j]["href"].strip().replace(" ","%20")]=new_link
                                                sub_internal_url_func(new_link)
                                
        else:
            rex=section_required.findAll('div',attrs={"class":"container"})
            if(len(rex)!=0):
                z=rex[0].findAll("a")
                for i in z:
                    if(i.text.strip()!=""):  
                        if(".pdf" in i["href"] or ".jpg" in i["href"] or ".png" in i["href"] or ".gif" in i["href"]):
                            if("mrcet.com" not in i["href"] or "http" not in i["href"]):
                                doc_links[sub_internal_link+":"+i.text.strip()]=college_url+"/"+i["href"].strip().replace(" ","%20")
                            else:
                                doc_links[sub_internal_link+":"+i.text.strip()]=i["href"].strip().replace(" ","%20")
                        else:
                            new_link=college_url+"/"+i["href"].strip().replace(" ","%20")
                            subsection_ref_links[sub_internal_link+":"+z[j].text.strip()]=new_link
                            sub_internal_url_func(new_link)
                    else:
                        if(".pdf" in i["href"] or ".jpg" in i["href"] or ".png" in i["href"] or ".gif" in i["href"]):
                            if("mrcet.com" not in i["href"] or "http" not in i["href"]):
                                doc_links[sub_internal_link+":"+i["href"].strip().replace(" ","%20")]=college_url+"/"+i["href"].strip().replace(" ","%20")
                            else:
                                doc_links[sub_internal_link+":"+i["href"].strip().replace(" ","%20")]=i["href"].strip().replace(" ","%20")
                        else:
                            new_link=college_url+"/"+i["href"].strip().replace(" ","%20")
                            subsection_ref_links[sub_internal_link+":"+i["href"].strip().replace(" ","%20")]=new_link
                            sub_internal_url_func(new_link)
                    
            else:
                print("All links in this web page:")
                for i in section_required.findAll("a"):
                    if(i.text.strip()!=""):  
                        if(".pdf" in i["href"] or ".jpg" in i["href"] or ".png" in i["href"] or ".gif" in i["href"]):
                            if("mrcet.com" not in i["href"] or "http" not in i["href"]):
                                doc_links[sub_internal_link+":"+i.text.strip()]=college_url+"/"+i["href"].strip().replace(" ","%20")
                            else:
                                doc_links[sub_internal_link+":"+i.text.strip()]=i["href"].strip().replace(" ","%20")
                        else:
                            new_link=college_url+"/"+i["href"].strip().replace(" ","%20")
                            subsection_ref_links[sub_internal_link+":"+i.text.strip()]=new_link
                            sub_internal_url_func(new_link)
                    else:
                        if(".pdf" in i["href"] or ".jpg" in i["href"] or ".png" in i["href"] or ".gif" in i["href"]):
                            if("mrcet.com" not in i["href"] or "http" not in i["href"]):
                                doc_links[sub_internal_link+":"+i["href"].strip().replace(" ","%20")]=college_url+"/"+i["href"].strip().replace(" ","%20")
                            else:
                                doc_links[sub_internal_link+":"+i["href"].strip().replace(" ","%20")]=i["href"].strip().replace(" ","%20")
                        else:
                            new_link=college_url+"/"+i["href"].strip().replace(" ","%20")
                            subsection_ref_links[sub_internal_link+":"+i["href"].strip().replace(" ","%20")]=new_link
                            sub_internal_url_func(new_link)
    



for i in section_ref_links.values():
    if(i not in section_dict.values() and "mrceterp" not in i):
        print(i)
        try:
            sub_internal_url_func(i)
        except:
            continue
for i in list(doc_links.items()):
    print(i)
