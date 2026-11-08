#!/usr/bin/env python3
"""Exact binary plane quintic tangent-incidence census.

Requires Python 3.10+ and SymPy 1.14. The Groebner ideal-unit test is over
GF(2), hence certifies absence of geometric singularities, not merely
absence of singular points over selected finite extensions.
"""
import itertools
from collections import Counter, defaultdict
from sympy import Poly, groebner, symbols

MON = [(a, b, 5-a-b) for a in range(6) for b in range(6-a)]
IDX = {e:i for i,e in enumerate(MON)}
PTS = [p for p in itertools.product(range(2), repeat=3) if any(p)]
x, y = symbols('x y')


def polynomial(v, variables):
    return sum((variables[0]**a * variables[1]**b * variables[2]**c
                for i,(a,b,c) in enumerate(MON) if v & (1 << i)), 0)


def kernel_basis():
    rows = [sum(((p[0]**a * p[1]**b * p[2]**c) & 1) << i
                for i,(a,b,c) in enumerate(MON)) for p in PTS]
    pivots = []
    for j in range(21):
        k = next((i for i in range(len(pivots),7) if rows[i] >> j & 1), None)
        if k is None: continue
        rows[k], rows[len(pivots)] = rows[len(pivots)], rows[k]
        for i in range(7):
            if i != len(pivots) and rows[i] >> j & 1:
                rows[i] ^= rows[len(pivots)]
        pivots.append(j)
        if len(pivots) == 7: break
    assert len(pivots)==7
    basis=[]
    for j in range(21):
        if j in pivots: continue
        w=1 << j
        for i,k in enumerate(pivots):
            if rows[i] >> j & 1: w ^= 1 << k
        basis.append(w)
    assert len(basis)==14
    return basis


def all_filling():
    basis=kernel_basis()
    arr=[0] * (1 << 14)
    for i in range(1,len(arr)):
        lo=i & -i
        arr[i] = arr[i ^ lo] ^ basis[lo.bit_length()-1]
    assert len(set(arr)) == 1 << 14
    return set(arr)-{0}


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]^A[1][2]*A[2][1]) ^
            A[0][1]*(A[1][0]*A[2][2]^A[1][2]*A[2][0]) ^
            A[0][2]*(A[1][0]*A[2][1]^A[1][1]*A[2][0])) & 1


def multiply(p, q):
    out={}
    for u in p:
        for v in q:
            e=tuple(u[j]+v[j] for j in range(3))
            if e in out: del out[e]
            else: out[e]=1
    return out


def group_actions():
    matrices=[]
    for mask in range(512):
        A=[[mask >> (3*i+j)&1 for j in range(3)] for i in range(3)]
        if det3(A): matrices.append(A)
    assert len(matrices)==168
    actions=[]
    for A in matrices:
        linear=[{tuple(int(t==j) for t in range(3)):1
                 for j in range(3) if A[k][j]} for k in range(3)]
        columns=[]
        for e in MON:
            p={(0,0,0):1}
            for k in range(3):
                for _ in range(e[k]): p=multiply(p,linear[k])
            columns.append(sum(1 << IDX[w] for w in p))
        actions.append(columns)
    return matrices,actions


def apply(v, cols):
    out=0
    while v:
        b=v & -v
        out ^= cols[b.bit_length()-1]
        v ^= b
    return out


def affine(v, chart):
    coordinates = ([1,x,y],[x,1,y],[x,y,1])[chart]
    return Poly(polynomial(v,coordinates),x,y,modulus=2)


def is_unit(G):
    return len(G.polys)==1 and G.polys[0].is_one


def smooth(v):
    for chart in range(3):
        f=affine(v,chart)
        A=groebner([f.as_expr(), f.diff(x).as_expr(), f.diff(y).as_expr()],
                   x,y,order='grevlex',modulus=2)
        if not is_unit(A): return False
    return True


def smooth_via_homogeneous_gradient(v):
    # Independent algebraic formulation: in degree 5, Euler's identity
    # implies f = X F_X + Y F_Y + Z F_Z in characteristic 2.
    homogeneous=[]
    for k in range(3):
        terms=[]
        for i,e in enumerate(MON):
            if v & (1<<i) and (e[k]&1):
                ee=list(e);ee[k]-=1;terms.append(tuple(ee))
        homogeneous.append(terms)
    for chart in range(3):
        coordinates=([1,x,y],[x,1,y],[x,y,1])[chart]
        derivatives=[sum((coordinates[0]**a * coordinates[1]**b *
                          coordinates[2]**c for a,b,c in terms),0)
                     for terms in homogeneous]
        G=groebner(derivatives,x,y,order='lex',modulus=2)
        if not is_unit(G):return False
    return True


