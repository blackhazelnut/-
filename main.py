import nltk
import string
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import numpy as np
import os
from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys
from textblob import TextBlob
from random import randint

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def ExceptionMsg(msg):
    print("Exception occur : " + msg)

def Required(items):
    print(" ")
    print(" ")
    print("-------Execution Start-------")
    for item in items:
        print("Require : " + item + " to be in the same folder")

CurrentDirectory = os.getcwd()

while(1):
    print("-----4D----")
    print("1 Obtain all dates")
    print("2 Obtain all 4D data")

    cmd = input("Please Enter Your Cmd : ")
    
    if cmd=='1': #1 obtain all dates
        Required(["Link.txt","ResultDate.txt"])
        counter=0
        driver = webdriver.Chrome()
        with open(CurrentDirectory + "\\" + "Link.txt") as LinkFile: 
            for link in LinkFile: 
                driver.get(link)
                time.sleep(1)
                with open("ResultDate.txt", "a") as ResultDate:
                    try:
                        while(1):
                            counter+=1
                            temp = driver.find_element_by_css_selector("#ctl00_ctl36_g_06c36ce1_a880_4b71_82e6_ce448fdef295 > div > div.results-filter.row.clearfix > div.form-group.col-md-3.drawListAndLabel > div > select > option:nth-child("+str(counter)+")")
                            #date = temp.text
                            #value = temp.get_attribute("value")
                            result = link+temp.get_attribute("querystring")
                            print(result)
                            ResultDate.write(result)
                            ResultDate.write("\n")
                    except:
                        print("end of 4d date list")

                    
    elif cmd=='2':#
        Required(["ResultDate.txt","Result.txt"])
        driver = webdriver.Chrome()

        with open(CurrentDirectory + "\\" + "ResultDate.txt") as ResultDateFile:
            for link in ResultDateFile: 
                print(link)
                driver.get(link)
                time.sleep(1)
                with open("Result.txt", "a") as Result:
                    try:
                        strResult=""

                        firstprize = driver.find_element_by_css_selector("#ctl00_ctl36_g_06c36ce1_a880_4b71_82e6_ce448fdef295_ctl00_divSingleDraw > div.tables-wrap > table.table.table-striped.orange-header > tbody > tr:nth-child(1) > td").text
                        secondprize = driver.find_element_by_css_selector("#ctl00_ctl36_g_06c36ce1_a880_4b71_82e6_ce448fdef295_ctl00_divSingleDraw > div.tables-wrap > table.table.table-striped.orange-header > tbody > tr:nth-child(2) > td").text
                        thirdprize = driver.find_element_by_css_selector("#ctl00_ctl36_g_06c36ce1_a880_4b71_82e6_ce448fdef295_ctl00_divSingleDraw > div.tables-wrap > table.table.table-striped.orange-header > tbody > tr:nth-child(3) > td").text
                        strResult = firstprize + " " + secondprize + " " + thirdprize
                        print(strResult)
                        for x in range(1,5):
                            for y in range(1,2):
                                starterprize = driver.find_element_by_css_selector("#ctl00_ctl36_g_06c36ce1_a880_4b71_82e6_ce448fdef295_ctl00_divSingleDraw > div.tables-wrap > table:nth-child(2) > tbody > tr:nth-child("+str(x)+") > td:nth-child("+str(y) +")").text
                                strResult+=" " + starterprize

                        for x in range(1,5):
                            for y in range(1,2):
                                consolationprize = driver.find_element_by_css_selector("#ctl00_ctl36_g_06c36ce1_a880_4b71_82e6_ce448fdef295_ctl00_divSingleDraw > div.tables-wrap > table:nth-child(3) > tbody > tr:nth-child("+str(x)+") > td:nth-child("+str(y) +")").text
                                strResult+=" " + consolationprize

                        Result.write(strResult)
                        Result.write("\n")
                            
                    except:
                        print("end of 4d list")

 
    else:
        print("Invalid Command")

