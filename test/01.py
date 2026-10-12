#最外层循环控制行数，最内层循环控制列数
# for i in range(1,10):
#     for j in range(1,i+1): #实际上i最后会执行到9，i+1会执行到10，所以实际上是执行到9
#         print(f"{i}*{j}={i*j}",end="\t")
#     print()
# print("end")


list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list1[:]
isSame = list1 is list2
# print(id(list1),id(list2))
# print(isSame)

# isSame = list1 == list2
# print(isSame)

# print(list1[::-1])
res = list1.insert(1,999)
# print(list1.insert(0,888))
print(list1)
print(res)
