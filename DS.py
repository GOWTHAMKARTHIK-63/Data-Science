import pandas as vs
import matplotlib.pyplot as gkn
gk = vs.read_csv('gender_submission.csv')
print(gk.head(40))
gk.rename(columns= {"PassengerId":"Number"},inplace=True)
print(gk)
filter=gk[gk["Survived"]==1]
print(filter)
Total_Pass = gk["Survived"].value_counts()
total = len(gk)
a = Total_Pass[0]
perc = (a / total) * 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind = 'bar',color = ["blue","Green"])
gkn.xlabel("Survived people")
gkn.ylabel("Non-Survived people")
gkn.title("Survived passenger in the flight")
gkn.xticks(rotation = 0)
gkn.yticks(rotation = 18)
gkn.show()