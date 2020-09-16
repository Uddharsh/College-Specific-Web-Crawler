#importing URL LIBRARY, Beautiful Soup and Regular Expression Checker
import urllib.request
from bs4 import BeautifulSoup
import re
from os import system
import webbrowser
import sys
import html
college_url="https://www.mrcet.com"
college_page=urllib.request.urlopen(college_url)
soup = BeautifulSoup(college_page, "lxml")
college_html=soup.prettify()
internal_ref_links=[]
def header_initial_selection(header_soup):
    header_links=[]
    for i in header_soup:
        header_links.append(i.findAll("a"))
    print("All the header links of the college's web page are displayed below:")
    for i in range(0,len(header_links[0])):
        if(i!=3 and i!=4):
            x=header_links[0][i]["href"]
            if(header_links[0][i].text!=''):
                if(".html" not in x):
                    print(i,"-",header_links[0][i].text,":",x)
                else:
                    print(i,"-",header_links[0][i].text,":",college_url+"/"+x)
            else:
                print(i,"-",x)
        else:
            if(i==3):
                print(i,"-","Contact Number:",header_links[0][i].text)
            else:
                print(i,"-","Email Id: mrcet2004@gmail.com")
#Departments
def main_link_selection(navigation_header_soup):
    print("main_link_selection()")
    count=0
    print("The main links of the college's website are displayed below:")
    navigation_header_dict={}
    navigation_header_links=navigation_header_soup[0].ul.findAll(recursive=False)
    for i in range(len(navigation_header_links)):
        navigation_header_links[i]=navigation_header_links[i].findAll('a')
    for i in range(len(navigation_header_links)):
            print(i+1,"-",navigation_header_links[i][0].text.strip())
    choice=int(input("Enter the corresponding number to which hyperlink you want to navigate further through:"))
    print("Sub links in "+navigation_header_links[choice-1][0].text.strip()+":")
    if(len(navigation_header_links[choice-1])!=0):
        for i in range(len(navigation_header_links[choice-1])):
                if(navigation_header_links[choice-1][i]["href"]!="#"):
                    x=navigation_header_links[choice-1][i].text.strip()
                    if(navigation_header_links[choice-1][i]["href"]!="#"):
                        print(i,"-",x)
                        count+=1
    sub_choice=int(input("Enter the corresponding number to which sub link you want to navigate further through:"))
    if(count==0):
        print("There aren't any links, you will now be redirected to the sub page")
        webbrowser.open_new_tab(college_url+"/"+navigation_header_links[choice-1][sub_choice]["href"])
        sys.exit(0)
    if(".pdf" in navigation_header_links[choice-1][sub_choice]["href"] or ".jpg" in navigation_header_links[choice-1][sub_choice]["href"] or ".png" in navigation_header_links[choice-1][sub_choice]["href"]or ".gif" in navigation_header_links[choice-1][sub_choice]["href"]):
        if("mrcet.com" not in navigation_header_links[choice-1][sub_choice]["href"]):
            new_link=college_url+"/"+navigation_header_links[choice-1][sub_choice]["href"].replace(" ","%20")
            webbrowser.open_new_tab(new_link)
            sys.exit(0)
        else:
            new_link=navigation_header_links[choice-1][sub_choice]["href"].replace(" ","%20")
            webbrowser.open_new_tab(new_link)
            sys.exit(0)
    else:
        temp=navigation_header_links[choice-1][sub_choice]["href"]
        new_link=college_url+"/"+temp
    return new_link
