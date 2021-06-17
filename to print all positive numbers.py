list1=[]
n=int(input('enter the number:'))
for i in range(0,n):
    elm=int(input())
    i=i+1
    list1.append(elm)
print('input:list1=',list1)
print("output:"),
for i in range(0,n):
    if list1[i]>0:
      print(list1[i],end=" ")
