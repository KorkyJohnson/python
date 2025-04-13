def main():

    lines = [
            "This is line 1\n",
            "This is line 2\n",
            "This is line 3\n"
            ]
    with open("data.txt", "w") as fileWrite:
        for line in lines:
            fileWrite.write(line)

    with open("data.txt", "r") as fileRead:
        lineCount = 0
        for line in fileRead:
            lineCount += 1
            print(f"{lineCount}) {line.rstrip().upper()}")
        print(f"There are {lineCount} lines in this file")

if __name__ == "__main__":
    main()