def main():
    n = int(input())
    temp = n
    n2 = 0

    while temp != 0:
        rem = temp % 10
        n2 = n2 * 10 + rem
        temp //= 10

    if n2 == n:
        print("palindrome number")
    else:
        print("not Palindrome number")


if __name__ == "__main__":
    main()
