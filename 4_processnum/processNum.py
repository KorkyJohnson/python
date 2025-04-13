def main():

    numberList = []

    with open("numbers.txt") as numberRead:
        for num in numberRead:
            try:
                num = float(num.rstrip())
                numberList.append(num)
            except ValueError:
                print(f'value "{num.rstrip()}" is not a valid number. Skipping')

    print(f'The numbers are:  {numberList}')
    print("The max number is ", max(numberList))
    print("The min number is ", min(numberList))
    print("The sum of numbers is ", sum(numberList))
    print("The count of numbers is ", len(numberList))
    print("The avg number is ", round(sum(numberList) / len(numberList),2))

if __name__ == "__main__":
    main()