#!/usr/bin/env python3
"""Independent literal two-update testing of all confined chip configurations."""
import itertools
import json
from collections import Counter
from math import comb


def graph(a,b):
    n=a+b
    adjacency=[tuple(j for j in range(n) if j!=i and (i<a or j<a)) for i in range(n)]
    return adjacency


def step(x,edges,degrees):
    flags=[int(t>=d) for t,d in zip(x,degrees)]
    return tuple(x[i]+sum(flags[j] for j in edges[i])-degrees[i]*flags[i]
                 for i in range(len(x)))


def direct(a,b):
    edges=graph(a,b)
    degrees=tuple(map(len,edges))
    hist=Counter()
    seen=0
    for state in itertools.product(*(range(2*d) for d in degrees)):
        seen+=1
        after=step(state,edges,degrees)
        if after != state and step(after,edges,degrees) == state:
            hist[sum(state)]+=1
    return hist,seen


def from_phases(a,b):
    edges=graph(a,b)
    n=a+b
    degrees=tuple(map(len,edges))
    hist=Counter()
    for phases in itertools.product((0,1),repeat=n):
        intervals=[]
        for i in range(n):
            d=degrees[i]
            q=sum(1 for j in edges[i] if phases[j]==0)
            if phases[i]==0:
                left,right=d,2*d-q-1
            else:
                left,right=d-q,d-1
            if left>right:
                break
            intervals.append(range(left,right+1))
        else:
            for state in itertools.product(*intervals):
                hist[sum(state)]+=1
    return hist


def main():
    pairs=[(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),
           (4,1),(4,2)]
    total=0
    summaries={}
    for a,b in pairs:
        actual,n=direct(a,b)
        predicted=from_phases(a,b)
        assert actual==predicted, (a,b,'coefficient mismatch')
        total+=n
        summaries[f'{a},{b}']={'tested_states':n,'primitive_two_states':sum(actual.values()),
                              'support':[min(actual),max(actual)]}
    print(json.dumps({'status':'PASS','tested_graph_pairs':len(pairs),
                      'literal_states_checked':total,
                      'comparison':'actual two-step evolution versus independent phase-interval enumeration',
                      'samples':summaries},sort_keys=True))


if __name__=='__main__':main()
