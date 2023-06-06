l1=[["student1","Student2","Student3"],[24,13,75]]

t=list(sorted(filter(lambda x:x,l1[1])))
print(t[len(l1)-1])