import heapq
list=[(1,"sia"),(2,"ria"),(3,"gia")]
heapq.heapify(list)
for i in range(len(list)):
    print(heapq.heappop(list))






l1=[10,20,30,40,50]
l2=[15,25,35,45,55]
l3=heapq.merge(l1, l2)

print(l3)


data = [10,20,43,1,2,65,17,44,2,3,1]
# print(sorted(data))
heapq.heapify(data)
print(data)

# i
# 2*i+1
# 2*i+2
# # (i-1)/2
print(heapq.heappop(data))
print(data)
heapq.heappush(data, 4)
heapq.heappush(data, 19)
heapq.heappush(data, 21)

heapq._heapify_max(data)
print(heapq._heappop_max(data))
print(data)
heapq.heapify