"""Independently regenerate the graph and enumerate minimum LD codes for q<=6.
Also test an eight-sensor q=7 witness without using bitmasks. Python 3, stdlib.
"""
from itertools import combinations

def graph(q):
    words=[(a,b) for a in range(q) for b in range(q) if a!=b]
    adjacent={u:frozenset(v for v in words if u!=v and (u[1]==v[0] or u[0]==v[1])) for u in words}
    return words,adjacent

def is_ld(chosen,words,adjacent):
    chosen=frozenset(chosen)
    signatures=[adjacent[u]&chosen for u in words if u not in chosen]
    return all(signatures) and len(signatures)==len(set(signatures))

for q,k,expected in [(2,1,2),(3,3,20),(4,4,168),(5,5,84),(6,7,11040)]:
    words,adjacent=graph(q)
    assert not any(is_ld(S,words,adjacent) for S in combinations(words,k-1))
    count=sum(is_ld(S,words,adjacent) for S in combinations(words,k))
    assert count==expected,(q,count,expected)
words,adjacent=graph(7)
witness=[(0,4),(0,5),(1,2),(1,3),(2,1),(3,1),(4,0),(5,0)]
assert is_ld(witness,words,adjacent)
print('ALTERNATE_OK')
