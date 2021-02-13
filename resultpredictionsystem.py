'''------------------------GUI--------------------------------'''
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from tkinter import *

root=Tk()

varr=DoubleVar()
varr1=DoubleVar()

root.geometry("720x400")

def click():   
       mid1=(varr.get())
       mid2=(varr1.get())
       final=(str(ma))
       
       labelResult.config(text=mid1)
       labelResul.config(text=mid2)
       labelRes.config(text=final)
       
l1=Label(root,text="STUDENT MARKS PREDICTION SYSTEM", font="helvetica 12").grid(row=0,columnspan=4,pady=40,padx=200)

l2=Label(root,text="MID 1 AVG MARKS BETWEEN 1 TO 20").grid(row=2,column=0)
scale1=Scale(root,from_=0,to=20,activebackground="red",bd=5,variable=varr).grid(row=2,column=1)

l3=Label(root,text="MID 2 AVG MARKS BETWEEN 1 TO 20").grid(row=2,column=2)
scale2=Scale(root,from_=0,to=20,activebackground="green",bd=5,variable=varr1).grid(row=2,column=3)

b1=Button(root,text="PREDICT FINAL SCORE",command=click).grid(row=3,columnspan=4,pady=30,padx=15)

l4=Label(root,text="Your Mid sem 1 marks is:-").grid(row=4,column=1)

labelResult = Label(root)
labelResult.grid(row=4, column=2)  

l5=Label(root,text="Your Mid sem 2 marks is:-").grid(row=5,column=1)

labelResul = Label(root)
labelResul.grid(row=5, column=2)

l6=Label(root,text="As our prediction your Final score is:-").grid(row=6,column=1)

labelRes = Label(root)
labelRes.grid(row=6, column=2)

root.mainloop()

'''----------------------PYTHON CODE-------------------'''

data= {'mid1': [20,20,19,18,17,17,16,15,15,14,14,13,13,12,12,11,11,10,10,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0,0,0,0],
                'mid2': [20,19,20,19,18,16,17,16,17,15,16,13,14,11,13,11,12,11,9,10,11,9,8,8,9,8,6,6,7,5,4,2,3,2,1,0,4,5,2,1,0],
                'final': ['9.8','9.7','9.7','9.5','9.3','9','9','8.8','8.7','8.2','8.4','7.8','8','7.2','7.5','6.9','7.1','6.8','6.7','6.7','6.8','6.5','6','5.7','5.9','5.6','5.2','5','5.2','4.8','4.6','4','3.7','3.3','2.8','2','2','2.3','1.5','1','0']
                }
df=pd.DataFrame(data,columns=['mid1','mid2','final'])

X =df[['mid1','mid2']]
Y = df['final']

reger=LogisticRegression()
reger.fit(X,Y)

aa=[[(varr.get()),(varr1.get())]]
ma=reger.predict(aa)
print(ma)



