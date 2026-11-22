"""Exact zero-temperature single-spin majority absorption law on the icosahedron.
Standard library only. Every bit mask in range(4096) is examined.
"""
from fractions import Fraction
from functools import lru_cache
from collections import Counter
from math import comb

N=12
# Pole and staggered pentagonal rings; indices 1..5 and 6..10.
E=set()
def edge(a,b): E.add(tuple(sorted((a,b))))
for i in range(5):
    a=1+i; b=6+i
    edge(0,a); edge(11,b)
    edge(a,1+(i+1)%5); edge(b,6+(i+1)%5)
    edge(a,b); edge(a,6+(i-1)%5)
assert len(E)==30
NB=[0]*N
for u,v in E:
    NB[u]|=1<<v; NB[v]|=1<<u
assert all(x.bit_count()==5 for x in NB)
FULL=(1<<N)-1

def possible(x):
    return tuple(v for v in range(N)
                 if (((NB[v]&x).bit_count()>=3)!=bool(x&(1<<v))))

def cut(x):
    return sum(bool((x>>u)&1)!=bool((x>>v)&1) for u,v in E)

CAPS={NB[v]|(1<<v) for v in range(N)}
assert len(CAPS)==12 and all(c.bit_count()==6 for c in CAPS)
ABS={x for x in range(1<<N) if not possible(x)}
assert ABS==({0,FULL}|CAPS), (len(ABS),ABS^CAPS)
# Every flip strictly reduces the number of discordant bonds.
assert all(cut(x^(1<<v))<cut(x) for x in range(1<<N) for v in possible(x))

@lru_cache(None)
def h(x):
    mv=possible(x)
    if not mv:
        return Fraction(int(x in CAPS),1)
    return sum((h(x^(1<<v)) for v in mv),Fraction(0,1))/len(mv)

C=[sum((h(x) for x in range(1<<N) if x.bit_count()==k),Fraction(0,1))
   for k in range(N+1)]
assert C==[
    Fraction(0),Fraction(0),Fraction(0),Fraction(2),
    Fraction(742264,23625),Fraction(9896937913,85050000),
    Fraction(7394887513,42525000),Fraction(9896937913,85050000),
    Fraction(742264,23625),Fraction(2),
    Fraction(0),Fraction(0),Fraction(0)]
# Verify polynomial identity in Bernstein basis through integer polynomial operations.
from math import factorial
P=[Fraction(0)]*13
for k,c in enumerate(C):
    for j in range(13-k):
        P[k+j]+=c*(-1)**j*comb(12-k,j)
# Expected q^3(739236313 q^2+1651550400 q+170100000)/85050000
# Expand each q^d=(p(1-p))^d coefficientwise.
Q=[Fraction(0)]*13
for d,num in ((5,739236313),(4,1651550400),(3,170100000)):
    for j in range(d+1):
        Q[d+j]+=Fraction(num*(-1)**j*comb(d,j),85050000)
assert P==Q
v=sum((h(x) for x in range(1<<N)),Fraction(0,1))/4096
assert v==Fraction(10067037913,87091200000)
three=[x for x in range(1<<N) if x.bit_count()==3]
assert Counter(h(x) for x in three)=={Fraction(0):160,Fraction(1,30):60}
# The synchronous majority cap has exactly itself as predecessor.
def sync(x):
    return sum((1<<v for v in range(N) if (NB[v]&x).bit_count()>=3),0)
assert {x for x in range(1<<N) if sync(x)==x}==ABS
assert all([x for x in range(1<<N) if sync(x)==cap]==[cap] for cap in CAPS)
print('PASS first checker: 4096 states, 14 terminal states, 12 caps, complete rational polynomial')
print('Bernoulli one-half probability',v)
print('3-positive-spin success classes:',Counter(h(x) for x in three))
print('synchronous cap predecessors: unique; synchronous cap probability = 12 q^6')
