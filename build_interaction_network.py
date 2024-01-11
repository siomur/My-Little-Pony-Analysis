import networkx as nx
import json
import argparse
import pandas as pd
from itertools import filterfalse


def build_network(input_file, output_file):
    
     
    #read the data

    data = pd.read_csv(input_file, header=0, encoding='ISO-8859-1')
    data = data[['pony', 'title']]

    prev_speaker = None
    prev_episode = None

    # create the graph
    G = nx.Graph()

    for i in range(len(data)): 
        speaker = data.iloc[i]['pony']
        episode = data.iloc[i]['title']

        if prev_episode == None: # first iteration
            prev_episode = episode
            prev_speaker = speaker
        
        elif episode != prev_episode: # respecting episode boundaries
            prev_episode = episode
            prev_speaker = speaker
        
        elif episode == prev_episode and speaker == prev_speaker: # pony would be talking to itself
            prev_episode = episode
            prev_speaker = speaker

        elif any(x in speaker.lower() for x in ['all', 'others', 'ponies', 'and']) or any(x in prev_speaker.lower() for x in ['all', 'others', 'ponies', 'and']): 
            # pony would be talking to a group, or group talking --which we exclude, so both cases does not count
            prev_episode = episode
            prev_speaker = speaker
            

        elif episode == prev_episode and speaker != prev_speaker: # pony would be talking to another pony
            # check if node exists for previous speaker, if not add node, create edge with speaker (if node exists, if not create node for speaker as well)
            if not G.has_node(speaker):
                G.add_node(speaker)

            if not G.has_node(prev_speaker):
                G.add_node(prev_speaker)
                G.add_edge(speaker, prev_speaker, weight=1)

            else:
                #check if edge exists, if not create edge, if so increment weight
                if not G.has_edge(speaker, prev_speaker):
                    G.add_edge(speaker, prev_speaker, weight=1)
                else:
                    G[speaker][prev_speaker]['weight'] += 1
            
            # iterate
            prev_episode = episode            
            prev_speaker = speaker



    # Convert the graph to a dictionary
    interaction_network = {node: dict(G[node]) for node in G.nodes}

    # Write the interaction network to a JSON file
    with open(output_file, 'w') as f:
        json.dump(interaction_network, f, indent=2)
 
          


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help="path to input file", required=True)
    parser.add_argument('-o', '--output', help="path to output file", required=True)
    args = parser.parse_args()
    build_network(args.input, args.output)

if __name__ == "__main__":
    main()