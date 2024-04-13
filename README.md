# assignment-Heaps


A binary tree is any tree in which a node can have no more than two offspring. A heap is a binary tree that is complete.  

Advantages of Heaps

Effective insertion and deletion: Elements can be inserted and removed with efficiency using the heap data structure.
When a new element is introduced to the heap, the heapify action is used to move it up to the proper location from the bottom of the heap.

Disadvantages of Heaps

Not the best for searching: Although the heap data structure makes it possible to retrieve the top element quickly, it is not the best for looking for a particular element within the heap. 
To find one element in a heap, you have to go through the whole tree.

heappush − This function adds an element to the heap without altering the current heap.
heappop − This function returns the smallest data element from the heap.
heapreplace − This function replaces the smallest data element with a new value supplied in the function.
heapq.nsmallest-This function will return smallest number in the heap.
heapq.nlargest-This function will return largest number in the heap.

