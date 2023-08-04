def main():
    m, n = map(int, input().split())
    print("Enter the elements")
    max_cars_parked = 0
    max_row_number = 0

    for i in range(m):
        count_cars = 0
        print("Row", i + 1)
        row_elements = list(map(int, input().split()))

        for num in row_elements:
            if num == 1:
                count_cars += 1

        if count_cars > max_cars_parked:
            max_cars_parked = count_cars
            max_row_number = i + 1

    print("The row number", max_row_number, "has most cars parked:", max_cars_parked)


if __name__ == "__main__":
    main()
