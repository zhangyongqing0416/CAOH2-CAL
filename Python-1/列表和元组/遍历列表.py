lst1=["北京","上海","天津"]
#遍历列表，并用竖线分割
for item in lst1:
    print(item,end='|')
print()
print("===遍历索引及对应元素===")
for index,item in enumerate(lst1):
    print(index,item)