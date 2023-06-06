list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = zip(list1, list2)
for i in list1:
    for j in list2:
        print(i + j, ",", end=" ")

print(list3)