def sub_link_func(sub_url):
    sub_page=urllib.request.urlopen(sub_url)
    sub_soup = BeautifulSoup(sub_page, "lxml")
    sub_html=sub_soup.prettify()
    section_list=[]
    anchor_list_1=[]
    anchor_dict={}
    count=1
    count1=1
    new_link=""
    section_required=(sub_soup.find('section',{"class":re.compile("padding")}))
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
                            anchor_dict[count1]=anchor_list_1[i][j]
                            if(anchor_list_1[i][j].text.strip()!=""):
                                print(count1,"-",anchor_list_1[i][j].text.strip())
                            else:
                                print(count1,"-",anchor_list_1[i][j]["href"])
                            count1+=1
                count=int(input("Enter corresponding number of the link you would like to navigate further through:"))
                if(".pdf" in anchor_dict[count]["href"] or ".jpg" in anchor_dict[count]["href"] or ".png" in anchor_dict[count]["href"] or ".gif" in anchor_dict[count]["href"]):
                    if("mrcet.com" not in anchor_dict[count]["href"] or "http" not in anchor_dict[count]["href"]):
                        new_link=college_url+"/"+anchor_dict[count]["href"].replace(" ","%20")
                        webbrowser.open_new_tab(new_link)
                        sys.exit(0)
                    else:
                        new_link=anchor_dict[count]["href"].replace(" ","%20")
                        webbrowser.open_new_tab(new_link)
                        sys.exit(0)
                else:
                    new_link=college_url+"/"+anchor_dict[count]["href"]
                if(new_link==""):
                    print("No links found in sub page. Redirecting to sub-link page...")
                    webbrowser.open_new_tab(sub_url)
                    sys.exit(0)
    elif(x.findAll("div",{"class":re.compile("container")})!=None):
        section_list.append(x.findAll("div",{"class":re.compile("container")}))
        if(len(section_list)!=0):
            for i in section_list[0]:
                anchor_list_1.append(i.findAll("a"))
            if(len(anchor_list_1)!=0): 
                for i in range(len(anchor_list_1)):
                    for j in range(len(anchor_list_1[i])):
                        if(len(anchor_list_1[i][j])!=0 and (not anchor_list_1[i][j].has_attr("data-parent")) and (anchor_list_1[i][j] not in anchor_dict.values()) and (anchor_list_1[i][j]["href"]!="#")):
                            anchor_dict[count1]=anchor_list_1[i][j]
                            if(anchor_list_1[i][j].text.strip()!=""):
                                print(count1,"-",anchor_list_1[i][j].text.strip())
                            else:
                                print(count1,"-",anchor_list_1[i][j]["href"])
                            count1+=1
                count=int(input("Enter corresponding number of the link you would like to navigate further through:"))
                if(".pdf" in anchor_dict[count]["href"] or ".jpg" in anchor_dict[count]["href"] or ".png" in anchor_dict[count]["href"] or ".gif" in anchor_dict[count]["href"]):
                    if("mrcet.com" not in anchor_dict[count]["href"]):
                        new_link=college_url+"/"+anchor_dict[count]["href"].replace(" ","%20")
                        webbrowser.open_new_tab(new_link)
                        sys.exit(0)
                    else:
                        new_link=anchor_dict[count]["href"].replace(" ","%20")
                        webbrowser.open_new_tab(new_link)
                        sys.exit(0)
                else:
                    new_link=college_url+"/"+anchor_dict[count]["href"]
                if(new_link==""):
                    print("No links found in sub page. Redirecting to sub-link page...")
                    new_link=sub_url
                    webbrowser.open_new_tab(new_link)
                    sys.exit(0)
    else:
        if(".pdf" in new_link or ".jpg" in new_link or ".png" in new_link or ".gif" in new_link):
            if("mrcet.com" not in anchor_dict[count]["href"] or "http" not in anchor_dict[count]["href"]):
                new_link=college_url+"/"+anchor_dict[count]["href"].replace(" ","%20")
                webbrowser.open_new_tab(new_link)
                sys.exit(0)
            else:
                new_link=anchor_dict[count]["href"].replace(" ","%20")
                webbrowser.open_new_tab(new_link)
                sys.exit(0)
        if(new_link==""):
            print("No links found, redirecting to the current page...")
            webbrowser.open_new_tab(sub_url)
            sys.exit(0)  
    return new_link
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
                                print("Section ",i+1,"-",y[i].find("div",{"class":"panel-heading"}).text.strip().replace(":"," "))
                                z= y[i].findAll("a")
                                count=1
                                for j in range(len(z)):
                                    if(z[j].has_attr("data-parent")):
                                        pass
                                    else:
                                        print(count,"-",z[j].text.strip())
                                        count+=1
                            choice=int(input("Enter the corresponding section number to further navigate through:"))
                            print("You've chosen Section Number ",choice,".")
                            print("The links in the selected section are displayed below:")
                            z=y[choice-1].findAll("a")
                            count=1
                            for j in range(len(z)):
                                if(not z[j].has_attr("data-parent")):
                                    if(z[j].text.strip() not in my_dict.values()):
                                        print(count,"-",z[j].text.strip())
                                        my_dict[count]=z[j].text.strip()
                                        anchor_text[z[j]["href"]]=z[j].text.strip()
                                        anchor_list[count]=z[j]["href"]
                                        print(anchor_list[count])
                                        count+=1
                            choice=int(input("Enter the corresponding link number to further navigate through:"))
                            new_internal_sublink=anchor_list[choice]
                            if(".pdf" in new_internal_sublink or ".jpg" in new_internal_sublink or ".png" in new_internal_sublink or ".gif" in new_internal_sublink):
                                new_link=college_url+"/"+new_internal_sublink.replace(" ","%20")
                                webbrowser.open_new_tab(new_link)
                                sys.exit(0)
                            else:
                                new_link=college_url+"/"+new_internal_sublink
                                sub_internal_url_func(new_link)
                            if(new_link==""):
                                print("No links found in sub page. Redirecting to internal sub page...")
                                new_internal_sublink=sub_internal_page
                                webbrowser.open_new_tab(new_internal_sublink)
                                sys.exit(0)
        else:
            rex=section_required.findAll('div',attrs={"class":"container"})
            if(len(rex)!=0):
                print("All links in this web page:")
                z=rex[0].findAll("a")
                for i in z:
                    if(i.text!=""):
                        if(".pdf" in i["href"] or ".jpg" in i["href"] or ".png" in i["href"] or ".gif" in i["href"]):
                                new_link=college_url+"/"+i["href"].strip().replace(" ","%20")
                                print(i.text+":"+new_link)
                        else:
                            new_link=college_url+"/"+i["href"]
                            sub_internal_url_func(new_link)
                    else:
                        if(".pdf" in i["href"] or ".jpg" in i["href"] or ".png" in i["href"] or ".gif" in i["href"]):
                                new_link=college_url+"/"+i["href"].strip().replace(" ","%20")
                                print(i["href"]+":"+new_link)
                        else:
                            new_link=college_url+"/"+i["href"]
                            sub_internal_url_func(new_link)
                    
            else:
                print("All links in this web page:")
                for i in section_required.findAll("a"):
                    print(i.text.strip())
    
sub_internal_url_func(sub_link_func(main_link_selection(soup.select('nav[class="navbar navbar-inverse"]'))))