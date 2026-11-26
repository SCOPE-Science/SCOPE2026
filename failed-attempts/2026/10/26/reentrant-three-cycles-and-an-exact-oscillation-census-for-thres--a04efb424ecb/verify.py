#!/usr/bin/env python3
"""Exact finite-state certificate for threshold-two three-color cyclic competition on K_{a,b}.
Only Python 3 standard library is required. Every certificate step is fully enumerative."""
from itertools import product
from collections import Counter
from math import factorial, comb, lcm

COLORS = range(3)
SUPPORTS = [s for s in product(range(3), repeat=3) if any(s)]
PAIRS = list(product(SUPPORTS, repeat=2))

def nxt_pair(s):
    A,B = s
    def m(c,other):
        out=[0,0,0]
        for i in COLORS:
            j=(i+1)%3 if other[(i+1)%3]==2 else i
            out[j] = min(2, out[j]+c[i])
        return tuple(out)
    return m(A,B),m(B,A)

def tagged_next(s):
    A,B,side,color=s
    other=B if side==0 else A
    destination=(color+1)%3 if other[(color+1)%3]==2 else color
    AA,BB=nxt_pair((A,B))
    return AA,BB,side,destination

def eventual(z,step):
    seen={};seq=[]
    while z not in seen:
        seen[z]=len(seq);seq.append(z);z=step(z)
    return seen[z],len(seq)-seen[z]

def pair_returns(A,B,p):
    state=(A,B)
    labels=[(side,i) for side,s in enumerate((A,B)) for i in COLORS if s[i]]
    for side,i in labels:
        q=(A,B,side,i)
        for _ in range(p):q=tagged_next(q)
        if q[3]!=i:return False
    return True

def signature_weight(s):
    # Exponents of (x,X) or (y,Y): counts of exact-singleton and >=2 classes.
    return (sum(t==1 for t in s),sum(t==2 for t in s))

def polynomial_of(p):
    P=Counter()
    for A,B in PAIRS:
        if pair_returns(A,B,p):
            u,v=signature_weight(A);w,z=signature_weight(B)
            P[u,v,w,z]+=1
    return +P

def sparse(*monomials):
    return +Counter(dict(monomials))

assert len(SUPPORTS)==26 and len(PAIRS)==676
TAGGED=[(A,B,side,i) for A,B in PAIRS for side,s in enumerate((A,B)) for i in COLORS if s[i]]
assert len(TAGGED)==2808
T={z:tagged_next(z) for z in TAGGED}
assert all(w in T for w in T.values())
individual=Counter()
for z in TAGGED:
    first,period=eventual(z,lambda q:T[q]);individual[(first,period)]+=1
    assert first<=3 and period in (1,3,4)
whole=Counter()
for A,B in PAIRS:
    periods=[]
    for side,s in enumerate((A,B)):
        for i in COLORS:
            if s[i]:periods.append(eventual((A,B,side,i),lambda q:T[q])[1])
    L=lcm(*periods)
    whole[L]+=1
    assert L in (1,3,4)
assert max(first for first,period in individual)==3
assert sorted(whole)==[1,3,4]
assert all(pair_returns(A,B,2)==pair_returns(A,B,1) for A,B in PAIRS)
assert all(pair_returns(A,B,6)==pair_returns(A,B,3) for A,B in PAIRS)
assert all(pair_returns(A,B,12)==(pair_returns(A,B,1) or pair_returns(A,B,3) or pair_returns(A,B,4)) for A,B in PAIRS)

P1=polynomial_of(1); P3=polynomial_of(3);P4=polynomial_of(4)
R3=+Counter({k:P3[k]-P1[k] for k in P3.keys()|P1.keys()})
R4=+Counter({k:P4[k]-P1[k] for k in P4.keys()|P1.keys()})
# (x^u X^v)(y^w Y^z) represented by (u,v,w,z).
expected3=Counter({(0,3,0,3):1})
for j in (1,2,3):
    expected3[(0,3,j,0)]+=comb(3,j)
    expected3[(j,0,0,3)]+=comb(3,j)
assert R3==+expected3
assert R4==Counter({(0,2,0,2):6})

def T(n):
    return sum(factorial(n)//(factorial(i)*factorial(j)*factorial(n-i-j))
               for i in range(2,n-3) for j in range(2,n-i-1)) if n>=6 else 0

def H(n):return 2**n-2*n-2 if n>=4 else 0

def I(n):return factorial(n)*comb(3,n) if 1<=n<=3 else 0

def predicted(a,b):return T(a)*T(b)+T(a)*I(b)+I(a)*T(b),6*H(a)*H(b)

def exact_step(x,a):
    A=x[:a];B=x[a:]
    na=[sum(y==i for y in A) for i in COLORS]
    nb=[sum(y==i for y in B) for i in COLORS]
    return tuple((i+1)%3 if nb[(i+1)%3]>=2 else i for i in A)+tuple((i+1)%3 if na[(i+1)%3]>=2 else i for i in B)

def direct(a,b):
    N=a+b;counts=Counter()
    for x in product(COLORS,repeat=N):
        seen={};z=x
        while z not in seen:
            seen[z]=len(seen);z=exact_step(z,a)
        entry=seen[z];p=len(seen)-entry
        assert entry<=3 and p in (1,3,4)
        if entry==0:counts[p]+=1
    r3,r4=predicted(a,b)
    assert counts[3]==r3 and counts[4]==r4
    return N,3**N,counts[1],counts[3],counts[4]

# Independent vertex-by-vertex enumeration, not driven by the quotient.
checks=[(1,6),(2,4),(2,6),(3,6),(4,4),(4,6)]
exhausted=0
for a,b in checks:
    n,k,q,r3,r4=direct(a,b)
    exhausted+=k
    print('DIRECT',a,b,'total',k,'fixed',q,'primitive3',r3,'primitive4',r4)
# Sharp transient and realizations can be checked directly on explicit labelled tuples.
def witness(A,B):
    a=sum(A); b=sum(B)
    x=tuple(i for i,c in enumerate(A) for _ in range(c))+tuple(i for i,c in enumerate(B) for _ in range(c))
    return eventual(x,lambda q:exact_step(q,a))
assert witness((0,1,1),(2,0,2))==(3,1)
assert witness((0,0,1),(2,2,2))==(0,3)
assert witness((0,2,2),(2,0,2))==(0,4)
assert H(4)==6 and T(6)==90
assert predicted(6,6)==(8100,15000)
print('QUOTIENT',len(PAIRS),'TAGGED',len(TAGGED),'TAG_PERIODS',sorted(set(p for t,p in individual)), 'PAIR_PERIODS',dict(whole),'SHARP_PREPERIOD',3)
print('PRIMITIVE3_POLYNOMIAL',dict(sorted(R3.items())))
print('PRIMITIVE4_POLYNOMIAL',dict(sorted(R4.items())))
print('DIRECT_TOTAL',exhausted)
print('VERIFY_OK')
