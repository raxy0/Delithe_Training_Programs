#https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
def implement_queue_with_two_stacks(queries):
    stack1 = []  # First stack
    stack2 = []  # Second stack
    output = []

    for query in queries:
        if query[0] == 1:
            # Enqueue the element into stack1
            stack1.append(query[1])
        elif query[0] == 2:
            # Dequeue the front element
            if not stack2:
                # Transfer all elements from stack1 to stack2 (reversing the order)
                while stack1:
                    stack2.append(stack1.pop())
            if stack2:
                stack2.pop()
        elif query[0] == 3:
            # Print the front element
            if not stack2:
                # Transfer all elements from stack1 to stack2 (reversing the order)
                while stack1:
                    stack2.append(stack1.pop())
            if stack2:
                output.append(stack2[-1])

    return output

def parse_input_string(input_string):
    input_list = input_string.strip().split('\n')[1:]
    queries = []
    for item in input_list:
        query = tuple(map(int, item.split()))
        queries.append(query)
    return queries

# Sample Input
input_string = "10\n1 42\n2\n1 14\n3\n1 28\n3\n1 60\n1 78\n2\n2\n"

# Parse the input string and get the queries
queries = parse_input_string(input_string)

# Output for the sample input
output = implement_queue_with_two_stacks(queries)
for item in output:
    print(item)
