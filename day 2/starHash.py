def main():
    s = input()
    count1 = 0
    count2 = 0

    for char in s:
        if char == '*':
            count1 += 1
        else:
            count2 += 1

    if count1 > count2:
        print("positive")
    elif count2 > count1:
        print("Negative")
    else:
        print("Equal")


if __name__ == "__main__":
    main()
