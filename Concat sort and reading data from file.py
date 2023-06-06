import pandas as pd
d={'cities':['lahore','karachi'],'provinces': ['punjab','sindh']}
d2={'cities': ['isalambad','karachi','peshawar','quetta'],'provinces':['capital','sindh','KPK','balochistan']}
f1=pd.DataFrame(d)
f2=pd.DataFrame(d2)
f3=pd.concat([f1, f2])
f3=f3.drop_duplicates()
f3=f3.sort_values(by=['provinces'])
f3=f3.reset_index(drop=True)
print(f3)