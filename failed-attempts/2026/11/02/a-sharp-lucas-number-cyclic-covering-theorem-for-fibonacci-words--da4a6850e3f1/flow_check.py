#!/usr/bin/env python3
"""Independent finite minimum-cost circulation checks (requires networkx >=3.0).

Each admissible n-word edge is mandatory. Every additional traversed n-word
has cost one, whether admissible or not. Network simplex independently solves
this relaxation on the unrestricted binary de Bruijn graph.
"""
import networkx as nx

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def check(n):
    vcount=1<<(n-1)
    mask=vcount-1
    imbalance=[0]*vcount
    mandatory=0
    for w in range(1<<n):
        if '00' in format(w,f'0{n}b'):continue
        src=w>>1;dst=w&mask
        imbalance[src]+=1;imbalance[dst]-=1
        mandatory+=1
    graph=nx.DiGraph()
    graph.add_nodes_from((v,{'demand':imbalance[v]}) for v in range(vcount))
    for w in range(1<<n):
        graph.add_edge(w>>1,w&mask,weight=1,capacity=10**6)
    min_extra,_=nx.network_simplex(graph)
    assert mandatory==fib(n+2)
    assert min_extra==fib(n)-1
    print(f'{n},{mandatory},{min_extra},{mandatory+min_extra}')

if __name__=='__main__':
    print('n,mandatory,min_extra,optimal_length')
    for n in range(2,13):check(n)
    print('FLOW_VERIFY_OK')
