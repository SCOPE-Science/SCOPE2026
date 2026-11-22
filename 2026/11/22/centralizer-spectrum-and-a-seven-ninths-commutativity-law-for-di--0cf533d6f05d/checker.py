#!/usr/bin/env python3
"""Independent finite transformation verification for directed-star Hecke-Kiselman monoids."""
from itertools import product
from math import comb

def comp(x, y):
    return tuple(x[y[i]] for i in range(3))
I=(0,1,2)
a=(0,0,2)
c=(0,1,1)
ac=comp(a,c)
ca=comp(c,a)
T=[I,a,c,ac,ca]
assert len(set(T))==5
assert comp(a,a)==a and comp(c,c)==c
assert comp(comp(a,c),a)==ac and comp(comp(c,a),c)==ac
mult=[[T.index(comp(u,v)) for v in T] for u in T]
assert set(mult[3])=={3}  # ac is absorbing in K2

def model(n):
    rows=[]
    for word in product((0,1),repeat=n):
        rows.append(tuple(word))
    for word in product((2,3,4),repeat=n):
        rows.append(tuple(word))
    return rows
for n in range(1,6):
    elems=model(n)
    lookup={x:i for i,x in enumerate(elems)}
    assert len(lookup)==2**n+3**n
    comm=[]
    for x in elems:
        for y in elems:
            xy=tuple(mult[u][v] for u,v in zip(x,y))
            yx=tuple(mult[v][u] for u,v in zip(x,y))
            assert xy in lookup and yx in lookup
            if xy==yx:
                comm.append(x)
    num=len(comm)
    want=7**n+3*4**n
    assert num==want,(n,num,want)
    for x in elems:
        csize=sum(all(mult[u][v]==mult[v][u] for u,v in zip(x,y)) for y in elems)
        if all(u in (0,1) for u in x):
            predicted=2**n+3**(n-x.count(1))
        else:
            s=x.count(3)
            predicted=2**s+(2**(n-s))*(3**s)
        assert csize==predicted,(n,x,csize,predicted)
    print('n=%d size=%d ordered_commuting=%d central=%d OK' % (n,len(elems),num,sum(all(all(mult[u][v]==mult[v][u] for u,v in zip(x,y)) for y in elems) for x in elems)))
