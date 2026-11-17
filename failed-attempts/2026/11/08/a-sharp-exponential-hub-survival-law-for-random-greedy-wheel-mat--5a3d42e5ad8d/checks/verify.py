#!/usr/bin/env python3
"""Independent finite-state checks and analytic-series checks for wheel greedy matching."""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial

checks=0

def ok(statement,detail):
    global checks
    assert statement,detail
    checks+=1

def model_probability(n, edges, marked):
    # Exact absorbing chain of all unmatched-vertex subsets; no structural recurrence used.
    edges=tuple(tuple(sorted(e)) for e in edges)
    @lru_cache(None)
    def H(mask):
        live=[(u,v) for u,v in edges if (mask>>u)&1 and (mask>>v)&1]
        if not live:
            return Fraction((mask>>marked)&1)
        return sum((H(mask & ~(1<<u) & ~(1<<v)) for u,v in live),Fraction(0))/len(live)
    return H((1<<n)-1)

def wheel(n):
    return n+1,[(i,(i+1)%n) for i in range(n)]+[(i,n) for i in range(n)],n

def fan(k):
    return k+1,[(i,i+1) for i in range(k-1)]+[(i,k) for i in range(k)],k

# Structural candidate p_k derived using the first rim edge, independently cross-check by full graph Markov chains.
a=[Fraction(1)]
for m in range(1,30):
    a.append(sum((a[j]*a[m-1-j] for j in range(m)),Fraction(0))/Fraction(4*m-1))
for k in range(0,17):
    predicted=a[k//2] if k%2==0 else Fraction(0)
    ok(model_probability(*fan(k))==predicted,('fan',k,predicted))
for n in range(3,17):
    predicted=a[n//2-1]/2 if n%2==0 else Fraction(0)
    ok(model_probability(*wheel(n))==predicted,('wheel',n,predicted))

# Totally separate uniform static random-priority enumeration for W4.
N,edges,hub=wheel(4)
success=0
for perm in permutations(range(len(edges))):
    used=0
    for j in perm:
        u,v=edges[j]
        if (used>>u)&1 or (used>>v)&1:continue
        used|=(1<<u)|(1<<v)
    success+=1 if not ((used>>hub)&1) else 0
ok(Fraction(success,factorial(len(edges)))==Fraction(1,6),('permutations',success))

# Entire function u(z)=1 - sum_{n>=1} d_n z^n; d_1=1/4,
# d_{n+1}=d_n/[4(n+1)(4n-1)]. The Riccati identity gives F=-4u'/u.
N=24
d=[Fraction(0)]*(N+1)
d[1]=Fraction(1,4)
for n in range(1,N):d[n+1]=d[n]/Fraction(4*(n+1)*(4*n-1))
u=[Fraction(1)]+[-x for x in d[1:]]
# coefficients of -4u'=F u, to all available degrees
for n in range(N):
    lhs=sum((a[j]*u[n-j] for j in range(n+1)),Fraction(0))
    rhs=-4*(n+1)*u[n+1]
    ok(lhs==rhs,('Riccati',n,lhs,rhs))

# Certified bracket rho in (3.47547,3.47548) using rational finite Taylor series and tail bound.
def U_partial(z, N=16):return 1-sum((d[k]*z**k for k in range(1,N+1)),Fraction(0))
def tail_bound(z,N=16):
    next_term = d[N]*z**N*z/Fraction(4*(N+1)*(4*N-1))
    r=z/Fraction(4*(N+2)*(4*(N+1)-1))
    assert r < 1
    return next_term/(1-r)
lo=Fraction(347547,100000)
hi=Fraction(347548,100000)
ok(U_partial(lo)>tail_bound(lo),('lower root',U_partial(lo)-tail_bound(lo)))
ok(U_partial(hi)<0,('upper root',U_partial(hi)))

print('VERIFY_OK',checks,'assertions','p(W4)=',Fraction(success,factorial(len(edges))), 'p(W6)=',a[2]/2, 'p(W8)=',a[3]/2,'rho in (3.47547,3.47548)')
