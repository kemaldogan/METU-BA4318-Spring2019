print("hello, you will be asked to enter input coordinates") 
input_number=int(input("First, please decide how many number you want to enter"))
a=0
our_list= []
while a<input_number:
    x=float(input("enter x coordinate of input"))
    y=float(input("enter y coordinate of input"))
    our_list.append((x,y))
    a=a+1
print("your list is:",our_list)
##########################
sumx=0
for i in range(0,len(our_list)):
    a=our_list[i]
    sumx=a[0]+sumx
    avgx= sumx/len(our_list)
sumy=0
for i in range(0,len(our_list)):
    b=our_list[i]
    sumy= b[1]+sumy
    avgy=sumy/len(our_list)
    CoM=(avgx,avgy)
print("center of mass for given coordinates is",CoM)
##########################
list_dist=[]
for k in range(0,len(our_list)):
    a=our_list[k]
    from scipy.spatial import distance
    dst = distance.euclidean(a, CoM)
    list_dist.append(dst)
print("distance between each coordinate and center of mass respectly is:",list_dist)
#########################
a=min(list_dist)
k=list_dist.index(a)
print("the point",our_list[k],"has min distance to center of mass and this distance is",a)
b=max(list_dist)
t=list_dist.index(b)
print("the point",our_list[t],"has max distance to center of mass and this distance is",b)
