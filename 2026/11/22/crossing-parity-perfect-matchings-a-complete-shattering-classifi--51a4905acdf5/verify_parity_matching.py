"""Finite verification of parity-restricted perfect matching shattering.
No external dependencies. Python 3.9+.
"""
from functools import lru_cache
from itertools import combinations
from math import factorial

@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    a=vertices[0]
    return tuple(((a,b),)+rest for j,b in enumerate(vertices[1:],1)
                 for rest in matchings(vertices[1:j]+vertices[j+1:]))

def crossing(e,f):
    a,b=e; c,d=f
    return (a<c<b<d) or (c<a<d<b)

def parity(M):
    return (-1)**sum(crossing(e,f) for e,f in combinations(M,2))

def top_count(n):
    def odd_double_factorial(j):
        x=1
        for k in range(1,j+1,2): x*=k
        return x
    return sum((2*n-2*r-1)*odd_double_factorial(2*r-1)*odd_double_factorial(2*(n-r-1)-1)
               for r in range(n))

def expected(S,n,sgn):
    s=len(S)
    if s<=n-2: return True
    if s>=n: return False
    used={x for e in S for x in e}
    rem=tuple(x for x in range(2*n) if x not in used)
    if len(rem)!=2:return False
    M=tuple(S)+(rem,)
    return parity(M)==sgn and not any(crossing(rem,e) for e in S)

checks=0
for n in range(2,6):
    MM=matchings(tuple(range(2*n)))
    bysign={s:[] for s in (-1,1)}
    for M in MM: bysign[parity(M)].append(M)
    totals={s:[0]*n for s in (-1,1)}
    supports=set(S for M in MM for s in range(n+1)
                    for S in combinations(M,s))
    for S in supports:
        s=len(S)
        if s==n:continue
        need=(1<<s)-1
        fset=set(S)
        for sign in (1,-1):
            traces=0
            for M in bysign[sign]:
                mset=set(M)
                bits=sum((1<<i) for i,e in enumerate(S) if e in mset)
                traces|=1<<bits
            shattered=(traces==(1<<(1<<s))-1)
            assert shattered==expected(S,n,sign),(n,sign,S,shattered)
            totals[sign][s]+=shattered
            checks+=1
    for s in (1,-1):
        assert totals[s][n-1]==(top_count(n)+s*n*n)//2
        for j in range(n-1):
            assert totals[s][j]==factorial(2*n)//(factorial(2*n-2*j)*2**j*factorial(j))
    print('n',n,'signed_matchings',len(bysign[1]),len(bysign[-1]),
          'faces+',totals[1],'faces-',totals[-1],'signed_top_gap',n*n)

# All labelled forbidden matching subsets on six vertices;
# check two crossing parities of avoiders, supplying the induction base.
V=tuple(range(6)); full=matchings(V)
forbidden_cases=0
for F in {frozenset(E) for M in full for j in range(4) for E in combinations(M,j)}:
    p={parity(M) for M in full if not any(e in F for e in M)}
    assert p=={1,-1},F
    forbidden_cases+=1
print('PASS',checks,'direct support/sign comparisons',forbidden_cases,'six-vertex forbidden matching cases')
