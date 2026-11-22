"""Independent finite certificates and exhaustive tests for the cyclic two-step Rule 184 image theorem.

Run with Python 3 standard library: python3 verify.py
Finite checks corroborate; the finite-context lemmas and transfer proof in RESULT.md
are what make the conclusions valid at all lengths.
"""
from itertools import product, permutations
from collections import Counter
from fractions import Fraction
from math import factorial, comb

FORBIDDEN=('1100','110100')


def f(a,b,c):
    return (a and not b) or (b and c)


def g(a,b,c):
    return (c and not b) or (b and a)


def rotate_update(x, local):
    n=len(x)
    return tuple(int(local(x[(i-1)%n],x[i],x[(i+1)%n])) for i in range(n))


def forbidden(y):
    n=len(y)
    return any(all(y[(i+j)%n]==int(v) for j,v in enumerate(w))
               for w in FORBIDDEN for i in range(n))


def seq_out(x, local):
    return ''.join(str(int(local(*x[i:i+3]))) for i in range(len(x)-2))

# The exact composite defect list for the one-step selector.
D=[]
for x in product((0,1),repeat=5):
    inner=[int(g(*x[j:j+3])) for j in range(3)]
    if int(f(*inner))!=x[2]:
        D.append(''.join(map(str,x)))
assert sorted(D)==sorted(('01100','11000','11001','11100'))

# Rule 184 never produces four consecutive output symbols 1100.
assert all(seq_out(x,f)!='1100' for x in product((0,1),repeat=6))

# Every six-bit window whose four reflected outputs equal 1100.
BAD=[]
for x in product((0,1),repeat=6):
    if seq_out(x,g)=='1100':
        BAD.append(''.join(map(str,x)))
assert sorted(BAD)==['110100','111000']

# An occurrence of 110100 in a forward image forces forbidden 1100
# in every eight-bit input context (a finite complete truth table).
PARENTS=[]
for x in product((0,1),repeat=8):
    if seq_out(x,f)=='110100':
        PARENTS.append(''.join(map(str,x)))
assert len(PARENTS)==9
assert all('1100' in w for w in PARENTS)
assert sorted(PARENTS)==sorted(a+b for a in ('0111','1011','1111') for b in ('0000','0001','0010'))

# Prefix matcher for the two forbidden words.
PREF=('', '1', '11', '110', '1101', '11010')
assert set(PREF)=={w[:j] for w in FORBIDDEN for j in range(len(w))}
S=len(PREF)
EDGES=[]
for i,p in enumerate(PREF):
    for bit in '01':
        v=p+bit
        if any(v.endswith(w) for w in FORBIDDEN):
            continue
        t=max((q for q in PREF if v.endswith(q)),key=len)
        EDGES.append((i,PREF.index(t),int(bit)))

# Sparse bivariate polynomials p[(degree of z, degree of u)] = coeff

def mult(a,b):
    c=Counter()
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            c[i+k,j+l]+=v*w
    return {k:v for k,v in c.items() if v}


def add(a,b,sign=1):
    c=Counter(a)
    for k,v in b.items():
        c[k]+=sign*v
    return {k:v for k,v in c.items() if v}

zero={}
one={(0,0):1}
U=[[(zero if i!=j else one).copy() for j in range(S)] for i in range(S)]
for i,j,b in EDGES:
    U[i][j]=add(U[i][j],{(1,b):1},-1)

# Exact complete 6x6 determinant via Leibniz expansion: 720 terms.
DET={}
for perm in permutations(range(S)):
    inversions=sum(perm[i]>perm[j] for i in range(S) for j in range(i+1,S))
    term=one
    for i,j in enumerate(perm):
        term=mult(term,U[i][j])
        if not term:
            break
    DET=add(DET,term,-1 if inversions%2 else 1)
EXPECTED={(0,0):1,(1,0):-1,(1,1):-1,(4,2):1,(6,3):1}
assert DET==EXPECTED,(DET,EXPECTED)

# Independent fixed-mass trace recurrence (no determinant use).
T=[[{} for _ in range(S)] for __ in range(S)]
for i,j,b in EDGES:
    T[i][j]=add(T[i][j],{(0,b):1})

def matmul(A,B):
    return [[reduce_sum(mult(A[i][k],B[k][j]) for k in range(S))
             for j in range(S)] for i in range(S)]

def reduce_sum(it):
    v=zero
    for x in it:
        v=add(v,x)
    return v

# Compare every possible source against the entire admissible output set.
# A separate independent formula checks the explicit double backward selector.
P=[[one.copy() if i==j else {} for j in range(S)] for i in range(S)]
totals=[]
for n in range(1,16):
    if n<=13:
        observed={rotate_update(rotate_update(x,f),f) for x in product((0,1),repeat=n)}
        expected={x for x in product((0,1),repeat=n) if not forbidden(x)}
        assert observed==expected,('image',n,observed^expected)
        for y in expected:
            assert rotate_update(rotate_update(rotate_update(rotate_update(y,g),g),f),f)==y,('selector',n,y)
        for y in set(product((0,1),repeat=n))-expected:
            assert y not in observed
    P=matmul(P,T)
    trace=reduce_sum(P[i][i] for i in range(S))
    poly={k[1]:v for k,v in trace.items() if k[0]==0}
    assert sum(poly.values())>=1
    if n<=13:
        density=Counter(sum(y) for y in expected)
        assert poly==dict(density),('density',n,poly,density)
    for k in range(n+1):
        direct=Fraction(0)
        for a in range(n//4+1):
            for b in range((n-4*a)//6+1):
                c=n-4*a-6*b
                m=a+b+c
                if not (0<=k-2*a-3*b<=c):
                    continue
                direct+=((-1)**(a+b))*Fraction(n*factorial(m-1),factorial(a)*factorial(b)*factorial(c))*comb(c,k-2*a-3*b)
        assert poly.get(k,0)==direct,(n,k,poly.get(k,0),direct)
    totals.append(sum(poly.values()))
assert totals==[2,4,8,12,22,34,58,100,170,294,508,882,1536,2678,4678],totals

# The rational series yields linear recurrence for all coefficients.
# Tested here in the exact polynomial ring Z[u].
traces=[]
P=[[one.copy() if i==j else {} for j in range(S)] for i in range(S)]
for n in range(1,24):
    P=matmul(P,T)
    t=reduce_sum(P[i][i] for i in range(S))
    traces.append({j:v for (i,j),v in t.items() if i==0})
for n in range(7,24):
    rhs=add(traces[n-2],{k+1:v for k,v in traces[n-2].items()})
    rhs=add(rhs,{k+2:v for k,v in traces[n-5].items()},-1)
    rhs=add(rhs,{k+3:v for k,v in traces[n-7].items()},-1)
    assert traces[n-1]==rhs,('recurrence',n)
print('VERIFY_OK: context lemmas, polynomial determinant, exhaustive ring images and inverse through n=13, density traces and exact bivariate binomial sums through n=15, recurrence through n=23')
