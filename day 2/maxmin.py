def main():
    n = int(input())
    print("")

    count = 1
    min_val = int(input())
    max_val = min_val

    for i in range(1, n):
        num = int(input())
        min_val = min(min_val, num)
        max_val = max(max_val, num)

    print("min and max are", min_val, "and", max_val)


if __name__ == "__main__":
    main()
