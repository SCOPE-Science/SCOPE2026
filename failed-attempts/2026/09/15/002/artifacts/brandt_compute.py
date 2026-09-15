"""Brandt matrices for B=(-2,-109), maximal order O = L + Z*(i+k)/2, class number h, then eigenvectors."""
from fractions import Fraction
import itertools, json, math, sys

def mul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (
      a0*b0 -2*a1*b1 -109*a2*b2 -218*a3*b3,
      a0*b1 + a1*b0 +109*a2*b3 -109*a3*b2,
      a0*b2 + a2*b0 -2*a1*b3 +2*a3*b1,
      a0*b3 + a3*b0 + a1*b2 - a2*b1)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def smul(s,a): return tuple(s*x for x in a)
def N(x): return x[0]*x[0]+2*x[1]*x[1]+109*x[2]*x[2]+218*x[3]*x[3]
def tr(x): return 2*x[0]
def conj(x): return (x[0],-x[1],-x[2],-x[3])

I=(Fraction(1),Fraction(0),Fraction(0),Fraction(0))
qi=(Fraction(0),Fraction(1),Fraction(0),Fraction(0))
qj=(Fraction(0),Fraction(0),Fraction(1),Fraction(0))
qk=(Fraction(0),Fraction(0),Fraction(0),Fraction(1))
v=(Fraction(0),Fraction(1,2),Fraction(0),Fraction(1,2))  # glue (i+k)/2
OBAS=[I,qi,qj,qk,v]
print("order basis norms:", [N(b) for b in OBAS], flush=True)

# O as Z-module: elements with coords? O = {a + b v : a in L, b in {0,1}}.
def inO(x):
    # x in O iff x in L or x - v in L
    if all(c.denominator==1 for c in x): return True
    d = sub(x,v)
    return all(c.denominator==1 for c in d)
# sanity: closed under mul
import random
random.seed(0)
for _ in range(300):
    x = add((Fraction(random.randint(-3,3)),Fraction(random.randint(-3,3)),Fraction(random.randint(-3,3)),Fraction(random.randint(-3,3))), random.choice([(Fraction(0),)*4, v)])
    y = add((Fraction(random.randint(-3,3)),Fraction(random.randint(-3,3)),Fraction(random.randint(-3,3)),Fraction(random.randint(-3,3))), random.choice([(Fraction(0),)*4, v)])
    assert inO(x) and inO(y), (x,y)
    assert inO(mul(x,y)), (x,y,mul(x,y))
print("order closure OK", flush=True)

# Right fractional ideals: represent ideal J by Z-basis (4x4). Class set reps via Minkowski: enumerate left-O ideals of small norm? Use standard: right ideal classes <-> ... simplest: enumerate all right O-ideals containing ... via norm-form enumeration.
# Approach: enumerate elements of O by norm; right ideals of norm m correspond to ... Use Kainen-style: classes via orbits of ... Easier robust method:
# Right ideal class representatives: ideals I with O subset ... Use lattice enumeration: every class has representative I with N(I) | disc? Norms divide 109? Since 109 prime, each class has rep of norm 1 (principal, only O itself) — need full enumeration via connecting ideals: enumerate ALL right ideals of norm l^k ... Instead use the standard graph method:
# Vertices = right ideal classes; T_l adjacency via subideals. Start from O, BFS over l-neighbors using local structure: right subideals J ⊂ I with [I:J] = l^2 (N(J)=l*N(I))... For l != 109, # of such = l+1 counting multiplicity, and neighbor classes determined up to isomorphism.
# Local enumeration: J ⊂ O right ideal of norm l ⟺ J/lO corresponds to ... Use: enumerate x in O/lO with ... hmm.
# Simplest concrete: represent O/lO ≅ M2(F_l) (l != 109 unramified). Right ideals J ⊃ lO with [O:J]=l (N(J)=l) correspond to 1-dim... [O:J]=l means J/lO is a 2-dim right ideal of M2(F_l)? [O:lO]=l^4. [J:lO]=l^3, so J/lO has dim 3 in M2(F_l)?? That's left... Let me think: N(J)=[O:J]^{1/2}? For quat ideals N(J)^2 = [O:J]. N(J)=l → [O:J]=l^2 → J/lO has F_l-dim 2, a minimal right ideal of M2(F_l) = row space = l+1 of them. 
# So: construct iso O/lO → M2(F_l) explicitly, enumerate l+1 minimal right ideals, pull back to J's, identify isomorphism class via theta/short-vector fingerprint + right-multiplication equivalence.
