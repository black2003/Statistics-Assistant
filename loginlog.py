def logreg(rx):
    import pandas as pd
    import os
    import intro
    fwx =1
    while(fwx == 1):
        intro.logi()
        ea = int(input("Your Answer :"))
        if(ea == 2):
            user = input("enter your username :")
        
            f = 1
            while (f == 1):
                passwd = input("enter your password :")
                passwdconf = input("confirm your password :")
                if(passwdconf == passwd):
                    f = 0
                else:
                    print("confirm not matched please re enter")
            r = os.getcwd()
            mr = r + "/" + "accounts" + "/" + user + ".csv"
            df = pd.DataFrame()
            df["user"]= [user]
            df["password"]= [passwd]
            df["ID"]=[0]
            df["Path"]=[0]
            df.to_csv(mr)
            print("please do login now!")
        elif(ea == 1):
            datax = pd.DataFrame()
            user = input("enter your username :")
            r = os.getcwd()
            mr = r + "/" + "accounts"+ "/" + user +".csv"
            if (os.path.isfile(mr)==True):
                msr =r + "/" + "accounts" + "/" + user + ".csv"
                f = 1
                while (f == 1):
                    passwd = input("enter your password :")
                    df = pd.read_csv(mr)
                    df.head()
                    for i in df['password']:
                        if (i == passwd):
                            fwx=0
                            f=0
                            rx["user"] = df["user"]
                            rx["password"] = df["password"]
                            rx["ID"] = df["ID"]
                            rx["Path"] = df["Path"]
                        else:
                            print("Wrong password!")
                            f=0
            else:
                print("user name not found")    
        else:
            print("wrong input please try again!")

