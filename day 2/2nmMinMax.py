def main():
    n = int(input())
    print("")

    count = 1
    min_val = int(input())
    max_val = min_val
    prev_min = min_val
    prev_max = max_val

    for i in range(1, n):
        num = int(input())

        if min_val > num:
            prev_min = min_val
            min_val = num
        if max_val < num:
            prev_max = max_val
            max_val = num

    print("min and max are", prev_max, "and", prev_min)


if __name__ == "__main__":
    main()
