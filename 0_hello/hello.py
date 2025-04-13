import datetime

def main():
    name = input("Please enter your name: ")
    today = datetime.date.today().strftime('%Y-%m-%d')
    print(f"Hi my name is {name}, todays date is {today}")

if __name__ == "__main__":
    main()