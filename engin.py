def heatmp(kx,add):
    import seaborn as sb
    import matplotlib.pyplot as plt
    import pandas as pd
    rms = add + "/"+"output(heatmap).png"
    plt.figure(figsize=(len(kx.columns),len(kx.columns)))
    sb.heatmap(kx.corr(),annot=True,linewidth=3,cmap='Blues')
    plt.savefig(rms)
def line(rx,xe,xq,add):
    import matplotlib.pyplot as plt
    import seaborn as sb
    import pandas as pd
    rms = add + "/"+"output(line).png"
    if (xe != 0):
        sb.lineplot(x=rx[xe],y=rx[xq])
    else:
        sb.lineplot(rx[xq])
    plt.savefig(rms , dpi = 300)
def datdes(kx,add):
    import pandas as pd
    mx = pd.DataFrame()
    mx= round(kx.describe() , 3)
    rms = add + "/"+"output(description).csv"
    mx.to_csv(rms)
def prepro(kx,add):
    import pandas as pd
    import getfl
    print("-----------------------------information about datatypes-----------------------------")
    kx.info()
    print("-------------------------------------------------------------------------------------")
    print("-----------------------------information about null values---------------------------")
    print(kx.isnull().sum())
    print("-------------------------------------------------------------------------------------")
    print("-------------------what do you want to replace null values with?---------------------")
    print("                   1  <-- mode         ")
    print("                   2  <-- median        ")
    print("-------------------------------------------------------------------------------------")
    x = list(kx.columns)
    er = int(input("whats your choice  :"))
    print("do you want to save it original doc or create a new?\n  1 for original  \n 2 for new")
    cr=int(input())
    if(cr == 1):
        if(er == 1):
            for i in x:
                kx[i]=kx[i].fillna(kx[i].mode())
                kx.to_csv(add)
        elif(er == 2):
            for i in x:
                kx[i]=kx[i].fillna(kx[i].median())
                kx.to_csv(add)
        else:
            print("wrong input!")
    elif(cr == 2):
        mrt = pd.DataFrame()
        ret = input("what do you want to rename the file(without extension)? :")
        if(er == 1):
            for i in x:
                mrt[i]=kx[i].fillna(kx[i].mode())
                mrt.to_csv(add+"/"+ret+".csv")
        elif(er == 2):
            for i in x:
                mrt[i]=kx[i].fillna(kx[i].median())
                mrt.to_csv(add+"/"+ret+".csv")
        else:
            print("wrong input!")
    else:
        print("wrong input!")
    print("-----------------------------information about null values---------------------------")
    if(cr == 1):
        print(kx.isnull().sum())
    else:
        print(mrt.isnull().sum())
    print("------------------------------------------------------------------------------------ ")
def boxplt(rx,xe,xq,add):
    import matplotlib.pyplot as plt
    import seaborn as sb
    import pandas as pd
    rms = add + "/"+"output(boxplot).png"
    if (xe != 0):
        sb.boxplot(x=rx[xe],y=rx[xq])
    else:
        sb.boxplot(rx[xq])
    plt.savefig(rms, dpi=300)
def vileplt(rx,xe,xq,add):
    rms = add + "/"+"output(violinplot).png"
    import matplotlib.pyplot as plt
    import seaborn as sb
    import pandas as pd
    if (xe != 0):
        sb.violinplot(x=rx[xe],y=rx[xq])
    else:
        sb.violinplot(rx[xq])
    plt.savefig(rms, dpi =300)


    

   






