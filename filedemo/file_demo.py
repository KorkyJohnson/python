def main():
    with open("data.txt","w") as fileWrite:
        fileWrite.write("This is line 1\r")
        fileWrite.write("This is line 2\r")
        fileWrite.write("This is line 3\r")
    
    with open("data.txt", "r") as fileRead:
        lineCount = 0
        for line in fileRead:
            print(f"{line}")
            lineCount += 1
        print(f"There are {lineCount} lines in this file")

if __name__ == "__main__":
    main()