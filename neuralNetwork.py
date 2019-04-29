
# coding: utf-8

# In[ ]:


import pandas as pd

mySlovnik = {}
badChars = [".","?",",","!"]

def mailFit(x_mail):
    cleanSlova = []
    
    for m in x_mail:
        m_clean = multiReplace(m, badChars, "")
        slova = m_clean.split(" ")
        for slovo in slova:
            cleanSlova.append(slovo)
            
    for i in range(len(cleanSlova)):
        s = cleanSlova[i]
        if s not in mySlovnik: #prehodenie slov na int pre spracovanie ..  ahoj = 1
            mySlovnik[s] = len(mySlovnik)
    x_vector = [] #tu sa ulozi vector repre. x_mail
    
    for m in x_mail:
        m_clean = multiReplace(m, badChars, "")
        slova = m_clean.split(" ")
        
        temp = []
        
        for slovo in slova:
            newS = mySlovnik[slovo]
            temp.append(newS)
        
        x_vector.append(temp)
        
    return x_vector

def hamFit(y_ham):
    y_vector = []
    
    for h in y_ham:
        if h == "ham":
            y_vector.append(0)
        if h == "spam":
            y_vector.append(1)
            
    return y_vector
    


def mutliReplace(slovo, listWordov, nahrada):
    for ch in listWordov:
        if ch in slovo:
            slovo = slovo.replace(ch, nahrada)
    return slovo
        
dataExcel = pd.read_csv("spam.csv", sep = ",")
x_mail = dataExcel['v2']
y_ham = dataExcel['v1']


