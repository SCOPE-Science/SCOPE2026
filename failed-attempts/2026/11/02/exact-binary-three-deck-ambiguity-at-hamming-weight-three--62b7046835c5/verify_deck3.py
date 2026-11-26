from itertools import combinations
from collections import defaultdict
from math import comb

def deck(w):
    r=[0]*8
    for i,j,k in combinations(range(len(w)),3):
        r[(w[i]<<2)|(w[j]<<1)|w[k]]+=1
    return tuple(r)

def fromgap(g):
    a,b,c,d=g
    return (0,)*a+(1,)+(0,)*b+(1,)+(0,)*c+(1,)+(0,)*d

def partner(g):
    a,b,c,d=g
    if (c-b)%3:return None
    t=(c-b)//3
    if not t:return None
    gp=(a-t,c,b,d+t)
    return gp if min(gp)>=0 else None

def pairs_formula(n):
    m=n-3
    return sum(m-4*t-2*b+1 for t in range(1,m//4+1) for b in range((m-4*t)//2+1))
for n in range(3,17):
    cells=defaultdict(list)
    for p in combinations(range(n),3):
        w=tuple(int(i in p) for i in range(n))
        g=(p[0],p[1]-p[0]-1,p[2]-p[1]-1,n-p[2]-1)
        cells[deck(w)].append(g)
    sizes=[len(c) for c in cells.values()]
    assert max(sizes)<=2
    for c in cells.values():
        if len(c)==2:
            assert partner(c[0])==c[1] and partner(c[1])==c[0],(n,c)
        else:
            assert partner(c[0]) is None,(n,c)
    p=sum(s==2 for s in sizes)
    assert p==pairs_formula(n),(n,p,pairs_formula(n))
    assert len(cells)==comb(n,3)-p
    print(n,comb(n,3),p,len(cells),max(sizes))
print('PASS: complete exhaustive weight-3 deck classes, n=3..16, partner and enumerator match')
