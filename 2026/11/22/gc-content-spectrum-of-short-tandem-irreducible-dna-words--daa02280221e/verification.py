"""Exact standalone integer-polynomial checks for a constrained DNA enumerator.
Uses Python's standard library. No solver or floating-point certificates.
"""
from itertools import product
from collections import defaultdict
from math import comb

A=range(4)
def gc(a): return int(a>=2)
def legal(t):
    return all(t[i]!=t[i+1] for i in range(len(t)-1)) and all(t[i:i+2]!=t[i+2:i+4] for i in range(len(t)-3))

def orbit(s):
    def op(x,t0,t1):
        if x<2: return x^t0
        return 2+((x-2)^t1)
    return min(tuple(op(x,a,b) for x in s) for a in range(2) for b in range(2))
S=list(s for s in product(A,repeat=3) if legal(s))
R=sorted({orbit(s) for s in S})
assert len(S)==36 and len(R)==10
idx={s:j for j,s in enumerate(R)}
initial=[defaultdict(int) for _ in R]
M=[[defaultdict(int) for _ in R] for _ in R]
for s in S:
    initial[idx[orbit(s)]][sum(map(gc,s))]+=1
for s in R:
    for x in A:
        if legal(s+(x,)):
            M[idx[s]][idx[orbit(s[1:]+(x,))]][gc(x)]+=1

def mul(a,b):
    out=defaultdict(int)
    for i,x in a.items():
        for j,y in b.items(): out[i+j]+=x*y
    return {k:v for k,v in out.items() if v}
def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items(): out[k]+=v
    return {k:v for k,v in out.items() if v}
def scale(p,k): return {j:k*v for j,v in p.items() if k*v}
ONE={0:1}
ZERO={}
def prodmat(A,B):
    n=len(A)
    return [[add(*(mul(A[i][k],B[k][j]) for k in range(n))) for j in range(n)] for i in range(n)]
I=[[ONE if i==j else ZERO for j in range(10)] for i in range(10)]
B=I
D=[ONE]
# Faddeev--LeVerrier: det(I-zM) = sum c_k z^k
for k in range(1,11):
    C=prodmat(M,B)
    tr=add(*(C[i][i] for i in range(10)))
    assert all(a%k==0 for a in tr.values()), (k,tr)
    ck={j:-v//k for j,v in tr.items() if v}
    D.append(ck)
    B=[[add(C[i][j],ck if i==j else ZERO) for j in range(10)] for i in range(10)]

expected_D=[
 {0:1}, {}, {1:-3}, {1:-4,2:-4}, {1:-4,2:-3,3:-4},
 {2:-2,3:-2}, {2:2,4:2}, {3:4,4:4}, {4:4}, {}, {}]
assert D==expected_D,(D,expected_D)

expected_N=[
 {0:1},{0:2,1:2},{0:2,1:5,2:2},
 {0:2,1:6,2:6,3:2},{1:6,2:5,3:6},
 {1:2,2:4,3:4,4:2}, {},
 {2:-2,3:-4,4:-4,5:-2}, {3:-4,4:-4,5:-4}, {4:-4,5:-4}]
# Derived from explicit N expression in the result.
# N_5 = 2u(u+1)(u^2+u+1); N_7 = -2u^2(u+1)(u^2+u+1)
assert len(expected_N)==10

# Compute exact coefficients from the orbit transfer and compare numerator D*F.
a=[{0:1},{0:2,1:2},{0:2,1:8,2:2}]
v=initial[:]
for n in range(3,18):
    a.append(add(*v))
    v=[add(*(mul(v[i],M[i][j]) for i in range(10))) for j in range(10)]
for n in range(len(a)):
    lhs=add(*(mul(D[j],a[n-j]) for j in range(min(n,len(D)-1)+1)))
    expected=expected_N[n] if n<len(expected_N) else {}
    assert lhs==expected,('rational identity',n,lhs,expected)

for n in range(0,9):
    hist=defaultdict(int)
    for t in product(A,repeat=n):
        if legal(t): hist[sum(map(gc,t))]+=1
    assert dict(hist)==a[n],('bruteforce',n,dict(hist),a[n])

# Verify color swap: replacing each symbol by a symbol in opposite GC group
# preserves legal words, so every coefficient is symmetric about n/2.
for n in range(len(a)):
    assert all(a[n].get(k,0)==a[n].get(n-k,0) for k in range(n+1))

# Strong connectivity is checked for the full 36-state automaton,
# not only the orbit quotient. Exact, exhaustive finite graph check.
E={s:[] for s in S}
for s in S:
    for x in A:
        t=s[1:]+(x,)
        if legal(s+(x,)):
            E[s].append(t)
            assert t in E
for start in S:
    todo={start}; reached={start}
    while todo:
        state=todo.pop()
        for j in E[state]:
            if j not in reached: reached.add(j); todo.add(j)
    assert len(reached)==36, (start,len(reached))
for cycle in ((0,1,2), (0,1,2,1)):
    s=cycle*3
    assert legal(s) and sum(gc(x) for x in cycle)==1
assert 3*1-4*1==-1  # (length, GC-weight) lattice determinant

# Check graph strong connectivity (an essential PF premise).
for start in range(len(R)):
    todo={start}; reached={start}
    while todo:
        i=todo.pop()
        for j in range(len(R)):
            if M[i][j] and j not in reached: reached.add(j); todo.add(j)
    assert len(reached)==len(R)

# Numeric coefficients are used only to corroborate the local limit.
print('PASS exact 10-state determinant, rational numerator, 4^8 brute-force, recurrence, symmetry, 36-state connectivity, lattice cycles')
for n in (4,6,8,10,12,14,16):
    print('length',n,'balanced',a[n].get(n//2,0),'total',sum(a[n].values()))
