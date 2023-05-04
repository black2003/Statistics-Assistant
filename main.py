import pandas as pd
import os
import engin
import getfl
import histlog
import loginlog
import intro
me = pd.DataFrame()
loginlog.logreg(me)
intro.welcom()
addr = histlog.histlogrew(me)
print("Now enter the path where the output shall be stored-----------------")
aerd = getfl.get_file()
df =pd.read_csv(addr)
fe = 1
while(fe == 1):
    intro.choi()
    ea = int(input("Your Answer :"))
    if(ea == 1):
        engin.heatmp(df, aerd)
    elif(ea == 2):
        print(df.head())
        rxs = input("Enter the parameter name as it is on the datasheet (x axis) (0 if no) :")
        rys = input("Enter the parameter name as it is on the datasheet (y axis) :")
        engin.line(df,rxs,rys, aerd)
    elif(ea == 3):
        engin.datdes(df, aerd)
    elif(ea == 4):
        engin.prepro(df, aerd)
    elif(ea == 5):
        print(df.head())
        rxs = input("Enter the parameter name as it is on the datasheet (x axis) (0 if no) :")
        rys = input("Enter the parameter name as it is on the datasheet (y axis) :")
        engin.boxplt(df,rxs,rys, aerd)
    elif(ea == 6):
        print(df.head())
        rxs = input("Enter the parameter name as it is on the datasheet (x axis) (0 if no) :")
        rys = input("Enter the parameter name as it is on the datasheet (y axis) :")
        engin.vileplt(df,rxs,rys, aerd)
    elif(ea == 7):
        print("exiting.....")
        fe=0
histlog.histstor(me, aerd)
print("Thank you for using Analyzing assistant software ^ U ^!!rty")