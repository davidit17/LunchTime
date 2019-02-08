# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:52:40 2019

@author: python
"""

import pandas as pd
import os


#os.getcwd()
#os.chdir('C:\\Users\\python\\Documents\\Untitled Folder\\Food Model')

Rest = pd.read_excel('Rest.xlsx',skip_blank_lines=True).dropna()

Rest.IsKosher=Rest.IsKosher.astype(int)
Rest.IsDelivery=Rest.IsDelivery.astype(int)


ans=True
Ko = 1
De = 1
Rating = 0
ResType = -1

def KoStatus():
    if Ko==1 :
        print('Kosher Only')
    else :
        print('Not Only Kosher') 

def DeStatus():
    if De==1 :
        print('Delivery option')
    else :
        print('We can go Out ') 


def ReturnRec(DataFrame,Ko,De,ResType=-1,Rating=0):

    relevant = DataFrame[(DataFrame['IsKosher']>=Ko) &
                         (DataFrame['IsDelivery']>=De)]
    
    if ResType !=-1:
        relevant = relevant[relevant['Type']==TypesDict[ResType]]
    relevant = relevant[relevant['Rating']>Rating]
    
    if relevant.empty:
        print('No Restaurant meets the conditions!')
    else :
        choice = relevant.sample(n=1)
        print("\n todays recommendation is :") 
        print("")
        print(
              ' Restaurant Name : ' + str(choice.ResDesc.get_values()[0]) +"\n",
              'Type : ' + str(choice.Type.get_values()[0]) +"\n",
              'rating : ' + str(choice.Rating.get_values()[0]) +"\n",
              'Price : ' + str(choice.Price.get_values()[0]) +"\n",
              'Distance : ' + str(choice.Distance.get_values()[0]) +"\n"
                  ) 
        
        print("""
              ___ ___  ______ __   __  ______  ______  
             |_  |_  ||____  |\ \ / / |  __  ||____  | 
               | | | |     | ||  V /  | |  | |     | | 
               | | | |_____| || |\ \ _| |  | |_____| |_
               | | |_/________/_| \_\___|  |_/________/
               |_|                                     

              """)
    
    
        
        
def GoodBye():
    print("""
          
 .d8888b.                         888 888                       
d88P  Y88b                        888 888                       
888    888                        888 888                       
888         .d88b.   .d88b.   .d88888 88888b.  888  888  .d88b. 
888  88888 d88""88b d88""88b d88" 888 888 "88b 888  888 d8P  Y8b
888    888 888  888 888  888 888  888 888  888 888  888 88888888
Y88b  d88P Y88..88P Y88..88P Y88b 888 888 d88P Y88b 888 Y8b.    
 "Y8888P88  "Y88P"   "Y88P"   "Y88888 88888P"   "Y88888  "Y8888 
                                                    888         
                                               Y8b d88P         
                                                "Y88P"          

    """)
        


def PrintMe():
    print("""

.   .                                                  
|   |,---..    ,    ,---.,---.,-.-.,---.,---.,---.,   .
|   ||   | \  /     |    |   || | ||   |,---||   ||   |
`---'`   '  `'      `---'`---'` ' '|---'`---^`   '`---|
                                   |              `---'
                                   
,---.                         |         
|---',---.,---.,---.,---.,---.|--- ,---.
|    |    |---'`---.|---'|   ||    `---.
`    `    `---'`---'`---'`   '`---'`---'                                  


d88888b  .d88b.   .d88b.  d8888b.   .88b  d88.  .d88b.  d8888b. d88888b db     
88'     .8P  Y8. .8P  Y8. 88  `8D   88'YbdP`88 .8P  Y8. 88  `8D 88'     88     
88ooo   88    88 88    88 88   88   88  88  88 88    88 88   88 88ooooo 88     
88~~~   88    88 88    88 88   88   88  88  88 88    88 88   88 88~~~~~ 88     
88      `8b  d8' `8b  d8' 88  .8D   88  88  88 `8b  d8' 88  .8D 88.     88booo.
YP       `Y88P'   `Y88P'  Y8888D'   YP  YP  YP  `Y88P'  Y8888D' Y88888P Y88888P

      """)
    print('*'*10)
    print("""
          Properties                         
          """) 
    print('*'*10)
    KoStatus()
    DeStatus()
    if Rating !=0:
        print('Rating Above : ' +str(Rating))
        
    if ResType !=-1:
        print('Restaurant Type : ' +str(TypesDict[ResType]))    
    print('*'*10)

while ans:
    PrintMe()
    print ("""
    1.Change Kosher
    2.Change Delivery
    3.Set Rating Filter
    #.
    #.
    6.Set Type Filter
    7.Show Restaurants List
    8.Get Recommendation
    9.Exit/Quit
    """)
    
    ans=input("please choose action")
    if ans=="1": 
        Ko*=-1
        os.system('cls||clear')
        
    elif ans=="2":
        De*=-1
        os.system('cls||clear')   
        
    elif ans=="3":
        Rating = int(input('enter Rating filter'))
        os.system('cls||clear')
      
    elif ans=="6":
        os.system('cls||clear')
        TypesDict = pd.Series(pd.Series(Rest.Type.unique()).
                              sort_values(ascending=True).values).to_dict() 
        TypesDict.update( {-1:'No Filter' } )            
        for key,value in TypesDict.items():
            print(key, ':', value) 
        ResType = int(input('enter Type Number '))
        os.system('cls||clear')
        
    elif ans=="7":
        os.system('cls||clear')
        print(Rest.iloc[:,1:8].to_string())
        input('Press Any Key To Continue') 
        os.system('cls||clear')
        [print(rest) for rest in Rest.ResDesc.sort_values(ascending=True).values]
        input('Press Any Key To Return') 
        os.system('cls||clear')
        
    elif ans=="8": 
        os.system('cls||clear')
        PrintMe()
        ReturnRec(Rest,Ko,De,ResType,Rating)
        input('Press Any Key') 
        os.system('cls||clear')
        
    elif ans=="9":
        GoodBye()
        ans=False
        
    elif ans !="":
        print("\n Not Valid Choice Try again") 

input('Press ENTER to exit')