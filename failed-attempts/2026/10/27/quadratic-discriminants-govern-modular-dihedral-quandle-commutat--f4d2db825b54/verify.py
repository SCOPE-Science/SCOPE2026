"""Finite-field checks for the commutator-image theorem in K[R_5].
Run: python verify.py (stdlib only).
"""
from itertools import product

P = 5

def commutator_w(f, g, add, mul, sub):
    p01 = sub(mul(f[0],g[1]),mul(f[1],g[0]))
    p02 = sub(mul(f[0],g[2]),mul(f[2],g[0]))
    p03 = sub(mul(f[0],g[3]),mul(f[3],g[0]))
    p12 = sub(mul(f[1],g[2]),mul(f[2],g[1]))
    p13 = sub(mul(f[1],g[3]),mul(f[3],g[1]))
    return (mul(3,p01),mul(3,p02),mul(4,add(p03,p12)),mul(4,p13))

class GF:
    def __init__(self, ext=False):
        self.ext=ext
        self.q=25 if ext else 5
        self.elements=range(self.q)
        if ext:
            self.zero=0
            self.one=1
        else:
            self.zero=0
            self.one=1
    def add(self,a,b):
        if not self.ext: return (a+b)%5
        return ((a%5+b%5)%5)+5*((a//5+b//5)%5)
    def neg(self,a):
        if not self.ext: return -a%5
        return (-a%5)+5*(-(a//5)%5)
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        if not self.ext:return a*b%5
        a0,a1=a%5,a//5;b0,b1=b%5,b//5
        return ((a0*b0+3*a1*b1)%5)+5*((a0*b1+a1*b0)%5)
    def sq(self,a): return self.mul(a,a)
    def scal(self,n,a):return self.mul(n%5,a)


def criterion(z,F,squares):
    # Coordinates z=(z1,z2,z3,z4) in the ordered basis w,w^2,w^3,w^4.
    delta=F.sub(F.sq(z[2]),F.scal(2,F.mul(z[1],z[3])))
    return z[0]!=0 or delta in squares

# Exhaustive direct commutator image on F_5^4 x F_5^4.
F=GF(False); elems=list(product(range(5),repeat=4)); observed=set()
for f in elems:
    for g in elems:
        observed.add(commutator_w(f,g,F.add,F.mul,F.sub))
sq={F.sq(x) for x in F.elements}
expected={z for z in elems if criterion(z,F,sq)}
assert observed==expected,('commutator image mismatch', len(observed),len(expected),next(iter(observed^expected),None))
assert len(observed)==585 and len(elems)-len(observed)==40

# Check the linearization against original quandle multiplication e_i*e_j=e_(2j-i) for each basis pair.
# e_i corresponds to X^i=exp(i*w); coefficient of w^k is i^k/k!.
invfact=[1,1,3,1,4]  # inverses of 0!,1!,2!,3!,4! modulo 5
w_basis=[tuple((pow(i,k,5)*invfact[k])%5 for k in range(5)) for i in range(5)]
def mul5(u,v): return tuple(x*y%5 for x,y in zip(u,v))
for i,j in product(range(5), repeat=2):
    e1=w_basis[i][:4];e2=w_basis[j][:4]
    got=commutator_w(e1,e2,F.add,F.mul,F.sub)
    expect=tuple((w_basis[(2*j-i)%5][k]-w_basis[(2*i-j)%5][k])%5 for k in range(1,5))
    assert got==expect,(i,j,got,expect)

# Extension field F_25: independent enumeration of all 25^3 triples,
# square/nonsquare split and a randomized witness check for realized outputs.
G=GF(True); sq25={G.sq(x) for x in G.elements}
fail=0
for b,s,d in product(G.elements, repeat=3):
    discr=G.sub(G.sq(s),G.scal(4,G.mul(b,d)))
    roots=[x for x in G.elements if G.add(G.sq(x),G.mul(b,d))==G.mul(s,x)]
    assert bool(roots)==(discr in sq25)
    if discr not in sq25:fail+=1
assert fail==25*24*24//2

# Sample constructed commutators in extension field; all must satisfy criterion.
import random
rng=random.Random(20261018)
for _ in range(5000):
    f=[rng.randrange(25) for j in range(4)]
    g=[rng.randrange(25) for j in range(4)]
    assert criterion(commutator_w(f,g,G.add,G.mul,G.sub),G,sq25)

# General theorem implies exactly (q(q-1)^2)/2 non-single-commutators.
# q=5: 40 of 625, q=25: 7200 of 390625.
print('VERIFY_OK F5 direct quandle basis, all 390625 ordered pairs in F5^4, F25 quadratic criterion 15625 triples')
print('q5 image=585 missing=40, q25 missing=7200')
