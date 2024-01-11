import argparse
import json
import math
import pandas as pd

def tf_idf(w, pony, data):
    return tf(w, pony, data) * idf(w, data)

def tf(w, pony, data) -> int:
    return data.get(pony, {}).get(w, 0)

def idf(w, data):
    count = sum(1 for pony in data.keys() if w in data[pony])
    if count == 0:
        return float('inf')
    return math.log(len(data.keys()) / count)

def compute_pony_lang(pony_counts, num_words):
    tfidf = {}
    
    with open(pony_counts, 'r') as file:
        data = json.load(file)

    for pony in data:
        words_tfidf = {}
        for word in data[pony]:
            score = tf_idf(word, pony, data)
            words_tfidf[word] = score

        # Sort by TF-IDF scores in descending order
        sorted_words_tfidf = dict(sorted(words_tfidf.items(), key=lambda item: item[1], reverse=True))
        
        # Select the top N words
        top_words = {word: sorted_words_tfidf[word] for word in list(sorted_words_tfidf.keys())[:num_words]}
        tfidf[pony] = top_words

    return tfidf

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--pony_counts", help="path to pony_counts json file", required=True)
    parser.add_argument("-n", "--num_words", help="number of words to output for each pony", required=True, type=int)
    args = parser.parse_args()

    result = compute_pony_lang(args.pony_counts, args.num_words)
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
