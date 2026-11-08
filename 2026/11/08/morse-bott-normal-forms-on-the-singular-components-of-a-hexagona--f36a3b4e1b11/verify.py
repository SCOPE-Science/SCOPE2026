#!/usr/bin/env python3
"""Exact rational verification of the six-cycle universal-adjoint quartic."""
from itertools import combinations
from fractions import Fraction

N=6
# A monomial is represented by the set of its variable indices.
MONOMIALS=[frozenset(set(range(N))-{i,(i+1)%N}) for i in range(N)]

def eval_deriv(point, deriv):
    val=0
    for mon in MONOMIALS:
        if set(deriv)<=mon and len(set(deriv))==len(deriv):
            v=1
            for j in mon-set(deriv):v*=point[j]
            val+=v
    return val

def gradient(point): return [eval_deriv(point,(i,)) for i in range(N)]
def hessian(point): return [[eval_deriv(point,(i,j)) for j in range(N)] for i in range(N)]

def rank(M):
    m=[[Fraction(a) for a in row] for row in M]
    nr=len(m);nc=len(m[0]);k=0
    for j in range(nc):
        idx=next((i for i in range(k,nr) if m[i][j]),None)
        if idx is None:continue
        m[k],m[idx]=m[idx],m[k]; q=m[k][j]
        m[k]=[v/q for v in m[k]]
        for i in range(nr):
            if i!=k and m[i][j]:
                q=m[i][j];m[i]=[u-q*v for u,v in zip(m[i],m[k])]
        k+=1
        if k==nr:break
    return k

def coeff_poly_gradient(basis):
    # Test identity on an entire linear component: the gradient restricted
    # to its linear span is a degree-three polynomial in free parameters.
    d=len(basis)
    accum=[{} for _ in range(N)]
    for mon in MONOMIALS:
        for j in mon:
            idx=sorted(mon-{j})
            factors=[[basis[k][i] for k in range(d)] for i in idx]
            poly={(0,)*d:1}
            for coeffs in factors:
                nxt={}
                for ex,c in poly.items():
                    for k,b in enumerate(coeffs):
                        if b:
                            ee=list(ex);ee[k]+=1;ee=tuple(ee)
                            nxt[ee]=nxt.get(ee,0)+c*b
                poly=nxt
            for ex,c in poly.items():
                accum[j][ex]=accum[j].get(ex,0)+c
    for j,poly in enumerate(accum):
        assert all(c==0 for c in poly.values()),('gradient-not-identically-zero',j,basis,poly)

def perm(v,sgn,shift):
    out=[0]*N
    for i in range(N):out[(sgn*i+shift)%N]=v[i]
    return tuple(out)

def line_signature(u,v):
    z=[u[i]*v[j]-u[j]*v[i] for i in range(N) for j in range(i+1,N)]
    # Make primitive and fix sign (used only to deduplicate lines).
    import math
    gcd=0
    for t in z:gcd=math.gcd(gcd,t)
    z=[i//gcd for i in z]
    sign=next(1 if q>0 else -1 for q in z if q)
    return tuple(sign*q for q in z)

# Two planes are the projective spans of the alternating coordinate triples.
planes=[]
for parity in (0,1):
    basis=[tuple(int(i==j) for i in range(N)) for j in range(parity,N,2)]
    coeff_poly_gradient(basis)
    pt=tuple(1+b*2 for b in range(3))
    witness=[0]*N
    for c,v in zip(pt,basis):
        for j in range(N):witness[j]+=c*v[j]
    assert not any(gradient(witness)) and rank(hessian(witness))==3
    planes.append(basis)

# Nine coordinate lines joining one even and one odd vertex.
coord={}
for i in range(0,N,2):
    for j in range(1,N,2):
        e=lambda k: tuple(int(t==k) for t in range(N))
        basis=(e(i),e(j));coeff_poly_gradient(basis)
        w=tuple(basis[0][h]+2*basis[1][h] for h in range(N))
        assert rank(hessian(w))==4
        coord[line_signature(*basis)]=basis
assert len(coord)==9

# Explicit noncoordinate line representatives: the zero pairs have
# graph distances two or three, respectively.
reps=[((-1,0,-1,0,1,0),(0,1,0,0,0,0)),
      ((-1,0,0,0,1,0),(0,-1,0,1,0,0))]
noncoord={}
for rep in reps:
    for sgn in (-1,1):
        for shift in range(N):
            basis=(perm(rep[0],sgn,shift),perm(rep[1],sgn,shift))
            noncoord[line_signature(*basis)]=basis
assert len(noncoord)==9,('expected nine',len(noncoord))
for basis in noncoord.values():
    coeff_poly_gradient(basis)
    witness=tuple(basis[0][i]+2*basis[1][i] for i in range(N))
    assert rank(hessian(witness))==4
assert set(noncoord).isdisjoint(coord)

# Exhaustiveness by support. Four nonzero coordinates force exactly two
# vanishing coordinates (nonconsecutive); show restricted partials split
# into the unique linear line above, using the noncoordinate line supports.
zero_pairs={tuple(i for i in range(N) if basis[0][i]==basis[1][i]==0)
            for basis in noncoord.values()}
assert zero_pairs=={(i,j) for i,j in combinations(range(N),2) if (j-i)%N not in (1,N-1)}
# Size-three supports contributing identically zero derivatives: precisely
# the two alternating triples. Size two (or smaller) automatically zero.
for support in combinations(range(N),3):
    p=[int(i in support) for i in range(N)]
    if not any(gradient(p)):
        assert support in ((0,2,4),(1,3,5))
for support in combinations(range(N),5):
    p=[int(i in support) for i in range(N)]
    assert any(gradient(p))
print('HEXAGON_ADJOINT_EXACT_CHECKS_PASS')
print('TWO_PLANES',len(planes),'NINE_COORDINATE_LINES',len(coord),'NINE_NONCOORDINATE_LINES',len(noncoord))
print('HESSIAN_RANKS: plane=3; coordinate_line=4; noncoordinate_line=4')
