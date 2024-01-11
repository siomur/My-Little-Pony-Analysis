import argparse
import json
from pathlib import Path
import pandas as pd
import requests

ponies = ["twilight sparkle", "applejack", "rarity", "pinkie pie", "rainbow dash", "fluttershy"]

def create_directories_if_not_exist(path):
    directory = Path(path).parent
    directory.mkdir(parents=True, exist_ok=True)

def fetch_stopwords():
    # take the stopwords listed here
    url = "https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt"
    response = requests.get(url)
    if response.status_code == 200:
        stopwords = response.text.split("\n")

    return stopwords

def pony_and_words(input_file):
    pony_word_count = {}
    
    data = pd.read_csv(input_file, header=0, encoding='ISO-8859-1')
    data = data[['pony', 'dialog']]

    stopwords = fetch_stopwords()

    for index, row in data.iterrows():
        # Check for NaN values in 'dialog' column
        if pd.notna(row['dialog']):
            words = row['dialog'].split()
            pony = row['pony'].lower()

            if pony in pony_word_count and ponies:
                for word in words:
                    word = word.lower()
                    word = ''.join(filter(str.isalpha, word))
                    if word not in stopwords:
                        if word in pony_word_count[pony]:
                            pony_word_count[pony][word] += 1
                        else:
                            pony_word_count[pony][word] = 1
            else:
                if pony not in ponies: 
                    continue

                pony_word_count[pony] = {}
                for word in words:
                    word = word.lower()
                    word = ''.join(filter(str.isalpha, word))
                    if word not in stopwords:
                            pony_word_count[pony][word] = 1

    return pony_word_count


def more_than_five(word_dict):
    result = {}
    for pony in word_dict:
        result[pony] = {}
        for word in word_dict[pony]:
            if word_dict[pony][word] >= 5:
                result[pony][word] = word_dict[pony][word] 

    return result 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_file", help="json file to output to", required=True)
    parser.add_argument("-d", "--input_file", help="path to your input file, should be csv", required=True)
    args = parser.parse_args()
    create_directories_if_not_exist(args.output_file)


    with open(args.output_file, "w") as f:
        result = pony_and_words(args.input_file)
        data = more_than_five(result)
        json.dump(data, f, indent=2)
    

if __name__ == "__main__":
    main()
