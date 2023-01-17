from matplotlib import pyplot as plt
budget_data = [500, 1000, 750, 300, 100]
budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']
plt.pie(budget_data,labels=budget_categories,autopct="%0.1f%%")
plt.legend(budget_categories,loc=5)
plt.show()