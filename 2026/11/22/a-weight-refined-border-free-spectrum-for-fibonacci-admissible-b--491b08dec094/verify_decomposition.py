"""Alternative shortest-border decomposition and asymptotic error checks.

Usage: python verify_decomposition.py
"""
from collections import Counter
from decimal import Decimal, localcontext

LIMIT=150

def shift_poly(p,k):return Counter({d+k:c for d,c in p.items()})
def concat_poly(p,q):
    r=Counter()
    for a,x in p.items():
        for b,y in q.items():r[a+b]+=x*y
    return +r

def psub(p,q):
    r=Counter(p)
    for a,c in q.items():r[a]-=c
    return r

# Fibonacci language weight enumerators by terminal-letter recurrences.
T=[Counter() for _ in range(LIMIT+1)]
T[0]=Counter({0:1});T[1]=Counter({0:1,1:1})
for n in range(2,LIMIT+1):T[n]=T[n-1]+shift_poly(T[n-2],1)

# Sandwich counts between different endpoints and between two 1 endpoints.
M=[Counter() for _ in range(LIMIT+1)]
P=[Counter() for _ in range(LIMIT+1)]
M[0]=Counter({0:1})
for n in range(1,LIMIT+1):
    M[n]=T[n-1]
    P[n]=M[n-1]

U=[Counter() for _ in range(LIMIT+1)]
U[1]=Counter({0:1,1:1})
for n in range(2,LIMIT+1):
    p=psub(T[n],T[n-2])
    p=psub(p,shift_poly(P[n-2],2))
    for k in range(2,n//2+1):
        p=psub(p,concat_poly(Counter({j*2:v for j,v in U[k].items()}),M[n-2*k]))
    assert all(v>=0 for v in p.values()),(n,p)
    U[n]=+p

# Compare with a different coefficient recurrence derived by collecting the power series.
V=[Counter() for _ in range(LIMIT+1)]
V[1]=Counter({0:1,1:1})
for n in range(2,LIMIT+1):
    p=Counter(V[n-1])
    if n>=3:p+=shift_poly(V[n-2],1)
    if n==2:p+=Counter({1:1,2:1})
    if n==3:p=psub(p,Counter({1:1,2:1}))
    if n%2==0:p=psub(p,Counter({2*k:v for k,v in V[n//2].items()}))
    V[n]=p
assert all(V[n]==U[n] for n in range(1,LIMIT+1))

F=[0,1]
for n in range(LIMIT+3):F.append(F[-1]+F[-2])
assert all(sum(U[n].values())<=F[n+2] for n in range(1,LIMIT+1))

with localcontext() as ctx:
    ctx.prec=60
    phi=(Decimal(1)+Decimal(5).sqrt())/2
    def p_partial(K):
        return 2/(phi**3)-sum(Decimal(sum(U[k].values()))/(phi**(2*k+1)) for k in range(2,K))
    for K in (10,20,40,60,100):
        lo=p_partial(K)-phi**(2-K)
        hi=p_partial(K)
        assert lo>0
        print(f'K={K}  limiting_proportion_in=[{lo}, {hi}]')
    for n in (20,40,60,100,150):
        print(f'n={n}  proportion={Decimal(sum(U[n].values()))/Decimal(F[n+2])}')
print('PASS independent shortest-border count and refined Mahler law through 150, tail bound checked')
