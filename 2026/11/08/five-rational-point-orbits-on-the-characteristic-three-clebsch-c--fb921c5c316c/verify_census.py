"""Independent exhaustive census of all GF(9)-rational points and their lines.
Unlike verify_orbits.py, this starts from every quadruple and constructs lines
from unordered point pairs, without using line prototypes or orbit representatives.
"""
from collections import Counter
from itertools import combinations, permutations, product
Q=range(9)
def ad(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
def mi(x,y):return ((x%3)*(y%3)-(x//3)*(y//3))%3+3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
def pw(x,n):
    y=1
    for _ in range(n):y=mi(y,x)
    return y
def normalize(v):
    y=pw(next(a for a in v if a!=0),7)
    return tuple(mi(a,y) for a in v)
def on(v):
    if any(v):
        if (sum(x%3 for x in v)%3 or sum(x//3 for x in v)%3):return False
        val=0
        for i,j,k in combinations(range(5),3):val=ad(val,mi(mi(v[i],v[j]),v[k]))
        return val==0
    return False
P={normalize((a,b,c,d,ad(ad(ad(0,mi(2,a)),mi(2,b)),ad(mi(2,c),mi(2,d)))))
   for a,b,c,d in product(Q,repeat=4) if on((a,b,c,d,ad(ad(ad(0,mi(2,a)),mi(2,b)),ad(mi(2,c),mi(2,d)))))}
assert len(P)==145
lines=set()
for u,v in combinations(sorted(P),2):
    L=frozenset({normalize(tuple(ad(x,mi(t,y)) for x,y in zip(u,v))) for t in Q}|{v})
    if len(L)==10 and L.issubset(P):lines.add(L)
assert len(lines)==27
profile=Counter(sum(p in L for L in lines) for p in P)
assert profile=={1:30,2:105,3:10}
unused=set(P); sizes=[]
while unused:
    p=min(unused)
    O={normalize(tuple(p[i] for i in g)) for g in permutations(range(5))}
    assert O<=unused
    unused-=O
    sizes.append((len(O),next(iter({sum(p in L for L in lines) for p in O}))))
assert sorted(sizes)==[(10,3),(15,2),(30,1),(30,2),(60,2)]
print('EXHAUSTIVE_GF9_CENSUS_OK: 145 points, 27 lines, all 5 projective S5 orbits')
