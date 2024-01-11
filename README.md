# My Little Pony Data Science Project

## Part 1: Overall Analysis of My Little Pony Transcript Dataset

### Dataset
The dataset for this analysis can be found [here](https://www.kaggle.com/liury123/my-little-pony-transcript).

### Instructions
Calculate the percentage of lines spoken by the top 5 most frequent speakers (ponies) over the entire dataset, including all characters.

## Part 2: Word Counts and TF-IDF Analysis for Each Pony

### Instructions
Create a Python script, `compile_word_counts.py`, that computes word counts for each pony from all episodes of My Little Pony. The script should have the following functionality:

- Run as follows:
  ```bash
  python compile_word_counts.py -o <word_counts_json> -d <clean_dialog.csv file>
  ```

- Words occurring less than 5 times across all valid speech acts should be excluded.
- Remove stopwords using the list provided [here](https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt).
- Consider only speech acts where the speaker is an exact match for one of the main character ponies.
- Treat each word as case-insensitive.
- Replace punctuation characters with a space.
- Exclude words that do not include alphabetic characters.
- Store word counts in dictionaries.

Create another script, `compute_pony_lang.py`, which runs as follows:
  ```bash
  python compute_pony_lang.py -c <pony_counts.json> -n <num_words>
  ```
  The script should output, in JSON format to stdout, the top `<num_words>` words with the highest TF-IDF score for each pony.

## Part 3: Network Modeling of My Little Pony Conversations

### Task 1: Build the MLP Interaction Network

#### Script
Create a Python script, `build_interaction_network.py`, that works as follows:
```bash
python build_interaction_network.py -i /path/to/<script_input.csv> -o /path/to/<interaction_network.json>
```

#### Instructions
- Model the interaction network as who speaks to whom.
- Define an edge between two characters whenever character Y has a line immediately after character X in an episode.
- The weight of the edge is the number of times they speak to each other.
- Exclude characters with specific words in their names: "others," "ponies," "and," "all."
- Ensure a character cannot talk to itself.
- Respect episode boundaries.
- Output should be in JSON format.

### Task 2: Compute Interaction Network Statistics

#### Script
Create a Python script, `compute_network_stats.py`, that runs as follows:
```bash
python compute_network_stats.py -i /path/to/<interaction_network.json> -o /path/to/<stats.json>
```

#### Instructions
Using the networkx library, compute the following statistics:
- Top three most connected characters by degree centrality.
- Top three most connected characters by weighted degree centrality.
- Top three most connected characters by closeness centrality.
- Top three most central characters by betweenness centrality.
