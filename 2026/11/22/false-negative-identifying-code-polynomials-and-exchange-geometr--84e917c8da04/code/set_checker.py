"""Independent literal-set verifier for one-false-negative identifying codes.
Only Python's standard library is used.  All 2^16 labelled detector choices are tested.
"""
from itertools import combinations
from collections import Counter

def build(variant):
    V = set(range(16))
    S = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    adjacency={x:set() for x in V}
    for a in V:
        for b in V:
            if a==b: continue
            r,c=divmod(a,4); t,u=divmod(b,4)
            if variant=='rook': edge=(r==t or c==u)
            else: edge=(((t-r)%4,(u-c)%4) in S)
            if edge:adjacency[a].add(b)
    return adjacency

def run(variant):
    adj=build(variant)
    U=set(range(16))
    closed={i:(adj[i]|{i}) for i in U}
    for i in U:
        assert len(adj[i])==6
        for j in U-{i}:
            assert (j in adj[i]) == (i in adj[j])
            assert len(adj[i]&adj[j])==2
    pairs=[(closed[i]-closed[j],closed[j]-closed[i])
           for i in range(16) for j in range(i+1,16)]
    counts=Counter(); optimal=[]
    for omitted_n in range(17):
        for Otuple in combinations(range(16),omitted_n):
            C=U-set(Otuple)
            if any(len(C&closed[v])<2 for v in U):continue
            if any(len(C&A)<2 and len(C&B)<2 for A,B in pairs):continue
            counts[len(C)]+=1
            if len(C)==10:optimal.append(frozenset(C))
    assert sum(counts.values()) == (4833 if variant=='rook' else 3769)
    assert min(counts)==10
    print(variant, 'counts',sorted(counts.items()), 'total',sum(counts.values()))
    print(variant, 'optimal',len(optimal))
    return adj,optimal

if __name__=='__main__':
    run('rook');run('shrikhande')
