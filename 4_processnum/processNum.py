def main():

    numberList = []

    with open("numbers.txt") as numberRead:
        for num in numberRead:
            numberList.append(num.rstrip())

    print(f'The numbers are:  {numberList}')

if __name__ == "__main__":
    main()