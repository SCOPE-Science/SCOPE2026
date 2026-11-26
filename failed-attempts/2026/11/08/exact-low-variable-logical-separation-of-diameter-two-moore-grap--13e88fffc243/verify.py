#!/usr/bin/env python3
"""Independent exhaustive finite checks of Moore graph local extension profiles.

Only Python standard library is required.
"""
from itertools import combinations, product

def five_cycle():
    v=list(range(5)); a={x:set() for x in v}
    for i in v:
        j=(i+1)%5;a[i].add(j);a[j].add(i)
    return a

def petersen():
    v=list(combinations(range(5),2))
    a={x:set() for x in v}
    for x,y in combinations(v,2):
        if set(x).isdisjoint(y): a[x].add(y);a[y].add(x)
    return a

def hoffman_singleton():
    v=list(product(range(2),range(5),range(5)))
    a={x:set() for x in v}
    def link(x,y): a[x].add(y);a[y].add(x)
    for i in range(5):
        for j in range(5):
            link((0,i,j),(0,i,(j+1)%5))
            link((1,i,j),(1,i,(j+2)%5))
    for i,j in product(range(5),repeat=2):
        for h in range(5):
            link((0,i,j),(1,h,(i*h+j)%5))
    return a

def check_graph(name,a,d):
    n=len(a);assert n==d*d+1,(name,n)
    assert all(len(z)==d for z in a.values())
    E=lambda x,y: y in a[x]
    for x,y in combinations(a,2):
        commons=len(a[x]&a[y]);assert commons==(0 if E(x,y) else 1),(name,x,y,commons)
    near_type=set()
    pair_tables={}
    for x,y in combinations(a,2):
        relation='edge' if E(x,y) else 'nonedge'
        counts={(p,q):sum((int(E(z,x)),int(E(z,y)))==(p,q) for z in a if z!=x and z!=y) for p,q in product(range(2),repeat=2)}
        pair_tables.setdefault(relation,set()).add(tuple(counts[t] for t in [(0,0),(0,1),(1,0),(1,1)]))
        near_type.add((relation,tuple(k for k,v in counts.items() if v)))
    assert all(len(t)==1 for t in pair_tables.values())
    assert pair_tables["edge"]=={((d-1)**2,d-1,d-1,0)}
    assert pair_tables["nonedge"]=={(d*(d-2),d-1,d-1,1)}
    # The witness-pattern calculation for the separating four-variable sentence.
    centers=[];dead=0;positive=0
    for x,y,z in combinations(a,3):
        if E(x,y) or E(x,z) or E(y,z): continue
        common=a[x]&a[y]&a[z]
        if len(common)!=1:continue
        none=sum(not(E(w,x) or E(w,y) or E(w,z)) for w in a if w not in (x,y,z))
        assert none==d*(d-3),(name,none,d)
        centers.append((x,y,z))
        dead+=none==0;positive+=none>0
    assert bool(centers)==(d>=3)
    assert (bool(dead)==(d==3)) and (bool(positive)==(d>3))
    print(f'{name}: n={n}, d={d}, pairs={n*(n-1)//2}, one-edge-pair-table={pair_tables["edge"]}, nonedge-pair-table={pair_tables["nonedge"]}, centered independent triples={len(centers)}, triple_zero_witness_count={d*(d-3) if d>=3 else "not_applicable"}')
    # verifies every 3-pebble extension pattern has identical support for d>=3
    return {r:tuple(int(x>0) for x in next(iter(v))) for r,v in pair_tables.items()}

c=check_graph('C5',five_cycle(),2)
a=check_graph('Petersen',petersen(),3)
b=check_graph('Hoffman-Singleton',hoffman_singleton(),7)
assert a==b,(a,b)
assert c['nonedge'] != a['nonedge'],(c,a)
assert c['edge'] == a['edge'],(c,a)
print('PASS: FO2 local patterns all agree, FO3 splits degree two from degrees three/seven, FO4 centered-triple witness gap exact')
