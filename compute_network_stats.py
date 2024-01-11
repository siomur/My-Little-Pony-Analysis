import argparse
import networkx as nx
import json

def compute_weighted_degree_centrality(G):
    weighted_degree_centrality = {}
    for node in G.nodes():
        weighted_degree_centrality[node] = 0
        for neighbor in G.neighbors(node):
            weighted_degree_centrality[node] += G[node][neighbor]['weight']
   
    return weighted_degree_centrality

def compute_network_stats(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    G = nx.Graph(data)

    #The top three most connected characters by degree centrality.
    #The top three most connected characters by weighted degree centrality (each edge contributes its weight = # of interactions)
    #The top three most connected characters by closeness centrality.
    #The top three most central characters by betweenness centrality.  

    stats = {}
    
    
    stats['degree'] = [p for p, v in sorted(nx.degree_centrality(G).items(), key=lambda x: x[1],  reverse = True)[:3]]
    stats['weighted_degree'] = [p for p, v in sorted(compute_weighted_degree_centrality(G).items(), key=lambda x:x[1], reverse=True)[:3]]
    stats['closeness'] = [p for p, v in sorted(nx.closeness_centrality(G).items(), key=lambda x:x[1], reverse=True)[:3]]
    stats['betweenness'] = [p for p, v in sorted(nx.betweenness_centrality(G).items(), key = lambda x:x[1], reverse=True)[:3]]
    print(stats)


    with open(output_file, 'w') as f:
        json.dump(stats, f, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help="path to input file", required=True)
    parser.add_argument('-o', '--output', help="path to output file", required=True)
    args = parser.parse_args()
    compute_network_stats(args.input, args.output)


if __name__ == '__main__':
    main()