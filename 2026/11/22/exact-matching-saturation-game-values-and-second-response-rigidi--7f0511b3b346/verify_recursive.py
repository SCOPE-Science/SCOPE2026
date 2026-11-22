#!/usr/bin/env python3
"""Exact matching-saturation games on the five Platonic graphs.
Pure Python, standard library only. Recursive memoization over remaining vertices.
"""
from functools import lru_cache
from collections import Counter
import json

def graphs():
    def gen(n, es):
        return n, sorted(set(tuple(sorted(e)) for e in es))
    tetra = gen(4, ((a,b) for a in range(4) for b in range(a+1,4)))
    cube = gen(8, ((a, a^(1<<j)) for a in range(8) for j in range(3)))
    octa = gen(6, ((a,b) for a in range(6) for b in range(a+1,6)
                    if b != (a+3)%6 and a != (b+3)%6))
    dodeca = gen(20, (((i,(i+1)%10) for i in range(10))))
    dodeca = gen(20,dodeca[1]+[(i,10+i) for i in range(10)]+
                 [(10+i,10+((i+2)%10)) for i in range(10)])
    ico_edges=[]
    for i in range(5):
        a,b=1+i,6+i
        ico_edges.extend([(0,a),(11,b),(a,1+(i+1)%5),
                           (b,6+(i+1)%5),(a,b),(a,6+(i-1)%5)])
    icosa=gen(12,ico_edges)
    return {'tetrahedron':tetra,'cube':cube,'octahedron':octa,
            'dodecahedron':dodeca,'icosahedron':icosa}

def solve(n, edges):
    assert len(edges)==len(set(edges)) and all(0<=u<v<n for u,v in edges)
    full=(1<<n)-1
    @lru_cache(None)
    def game(mask, max_turn):
        vals=[]
        for u,v in edges:
            if (mask>>u)&1 and (mask>>v)&1:
                vals.append(1+game(mask^(1<<u)^(1<<v),not max_turn))
        if not vals:return 0
        return max(vals) if max_turn else min(vals)
    @lru_cache(None)
    def terminal_extreme(mask, maximum):
        vals=[]
        for u,v in edges:
            if (mask>>u)&1 and (mask>>v)&1:
                vals.append(1+terminal_extreme(mask^(1<<u)^(1<<v),maximum))
        if not vals:return 0
        return max(vals) if maximum else min(vals)
    a,b=edges[0]
    def response_hist(first_edge, max_first):
        a,b=first_edge; rem=full^(1<<a)^(1<<b)
        hist=Counter()
        for u,v in edges:
            if (rem>>u)&1 and (rem>>v)&1:
                tail=rem^(1<<u)^(1<<v)
                hist[2+game(tail,max_first)]+=1
        return tuple(sorted(hist.items()))
    hist_max=response_hist(edges[0],True)
    hist_min=response_hist(edges[0],False)
    assert all(response_hist(e,True)==hist_max and response_hist(e,False)==hist_min for e in edges)
    result={'vertices':n,'edges':len(edges),
            'min_maximal':terminal_extreme(full,False),
            'max_matching':terminal_extreme(full,True),
            'max_first':game(full,True),'min_first':game(full,False),
            'maxfirst_second_response_hist':list(map(list,hist_max)),
            'minfirst_second_response_hist':list(map(list,hist_min))}
    return result

def main():
    results={name:solve(*g) for name,g in graphs().items()}
    print(json.dumps(results,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
