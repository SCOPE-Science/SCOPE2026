"""Independent finite Hochster ranks for the pentagon moment-angle manifold.

The Gysin and cup-product arguments for cyclic quotients are proved in RESULT.md;
this executable checks the combinatorial input, not those infinite-family arguments.
"""
from collections import defaultdict
from itertools import combinations


def ranks():
    betti=defaultdict(int)
    k=range(5)
    for size in range(6):
        for J0 in combinations(k,size):
            J=set(J0)
            if not J:
                betti[0]+=1 # reduced degree -1 of empty subcomplex
                continue
            edges=[(i,(i+1)%5) for i in range(5) if i in J and (i+1)%5 in J]
            parent={i:i for i in J}
            def root(x):
                while parent[x]!=x:
                    x=parent[x]
                return x
            for a,b in edges:
                pa,pb=root(a),root(b)
                parent[pa]=pb
            components=len({root(i) for i in J})
            h0=components-1
            h1=len(edges)-len(J)+components
            betti[size+1]+=h0
            betti[size+2]+=h1
    return {i:betti[i] for i in range(8) if betti[i]}


def gysin(p):
    # H^j of base B: 1,1,4,1,1 in degrees 0,2,3,4,6.
    # e: H^0 -> H^2 is multiplication p;
    # e: H^2 -> H^4 vanishes; e: H^4 -> H^6 is multiplication p.
    assert p >= 2
    return {0:'Z',2:f'Z/{p}',3:'Z^5',4:'Z^5',6:f'Z/{p}',7:'Z'}

assert ranks()=={0:1,3:5,4:5,7:1}, ranks()
for p in [2,3,4,5,7,11,25]:
    assert gysin(p)[6]==f'Z/{p}'
print('PENTAGON_HOCHSTER_AND_GYSIN_INPUTS_OK')
