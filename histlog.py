def histlogrew(rx):
    import pandas as pd
    import getfl as wee
    f=1
    while (f == 1):
        for i in rx['ID']:
                print("would you like to restore your previous worked analysis file? (Y/N)")
                a = input()
                f=1
                while(f==1):
                    if(a == 'Y'):
                        rx.head()
                        f2 = 1
                        while(f2 == 1):
                            aid = int(input("Please enter a valid save ID"))
                            for k in rx['ID']:
                                if(aid == k):
                                    f2=0
                                    aer=df.loc[rx['ID'] == aid]
                                    add = aer['Path']
                                    return add
                                    f=0
                                elif(aid == 0):
                                    f2=0
                                    f=0
                                    break
                            else:
                                print("No such ID exists")
                    elif(a == 'N'):
                        print("Enter the directory location where your file to be analyzed is")
                        add = wee.get_file()
                        ems=input("enter the file name with extension 'csv' :")
                        add = add + "/"+ems
                        return add
                        f=0
                    else:
                        print("please enter a valid input")
def histstor(rx,add):
     import os
     import pandas as pd
     f=1
     r = os.getcwd()
     user = rx.loc[0]['user']
     mr = r + "/" + "accounts"+ "/" + user +".csv"
     df = pd.read_csv(mr)
     while(f == 1):
        de = input("Would you like to save the current file? (Y/N) :")
        if(de == 'Y'):
            for i in rx['ID']:
                if(i == 0):
                    df = df[df['ID'] != 0]
                    re = len(df.index)
                    re = re+1
                    df2 = {'ID':re , 'Path':add}
                    df3 = pd.Series(df2)
                    df = pd.concat([df,df3],axis=0)
                    print("saved..!")
                else:
                    re = len(df.index)
                    re = re+1
                    df2 = {'ID':re ,'Path':add}
                    df3 = pd.Series(df2)
                    df = pd.concat([df,df3],axis=0)
                    print("saved..!")
            f=0
        elif(de == 'N'):
            print("ok work not saved!")
            f=0
        else:
            print("wrong input!")
        




                                
                                

                 

