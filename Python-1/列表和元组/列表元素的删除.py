lst4=[]
for i in [1,2,3,4,5]:
    lst4.append(i*2+1)
print(lst4)
#删除索引为1的元素
del lst4[1]
print(lst4)
#删除索引为1的元素并返回被输出的元素
item=lst4.pop(1)
print(lst4)
print(item)
#pop不指定位置，默认删除最后一个
lst4.pop()
print(lst4)