def grad(v,p):
    v3=[]
    for axis in range(3):
        s=0
        for i,e in enumerate(MON):
            if not (v >> i & 1) or not (e[axis] & 1):continue
            ee=list(e);ee[axis]-=1
            s ^= (p[0]**ee[0]*p[1]**ee[1]*p[2]**ee[2])&1
        v3.append(s)
    return tuple(v3)


def tangent_profile(v):
    vals=[grad(v,p) for p in PTS]
    if any(j==(0,0,0) for j in vals):return None
    return Counter(vals)


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3))&1
             for j in range(3)] for i in range(3)]


def matrix_order(A):
    I=[[int(i==j) for j in range(3)] for i in range(3)]
    M=I
    for k in range(1,9):
        M=matmul(M,A)
        if M==I:return k
    raise AssertionError('not invertible')



REPS=[]

IRR={1:3,2:7,3:11,4:19,5:37,6:67}
def mul(a,b,n,pol):
 out=0
 while b:
  if b&1:out^=a
  b>>=1;a<<=1
  if a>>n:a^=pol
 return out

def count(v,n):
 q=1<<n;pol=IRR[n]
 power=[[1]*6 for _ in range(q)]
 for x in range(q):
  for j in range(1,6):power[x][j]=mul(power[x][j-1],x,n,pol)
 mons=[e for i,e in enumerate(MON) if v>>i &1]
 ans=0
 for x in range(q):
  for y in range(q):
   r=0
   for a,b,c in mons:
    if c==0:r^=mul(power[x][a],power[y][b],n,pol)
    else:r^=mul(power[x][a],power[y][b],n,pol)
   if not r:ans+=1
 for x in range(q):
  r=0
  for a,b,c in mons:
   if c==0:r^=power[x][a]
  if not r:ans+=1
 if any(a==5 and b==0 and c==0 for a,b,c in mons):pass
 else:ans+=1
 return ans

def coeffs(ns):
 a=[1]
 for k in range(1,7):
  t=sum(a[k-i]*(ns[i-1]-2**i-1) for i in range(1,k+1))
  assert t%k==0,(k,t)
  a.append(t//k)
 return a+[2**(6-k)*a[k] for k in range(5,-1,-1)]


from sympy import GF as symGF
from sympy import Poly as symPoly

def main():
    from collections import Counter
    from sympy import Symbol
    T=Symbol('T')
    for n,f in IRR.items():
        u=Symbol('u')
        polynomial_mod=sum(u**i for i in range(n+1) if (f>>i)&1)
        assert symPoly(polynomial_mod,u,modulus=2).is_irreducible
    forms=all_filling()
    matrices,actions=group_actions()
    remain=set(forms); orbits=[]
    while remain:
        v=min(remain)
        orbit={apply(v,A) for A in actions}
        assert orbit<=remain
        remain-=orbit
        orbits.append((v,len(orbit)))
    assert len(orbits)==139
    good=[]
    for v,sz in orbits:
        s=smooth(v)
        assert s==smooth_via_homogeneous_gradient(v)
        if s:good.append((v,sz))
    assert len(good)==10 and sum(sz for v,sz in good)==1512
    result=[]
    for v,sz in good:
        ns=[count(v,n) for n in range(1,7)]
        L=coeffs(ns)
        assert len(L)==13 and L[12]==64
        result.append((v,sz,ns,L))
    assert len({tuple(v[-1]) for v in result})==10
    assert sum(sz for _,sz,_,_ in result)==1512
    assert len({tuple(ns) for _,_,ns,_ in result})==10
    # Independent projective enumeration on all nonzero vectors, retaining
    # unique triples by first nonzero coordinate normalized to 1.
    for v,_,ns,_ in result:
        for n in (1,2,3,6):
            q=1<<n;mod=IRR[n]
            powers=[[1]*6 for _ in range(q)]
            for a in range(q):
                for k in range(1,6):powers[a][k]=mul(powers[a][k-1],a,n,mod)
            terms=[(a,b,c) for i,(a,b,c) in enumerate(MON) if v>>i&1]
            answer=0
            for z in (0,1):
                if z:
                    pts=((a,b,1) for a in range(q) for b in range(q))
                else:
                    pts=((a,1,0) for a in range(q))
                for a,b,c in pts:
                    t=0
                    for x,y,w in terms:
                        t^=mul(mul(powers[a][x],powers[b][y],n,mod),powers[c][w],n,mod)
                    answer+=(t==0)
            p=(1,0,0);t=0
            for x,y,w in terms:
                t^=mul(mul(powers[1][x],powers[0][y],n,mod),powers[0][w],n,mod)
            answer+=(t==0)
            assert answer==ns[n-1],(v,n,answer,ns[n-1])
    for r in result: print(r)
    print('F2_PLANE_FILLING_QUINTIC_TEN_DISTINCT_ZETA_PASS')

if __name__ == '__main__':main()
