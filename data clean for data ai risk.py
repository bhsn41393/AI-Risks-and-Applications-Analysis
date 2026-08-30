import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

data=pd.read_csv("halal.csv")
print(data.head(10))


print(data.head(10))
c=0
for i in data["daily_ai_chat_hours"] :
    if i=="khazog":
        continue
    else :
        c+=1

    
print(c)
print(f"num of sofof={c}")
print(data.info())
print(data.describe())
print("#"*20)
print("#"*20)
print(data.head(0))
print(data.describe())
print(data.shape[1])
print(data.columns)
print(len(data.columns))
print(data.isnull)
print(data["daily_ai_chat_hours"])
r=[]
for i in data["daily_ai_chat_hours"]:
    if i not in r:
        r.append(i)
    else :
        continue
print(r)
print(len(r))
print(data.daily_ai_chat_hours.isnull())
print(data["daily_ai_chat_hours"].sum())
hassan=data["daily_ai_chat_hours"]>5.5
print("#"*30)
print(hassan)
print("#"*30)
print(f"pianat alnas aly peyegdo aksar men 6.5 hour in ai ={len(data[hassan])}")
print(data[hassan])
hassan=data["country_region"]=="Asia"
print(data[hassan]["income_level"])
dada=data["daily_ai_chat_hours"]>3
print(data[dada]["country_region"])
fafa=(data["daily_ai_chat_hours"]>3) & (data["country_region"]=="Asia")
print(data[fafa])
data["estekhdam alsoshial media zayed estekhdam al ai al of them"]=data["daily_ai_chat_hours"]+data["social_media_hours_daily"]
print(data["estekhdam alsoshial media zayed estekhdam al ai al of them"])
data["label risk score"]=data["dependency_risk_label"]
c=0
for i in data["label risk score"]:
    if i =="Low":
        data["label risk score"][c]=2
        c+=1
    elif i == "Moderate":
        data["label risk score"][c]=4
        c+=1
    else:
        data["label risk score"][c]=6
        c+=1
print(data["label risk score"])
data["month"]=np.random.randint(1,13,1000)
print(data["month"])
data["year"]=np.random.randint(2000,2002,1000)
print(len(data["year"]))
print(len(data["country_region"]))


print("#"*30)
fig,x1=plt.subplots(1,2)
x1[0].scatter(x=data["self_esteem_score"],y=data["dependency_risk_label"])
plt.show()






        

        





        


