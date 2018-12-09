

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math 


df=pd.read_csv('https://raw.githubusercontent.com/vidoolytech/hiringtask/master/machine_learning/ad_org/data/mn/ad_org_train.csv')



dur=[]
for a in df.duration:
    dur.append(a[2:])


dur_sec=[]
for t in dur:
    h=t.find('H')
    m=t.find('M')
    s=t.find('S')
    sec=0
    if h>=0:
        sec=sec+int(t[:h])*60*60
        if m>=0:
            sec=sec+int(t[h+1:m])*60
            if s>=0:
                sec=sec+int(t[m+1:s])
    elif m>=0:
        sec=sec+int(t[:m])*60
        if s>=0:
            sec=sec+int(t[m+1:s])
    else:
        sec=sec+int(t[:s])
    dur_sec.append(sec)


df['dur_sec']=dur_sec


df.head()


df_new=pd.get_dummies(df,columns=['category'])



df_new.head()


del df_new['duration']



del df_new['published']

del df_new['vidid']



df_new.head()

x=df_new.iloc[:,1:]
y=df_new.iloc[:,0]

x=x[x.views!='F']

x=x[x.likes!='F']


x=x[x.dislikes!='F']


x=x[x.comment!='F']

x.views=pd.to_numeric(x.iloc[:,0])
x.likes=pd.to_numeric(x.iloc[:,1])
x.dislikes=pd.to_numeric(x.iloc[:,2])
x.comment=pd.to_numeric(x.iloc[:,3])


from sklearn.linear_model import LinearRegression

reg=LinearRegression()

reg.fit(x,y[x.index])


reg.coef_

reg.intercept_

reg.score(x,y[x.index])
###0.002997376099930671

df_1=pd.read_csv('https://raw.githubusercontent.com/vidoolytech/hiringtask/master/machine_learning/ad_org/data/mn/ad_org_test.csv')


dur=[]
for a in df_1.duration:
    dur.append(a[2:])


dur_sec=[]
for t in dur:
    h=t.find('H')
    m=t.find('M')
    s=t.find('S')
    sec=0
    if h>=0:
        sec=sec+int(t[:h])*60*60
        if m>=0:
            sec=sec+int(t[h+1:m])*60
            if s>=0:
                sec=sec+int(t[m+1:s])
    elif m>=0:
        sec=sec+int(t[:m])*60
        if s>=0:
            sec=sec+int(t[m+1:s])
    else:
        sec=sec+int(t[:s])
    dur_sec.append(sec)



df_1['dur_sec']=dur_sec

df_1.head()
df_1.head()



df_new_1=pd.get_dummies(df_1,columns=['category'])

df_new.head()

del df_new_1['duration']

del df_new_1['published']

del df_new_1['vidid']

df_new_1.head()
x_1 = df_new_1
x_1=x_1[x_1.views!='F']
x_1=x_1[x_1.likes!='F']
x_1=x_1[x_1.dislikes!='F']
x_1=x_1[x_1.comment!='F']

x_1.views=pd.to_numeric(x_1.iloc[:,1])
x_1.likes=pd.to_numeric(x_1.iloc[:,2])
x_1.dislikes=pd.to_numeric(x_1.iloc[:,3])
x_1.comment=pd.to_numeric(x_1.iloc[:,4])
y_1 = reg.predict(x_1)
Y_predict=[]
for i in range(len(y_1)):
    if (y_1[i] >=0):
        Y_predict.append(y_1[i])
    else:
        Y_predict.append(0)