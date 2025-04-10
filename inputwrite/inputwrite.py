def main():

    maxInput = 3
    count = 0

    inputWrite(maxInput, count)

    inputRead()

def inputWrite(maxInput, count):
    with open ("user_input.txt","w") as inputWrite:
        while count < maxInput:
            text = input(f"Please enter your text ({count+1} of {maxInput}) ")
            inputWrite.write(f'{text}\n')
            count += 1

def inputRead():
    with open ("user_input.txt","r") as inputRead:
        lineCnt = 0
        for line in inputRead:
            lineCnt += 1
            print(f'Line {lineCnt} - {line.rstrip()}\n')

if __name__ == "__main__":
    main()