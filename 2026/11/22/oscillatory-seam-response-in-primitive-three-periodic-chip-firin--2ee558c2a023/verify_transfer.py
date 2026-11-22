#!/usr/bin/env python3
"""Exact transfer and characteristic-polynomial verification for cubic strip period-three chip firing."""
import sympy as sp

COLS = [(a, b) for a in range(3) for b in range(3)]
PAIRS = [(a, b) for a in range(9) for b in range(9)]
INDEX = {s: i for i, s in enumerate(PAIRS)}
Z = sp.symbols('z')
A = Z**4 + 2*Z**3 + 12*Z**2 + 5*Z + 1
B = Z**4 + 4*Z**3 + 6*Z**2 + Z + 1
C = Z**5 - 6*Z**4 + 5*Z**3 + Z**2 + 6*Z - 1

def weight(p, q, r):
    a, b = COLS[p]
    c, d = COLS[q]
    e, f = COLS[r]
    top = int(a == (c-1)%3) + int(e == (c-1)%3) + int(d == (c-1)%3)
    bot = int(b == (d-1)%3) + int(f == (d-1)%3) + int(c == (d-1)%3)
    return top*bot

T = sp.MutableSparseMatrix(81, 81, {})
for i, (p, q) in enumerate(PAIRS):
    for r in range(9):
        w = weight(p, q, r)
        if w:
            T[i, INDEX[(q, r)]] = w

def swap(c):
    a,b = COLS[c]
    return 3*b+a

swap_index = [INDEX[(swap(a),swap(b))] for a,b in PAIRS]
assert sorted(swap_index) == list(range(81))
assert all(swap_index[swap_index[i]] == i for i in range(81))
for i in range(81):
    for j in range(81):
        assert T[swap_index[i], swap_index[j]] == T[i,j]

seen=set()
plus=[]
minus=[]
for i in range(81):
    if i in seen:
        continue
    j=swap_index[i]
    seen.add(i)
    seen.add(j)
    plus.append((i,j))
    if i != j:
        minus.append((i,j))
assert len(plus)==45 and len(minus)==36

TP = sp.zeros(len(plus))
TM = sp.zeros(len(minus))
for k,(i,j) in enumerate(plus):
    for h,(u,v) in enumerate(plus):
        TP[h,k] = T[u,i] + (T[u,j] if i != j else 0)
for k,(i,j) in enumerate(minus):
    for h,(u,v) in enumerate(minus):
        TM[h,k] = T[u,i]-T[u,j]

assert sp.expand(TP.charpoly(Z).as_expr() - Z**24*(Z-1)**4*(Z**2+Z+1)**2*B**2*C) == 0
assert sp.expand(TM.charpoly(Z).as_expr() - Z**21*(Z-1)**5*(Z**2+Z+1)*A**2) == 0

# Newton identities reconstruct root power sums from the monic polynomials.
def rootsum(poly, n):
    coeff=[int(x) for x in sp.Poly(poly,Z).all_coeffs()]
    degree=len(coeff)-1
    s=[degree]
    for k in range(1,n+1):
        v=sum(coeff[j]*s[k-j] for j in range(1,min(k-1,degree)+1))
        if k <= degree:
            v += k*coeff[k]
        s.append(-v)
    return s[n]

assert rootsum(A,0)==4
assert [rootsum(A,k) for k in range(1,5)]==[-2,-20,49,148]

def formula(n):
    cyc=2 if n%3==0 else -1
    aa=rootsum(A,n)
    bb=rootsum(B,n)
    cc=rootsum(C,n)
    prism=9+3*cyc+2*aa+2*bb+cc
    mobius=-1+cyc-2*aa+2*bb+cc
    assert prism-mobius==4*aa+10+2*cyc
    assert prism%3==0 and mobius%3==0
    return 2*prism//3,2*mobius//3

# Compare independent trace calculations with the all-n Newton formula.
Q=sp.eye(81)
EXPECTED=[(164,24),(528,128),(1020,3100),(8064,9220),(57540,32284),
          (202864,229344),(931328,1173444),(5508800,4831808)]
for n in range(1,11):
    Q=Q*T
    if n>=3:
        direct_prism=sum(Q[i,i] for i in range(81))
        direct_mobius=sum(Q[i,swap_index[i]] for i in range(81))
        x,y=formula(n)
        assert (direct_prism,direct_mobius)==(3*x//2,3*y//2)
        assert (x,y)==EXPECTED[n-3]

# Rational root brackets and exact inequalities used in the proof.
for lo,hi in [(sp.Rational(15,100),sp.Rational(17,100)),
              (sp.Rational(173,100),sp.Rational(174,100)),
              (sp.Rational(488,100),sp.Rational(489,100))]:
    assert C.subs(Z,lo)*C.subs(Z,hi)<0
r=sp.Rational(24,5)
assert r**4-2*r**3-12*r**2-5*r-1>0
assert len(sp.polys.polytools.intervals(A,all=True)[0])==0
assert len(sp.polys.polytools.intervals(B,all=True)[0])==0
assert len(sp.polys.polytools.intervals(C,all=True)[0])==3
print('TRANSFER_CHARACTERISTIC_ROOT_AND_TRACES_PASSED')
for n in range(3,11):print(n,*formula(n))
