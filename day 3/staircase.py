def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        spaces = n - i
        hashtags = i
        line = " " * spaces + "#" * hashtags
        print(line)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)