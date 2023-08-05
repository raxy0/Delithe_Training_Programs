#https://www.hackerrank.com/challenges/queue-using-two-stacks/problem


q = int(input())  # Read the number of test cases (q)

qa = []  # Initialize an empty list to represent the queue

# Loop through each test case
for q0 in range(q):
    li = [int(i) for i in input().strip().split()]  # Read the input query as a list of integers

    # The first element of the input query (li[0]) represents the query type
    if li[0] == 1:
        qa.append(li[1])  # Enqueue the element (li[1]) at the end of the queue (qa)
    elif li[0] == 2:
        del qa[0]  # Dequeue the front element by deleting the element at index 0 of the queue (qa)
    else:
        print(qa[0])  # Print the front element (first element) of the queue (qa)
