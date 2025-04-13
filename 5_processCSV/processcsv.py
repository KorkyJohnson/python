import csv

def main():

    ages = []        # store ages for avg
    lang_cnt = {}   # store language counts

    with open('people.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            age = int(row["age"])
            language = row["language"]
            ages.append(age)            

            print(f'{name} is {age} years old and codes in {language}')

            match language:
                case "Python":
                    lang_cnt[language] = lang_cnt.get(language, 0) + 1
                case "Java":
                    lang_cnt[language] = lang_cnt.get(language, 0) + 1
                case "Cobol":
                    lang_cnt[language] = lang_cnt.get(language, 0) + 1
                case _:
                    lang_cnt[language] = lang_cnt.get("Unknown Language", 0) + 1

    print('Average age: ', round(sum(ages) / len(ages)))
    # print(lang_cnt)
    for lang, cnt in sorted(lang_cnt.items()):
        print(f'{lang}: {cnt}')

if __name__ == "__main__":
    main()