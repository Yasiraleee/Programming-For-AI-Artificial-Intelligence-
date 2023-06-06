from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]

plt.plot(x_values,y_values,linestyle="--",marker="o",color="Blue")
plt.xlabel("Values of X")
plt.ylabel("Values of Y")
plt.legend(["ok"])
plt.title("oh")
plt.show()