import csv

def main():
    with open("data.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['name']} is {row['age']} years old and codes in {row['language']}.")
        
if __name__ == "__main__":
    main()