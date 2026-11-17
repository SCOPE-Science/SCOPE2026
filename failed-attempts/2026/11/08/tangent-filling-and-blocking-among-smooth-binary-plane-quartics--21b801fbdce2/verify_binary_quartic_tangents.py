#!/usr/bin/env python3
"""Exact census of tangent-filling and blocking smooth plane quartics over GF(2).
Requires Python 3.10+ and SymPy. No external data or network access.

Binary coordinates p=4*x+2*y+z; coefficient m has bit i for MON[i].
The proof-grade geometric-smoothness check uses unit ideals on all three
projective affine charts, not point sampling in extension fields.
"""
from collections import Counter
from itertools import product
from fractions import Fraction
from sympy import symbols, groebner

X, Y, Z = symbols("X Y Z")
MON = [(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
assert len(MON)==15
BASIS = [X**a*Y**b*Z**c for (a,b,c) in MON]
INDEX = {m:i for i,m in enumerate(MON)}
PTS = tuple(range(1,8))

def parity(v):
    return v.bit_count() & 1

def point_bits(p):
    return ((p>>2)&1, (p>>1)&1, p&1)

def dot(a,b):
    return parity(a&b)

def support(l):
    return sum(1<<(p-1) for p in PTS if dot(l,p)==0)

LINE_POINTS = {l:support(l) for l in PTS}
assert len(set(LINE_POINTS.values()))==7
assert all(s.bit_count()==3 for s in LINE_POINTS.values())

# Polynomial substitution is performed in a separate monomial-dictionary algebra
# to avoid relying on SymPy's polynomial substitutions for the group action.
ONE = {(0,0,0):1}

def mul(f,g):
    r = {}
    for (a,b,c),v in f.items():
        for (d,e,h),w in g.items():
            t=(a+d,b+e,c+h)
            r[t]=r.get(t,0)^(v&w)
    return {t:v for t,v in r.items() if v}

def poly_powers(f):
    t=[ONE]
    for i in range(4):t.append(mul(t[-1],f))
    return t

def matrices():
    for a,b,c in product(PTS,repeat=3):
        if a!=b and c not in (a,b,a^b):
            yield a,b,c

G = tuple(matrices())
assert len(G)==168

def transformation_columns(A):
    # A's columns are encoded as vectors with x,y,z in bits 2,1,0.
    return [
        {(int(j==0),int(j==1),int(j==2)):1 for j in range(3) if (A[j]>>i)&1}
        for i in (2,1,0)
    ]

POWER_TABLE = []
for A in G:
    POWER_TABLE.append([poly_powers(f) for f in transformation_columns(A)])

def change_coordinates(mask,power_table):
    h = {}
    for i,(a,b,c) in enumerate(MON):
        if (mask>>i)&1:
            piece=mul(mul(power_table[0][a],power_table[1][b]),power_table[2][c])
            for t in piece:
                h[t]=h.get(t,0)^1
    return sum((v&1)<<INDEX[t] for t,v in h.items())

def smooth_over_algebraic_closure(mask):
    f=sum(BASIS[i] for i in range(15) if (mask>>i)&1)
    ideal_generators=(f, f.diff(X), f.diff(Y), f.diff(Z))
    for coord in (X,Y,Z):
        variables=tuple(q for q in (X,Y,Z) if q!=coord)
        h=groebner([v.subs(coord,1) for v in ideal_generators],
                    *variables, modulus=2)
        # Unit ideal over GF(2): equivalent to absence of a common zero
        # over an algebraic closure, by the weak Nullstellensatz.
        if len(h.polys)!=1 or h.polys[0].as_expr()!=1:
            return False
    return True

# Direct rational-point and derivative evaluation (different representation
# from the polynomial substitution/orbit construction).
EVAL = []
DX,DY,DZ = [],[],[]
for p in PTS:
    x,y,z=point_bits(p)
    EVAL.append(sum(1<<i for i,(a,b,c) in enumerate(MON) if x**a*y**b*z**c))
    DX.append(sum(1<<i for i,(a,b,c) in enumerate(MON) if a%2 and x**(a-1)*y**b*z**c))
    DY.append(sum(1<<i for i,(a,b,c) in enumerate(MON) if b%2 and x**a*y**(b-1)*z**c))
    DZ.append(sum(1<<i for i,(a,b,c) in enumerate(MON) if c%2 and x**a*y**b*z**(c-1)))

def profile(mask):
    cp=tuple(p for p in PTS if not parity(mask&EVAL[p-1]))
    tangents=[]
    for p in cp:
        l=4*parity(mask&DX[p-1])+2*parity(mask&DY[p-1])+parity(mask&DZ[p-1])
        assert l in PTS and dot(l,p)==0
        tangents.append(l)
    tangent_union=0
    for l in tangents:tangent_union|=LINE_POINTS[l]
    blocking=all(any(dot(l,p)==0 for p in cp) for l in PTS)
    return (len(cp),len(set(tangents)),tangent_union.bit_count(),blocking)


def independent_profile(mask):
    # Separate literal polynomial/derivative evaluation and incidence loops.
    active=[(a,b,c) for i,(a,b,c) in enumerate(MON) if (mask>>i)&1]
    curve=[]
    tangent=[]
    for p in PTS:
        x,y,z=point_bits(p)
        if sum(x**a*y**b*z**c for a,b,c in active)%2==0:
            curve.append(p)
            u=sum((a%2)*(x**(a-1) if a else 0)*y**b*z**c for a,b,c in active)%2
            v=sum((b%2)*x**a*(y**(b-1) if b else 0)*z**c for a,b,c in active)%2
            w=sum((c%2)*x**a*y**b*(z**(c-1) if c else 0) for a,b,c in active)%2
            tangent.append(4*u+2*v+w)
    assert all(k in PTS for k in tangent)
    covered=sum(any(dot(l,p)==0 for l in tangent) for p in PTS)
    blocking=all(any(dot(l,p)==0 for p in curve) for l in PTS)
    return (len(curve),len(set(tangent)),covered,blocking)


def census():
    visited=set()
    orbit_reps=[]
    smooth_forms=set()
    weighted=Counter()
    orbit_count=Counter()
    for f in range(1,1<<15):
        if f in visited:continue
        orb={change_coordinates(f,P) for P in POWER_TABLE}
        assert f in orb and orb.isdisjoint(visited)
        visited.update(orb)
        if not smooth_over_algebraic_closure(f):continue
        smooth_forms.update(orb)
        profile_f=profile(f)
        orbit_reps.append((f,len(orb),profile_f))
        weighted[profile_f]+=len(orb)
        orbit_count[profile_f]+=1
    assert visited==set(range(1,1<<15))
    assert len(smooth_forms)==10920 and len(orbit_reps)==78
    assert sum(weighted.values())==10920

    # Independent incidence accumulation over EVERY smooth coefficient vector,
    # not just the 78 orbit representatives. Checks invariance simultaneously.
    direct=Counter(profile(f) for f in smooth_forms)
    assert weighted==direct
    # Truly separate arithmetic implementation for all smooth quartics.
    for f in smooth_forms:
        assert profile(f)==independent_profile(f)
    assert sum(orbit_count.values())==78

    tally=Counter()
    classes=Counter()
    pointcounts=Counter()
    pointfilling=Counter()
    for (np,nt,covered,blocking),weight in weighted.items():
        filling=(covered==7)
        tally[(filling,blocking)]+=weight
        classes[(filling,blocking)]+=orbit_count[(np,nt,covered,blocking)]
        pointcounts[np]+=weight
        if filling:pointfilling[np]+=weight
    assert tally==Counter({(True,True):2040,(True,False):616,
                           (False,True):1848,(False,False):6416})
    assert classes==Counter({(True,True):14,(True,False):6,
                             (False,True):11,(False,False):47})
    assert sum(tally[k] for k in tally if k[0])==2656
    assert sum(tally[k] for k in tally if k[1])==3888
    assert pointcounts==Counter({0:165,1:1008,2:2646,3:3360,
                                 4:2541,5:1008,6:168,7:24})
    assert pointfilling==Counter({3:364,4:1260,5:840,6:168,7:24})
    print("MODELS 32767  ORBITS",len(orbit_reps),"SMOOTH",len(smooth_forms))
    print("CATEGORIES  filling_blocking, filling_notblocking, notfilling_blocking, neither")
    print("EQUATIONS",tally[(True,True)],tally[(True,False)],tally[(False,True)],tally[(False,False)])
    print("PROJECTIVE_CLASSES",classes[(True,True)],classes[(True,False)],classes[(False,True)],classes[(False,False)])
    print("TANGENT_FILLING",sum(tally[k] for k in tally if k[0]),"PROBABILITY",Fraction(2656,10920))
    print("POINT_COUNT_TOTALS", sorted(pointcounts.items()))
    print("POINT_COUNT_FILLING",sorted(pointfilling.items()))
    print("EXAMPLE_MASKS", {category:min(f for f,w,p in orbit_reps if (p[2]==7,p[3])==category) for category in tally})
    print("BINARY_QUARTIC_TANGENT_BLOCKING_CENSUS_PASS")

if __name__=='__main__':census()
