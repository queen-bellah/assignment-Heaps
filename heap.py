import heapq



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


print(data)
heapq.heappop(data)
print(data)