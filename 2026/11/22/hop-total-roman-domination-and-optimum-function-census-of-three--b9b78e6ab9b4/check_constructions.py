"""Directly check representative optimal configurations against the graph definition."""
from itertools import combinations

def valid(n,two,one):
    vertices=list(map(frozenset,combinations(range(n),3)))
    d=set(map(frozenset,two)); o=set(map(frozenset,one))
    assert not (d&o)
    positive=d|o
    for u in vertices:
        if u not in positive:
            if not any(u!=v and (u&v) for v in d):return False
        else:
            if not any(u!=v and not (u&v) for v in positive):return False
    return True
for n in range(8,21):
    r,s=divmod(n,3)
    if s==0:
        two=[tuple(range(3*j,3*j+3)) for j in range(r-1)]
        one=[tuple(range(n-3,n))]
    else:
        two=[tuple(range(3*j,3*j+3)) for j in range(r)]
        one=[]
    assert valid(n,two,one)
    if s==1:
        # Two defender triples share ground point zero; exactly two other points are unused.
        two=[(0,1,2),(0,3,4)]+[tuple(range(5+3*j,8+3*j)) for j in range(r-2)]
        assert valid(n,two,[])
    print(n,'constructive_OK')
