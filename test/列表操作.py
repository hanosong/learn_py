list1 = [13,3243,353,1123,22,3342,431]
#冒泡排序算法
for i,val in enumerate(list1):
    for j in range(i+1,len(list1)):
        # 开始冒泡
        if list1[i] > list1[j]: # 如果当前元素大于下一个元素，则交换，i表示当前元素，j表示下一个元素
            list1[i],list1[j] = list1[j],list1[i] # 交换两个元素，将当前元素和下一个元素交换
print(list1)









