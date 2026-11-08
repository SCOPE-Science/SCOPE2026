"""Exact projective S5 orbit and 27-line-incidence certificate over GF(9).
GF(9) is represented by a+bi, with i*i=-1 and a,b in GF(3).
Only Python's standard library is used.
"""
from itertools import combinations, permutations

def add(x,y): return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
def neg(x): return (-x%3)+3*((-(x//3))%3)
def mul(x,y):
    a,b=x%3,x//3
    c,d=y%3,y//3
    return (a*c-b*d)%3+3*((a*d+b*c)%3)
def power(x,n):
    r=1
    for _ in range(n): r=mul(r,x)
    return r
def projective(v):
    first=next(x for x in v if x)
    unit=power(first,7)
    return tuple(mul(x,unit) for x in v)
def sigma3(v):
    a=0
    for i,j,k in combinations(range(5),3):
        a=add(a,mul(mul(v[i],v[j]),v[k]))
    return a
def surface(v):
    t=0
    for x in v:t=add(t,x)
    return t==0 and sigma3(v)==0
G=list(permutations(range(5)))
def act(g,v):return projective(tuple(v[k] for k in g))
def span(u,v):
    return frozenset({projective(tuple(add(x,mul(t,y)) for x,y in zip(u,v))) for t in range(9)}|{projective(v)})
def orbit_line(L):
    return {frozenset(act(g,p) for p in L) for g in G}
# 15 lines through the coordinate-pair construction and their 12 complements.
A=span((1,2,0,0,0),(0,0,1,2,0))
B=span((0,1,2,4,8),(1,0,4,2,8))
LA,LB=orbit_line(A),orbit_line(B)
assert len(A)==len(B)==10
assert len(LA)==15 and len(LB)==12 and LA.isdisjoint(LB)
assert all(surface(p) for L in LA|LB for p in L)
reps=[
 ((0,0,0,1,2),10,12,3,0,'S3xC2'),
 ((0,1,1,2,2),15,8,2,0,'D8'),
 ((0,1,2,3,6),30,4,1,0,'C4'),
 ((1,1,3,3,4),30,4,0,2,'C2xC2'),
 ((0,1,2,4,8),60,2,1,1,'C2'),
]
seen=set()
for p,size,stab,na,nb,name in reps:
    assert surface(p)
    O={act(g,p) for g in G}
    assert len(O)==size and 120//size==stab
    assert not (O&seen)
    seen |= O
    assert sum(p in L for L in LA)==na
    assert sum(p in L for L in LB)==nb
    assert all(sum(t in L for L in LA)==na and sum(t in L for L in LB)==nb for t in O)
assert len(seen)==145
assert sum(len(L) for L in LA|LB)==270
print('ORBIT_AND_LINE_CERTIFICATE_OK: orbit sizes 10,15,30,30,60; line orbits 15+12')
