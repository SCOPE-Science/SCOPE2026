"""Exact finite-field verification of 28 bitangents and their fifth-power orbits.

The field is F_5[t]/(t^4-2), a field of size 625 because 2 is not
in the subgroup of fourth powers of F_25^* (order six).
"""
from collections import Counter
from itertools import permutations, product

class K:
    def __init__(self, v):
        if isinstance(v, K): self.v = v.v
        elif isinstance(v,int): self.v = (v%5,0,0,0)
        else: self.v = tuple(int(a)%5 for a in v)
    def __add__(self, other):
        w=K(other); return K(tuple((self.v[i]+w.v[i])%5 for i in range(4)))
    __radd__=__add__
    def __neg__(self): return K(tuple(-i for i in self.v))
    def __sub__(self, other): return self+(-K(other))
    def __rsub__(self,other): return K(other)-self
    def __mul__(self,other):
        w=K(other); z=[0]*7
        for i in range(4):
            for j in range(4): z[i+j]+=self.v[i]*w.v[j]
        for k in range(6,3,-1): z[k-4]+=2*z[k]
        return K(tuple(z[:4]))
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0: return (self**623)**(-n)
        o=K(1); a=self
        while n:
            if n&1:o=o*a
            a=a*a; n//=2
        return o
    def __eq__(self,o): return self.v==K(o).v
    def __hash__(self): return hash(self.v)
    def __repr__(self): return str(self.v)

t=K((0,1,0,0)); assert t**4==2 and t**625==t
r2=[j*t for j in range(1,5)]
r4=[j*t*t for j in range(1,5)]
assert len(set(r2))==len(set(r4))==4
assert all(z**4==2 for z in r2)
assert all(z**4==4 for z in r4)
# Coefficients of F(X,Y,uX+vY) in X^(4-j)Y^j.
from math import comb
for u in r2:
    for v in r2:
        left=[]; right=[]
        A,B,C=u*u,u*v,v*v
        for j in range(5):
            c = 3*comb(4,j)*(u**(4-j))*(v**j)
            if j in (0,4): c+=1
            left.append(c)
        right=[A*A,2*A*B,B*B+2*A*C,2*B*C,C*C]
        assert left==right, (u,v,left,right)
        assert B*B-4*A*C!=0  # two distinct double contacts

# Each line is normalized with first nonzero coefficient 1.
def normal(v):
    # Nonzero x has inverse x**623 in F_625 (since |F_625*|=624).
    for x in v:
        if x!=0:
            inv=x**623
            return tuple(y*inv for y in v)
    raise ValueError('zero line')

lines=[]
for s in r4: lines += [normal((1,-s,0))]
for s in r2: lines += [normal((1,0,-s)),normal((0,1,-s))]
for u in r2:
    for v in r2: lines.append(normal((-u,-v,1)))
assert len(lines)==len(set(lines))==28
set_lines=set(lines)
assert all(normal(tuple(a**5 for a in ln)) in set_lines for ln in lines)
rem=set(lines); sizes=[]
while rem:
    start=next(iter(rem)); p=start; orb=[]
    while p not in orb:
        orb.append(p); p=normal(tuple(a**5 for a in p))
    assert p==start
    for x in orb: rem.remove(x)
    sizes.append(len(orb))
assert Counter(sizes)==Counter({2:2,4:6}),sizes
assert all(normal(tuple(a**(5**4) for a in ln))==ln for ln in lines)

# Uniqueness of the F_5-rational diagonal normal form of every
# degree-four Sziklai-optimal plane quartic.
triples={q for q in product(range(1,5),repeat=3) if sum(q)%5==0}
orbit={(c*x%5,c*y%5,c*z%5) for c in range(1,5) for x,y,z in set(permutations((1,1,3)))}
assert len(triples)==12 and triples==orbit
print('VERIFY_OK: 28 distinct bitangents; Frobenius cycle type (2,2,4,4,4,4,4,4); one F5 form.')
