"""Reproduce the two-colour strong-majority / efficient domination correspondence.
Requires Python 3 and networkx. All test graphs are simple connected cubic graphs.
"""
from itertools import product
import networkx as nx


def strong_majority_two(G, colors):
    edge_list = [tuple(sorted(e)) for e in G.edges()]
    assigned = dict(zip(edge_list, colors))
    for u, v in edge_list:
        neighbors = [assigned[f] for f in edge_list if f != (u, v) and (u in f or v in f)]
        if len(neighbors) != 4:
            raise ValueError('non-cubic input')
        if neighbors.count(0) != 2 or neighbors.count(1) != 2:
            return False
    return True


def efficient_codes(G):
    vertices=list(G.nodes())
    codes=[]
    for bits in product((0,1),repeat=len(vertices)):
        S={v for v, bit in zip(vertices,bits) if bit}
        if all(len(S.intersection(set(G.neighbors(v)) | {v}))==1 for v in vertices):
            codes.append(S)
    return codes


def check(G, name):
    G=nx.convert_node_labels_to_integers(G)
    if not nx.is_connected(G) or any(deg!=3 for _,deg in G.degree()):
        raise ValueError('input not connected simple cubic graph')
    edges=[tuple(sorted(e)) for e in G.edges()]
    codes=efficient_codes(G)
    theoretical=set()
    for S in codes:
        for special in (0,1):
            col=tuple(special if (u in S or v in S) else 1-special for u,v in edges)
            theoretical.add(col)
    observed={col for col in product((0,1),repeat=len(edges)) if strong_majority_two(G,col)}
    assert observed == theoretical, (name,len(observed),len(theoretical))
    assert len(observed)==2*len(codes)
    print(f'{name}: vertices={len(G)} edges={len(edges)} codes={len(codes)} successful_named_edge_colouring={len(observed)} OK')


def main():
    collection={}
    for i,G in enumerate(nx.graph_atlas_g()):
        if 4<=len(G)<=6 and nx.is_connected(G) and all(d==3 for _,d in G.degree()):
            collection[f'atlas_{i}']=G
    collection.update({
        'cube_Q3':nx.cubical_graph(),
        'circular_ladder_4':nx.circular_ladder_graph(4),
        'petersen':nx.petersen_graph(),
        'circular_ladder_5':nx.circular_ladder_graph(5),
    })
    for n in (8,10):
        for seed in range(6):
            collection[f'random_{n}_{seed}']=nx.random_regular_graph(3,n,seed=seed)
    for name, G in collection.items():
        check(G,name)
    print('VERIFY_OK',len(collection),'graph instances')

if __name__=='__main__':main()
