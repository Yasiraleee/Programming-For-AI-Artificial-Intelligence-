from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
ok=pd.read_csv("cars.csv")
Y=ok["CO2"]
X=ok[["Weight","Volume"]]

regr=linear_model.LinearRegression()
regr.fit(X,Y)
predict=regr.predict([[2300,1300]])
print(predict)