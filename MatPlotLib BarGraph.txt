from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
drinks = ["cappuccino", "latte", "chai", "americano", "mocha",
"espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
sales = [91, 76, 56, 66, 52, 27]
plt.bar(range(len(drinks)),sales)
ax=plt.subplot()
ax.set_xticks(range(6))
ax.set_xticklabels(drinks)
plt.legend("YES")
plt.show()