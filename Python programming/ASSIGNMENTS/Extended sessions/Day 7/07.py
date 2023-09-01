l1 = [24,28,52,"christ","university"]
l2 = [1,2,3,4,5,6,7,8]

t= (1,2,3,"Hello",True)
# print(t[3:4])
# print(t[3])

t1 = (t,1,2,3,"Hello")
# print(t1)
#tuples are immutable and only lists are mutable

#list inside a tuple can be accessed or are mutable
t2 = (l1,5,'h')
# print("tuple before: ",t2)
t2[0][1] = 32 #here the list inside the tuple is being changed
# print("tuple after",t2)

# t3 = (l1,l2)
# print(t3)

print("geeta" or "seetha")
print("geeta" and "seetha")