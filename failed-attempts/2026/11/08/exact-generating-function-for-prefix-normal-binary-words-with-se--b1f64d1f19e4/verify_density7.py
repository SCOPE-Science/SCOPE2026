"""Exact algebraic and direct-word verification for the density-seven prefix-normal generating function.

Requires Python 3 and sympy. No network or external data are used.
"""
import itertools
from collections import defaultdict
from functools import lru_cache
from math import comb, factorial, gcd
from fractions import Fraction
import sympy as S

z = S.Symbol('z')
RAYS = (
    (0,0,0,0,1), (0,0,0,1,0), (0,0,1,0,0),
    (0,1,0,0,1), (0,1,0,1,0), (0,1,1,0,0),
    (1,0,1,0,1), (1,0,1,1,0), (1,1,0,1,1),
    (1,1,0,2,0), (1,1,1,0,1), (2,1,1,1,1), (2,1,1,2,0),
)
A = S.Matrix([
    [1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1],
    [-1,1,1,0,0], [-1,0,1,1,0], [-1,0,0,1,1], [-1,-1,1,1,1],
])

def primitive(v):
    d = S.ilcm(*(x.q for x in v))
    ints = [int(x*d) for x in v]
    g = 0
    for a in ints: g = gcd(g, a)
    return tuple(x//g for x in ints)

def computed_extreme_rays():
    ans=set()
    for rows in itertools.combinations(range(A.rows),4):
        ker=A[list(rows),:].nullspace()
        if len(ker)!=1: continue
        v=primitive(ker[0]); v2=tuple(-t for t in v)
        for t in (v,v2):
            if all(y>=0 for y in A*S.Matrix(t)): ans.add(t)
    return tuple(sorted(ans))

@lru_cache(None)
def facets(face):
    V = S.Matrix.hstack(*(S.Matrix(RAYS[i]) for i in face))
    rank = V.rank()
    basis=[]
    for i in face:
        Q=S.Matrix.hstack(*(S.Matrix(RAYS[k]) for k in basis+[i]))
        if Q.rank()>len(basis):basis.append(i)
        if len(basis)==rank:break
    B=S.Matrix.hstack(*(S.Matrix(RAYS[k]) for k in basis))
    coord={i:B.gauss_jordan_solve(S.Matrix(RAYS[i]))[0] for i in face}
    out=set()
    for sub in itertools.combinations(face,rank-1):
        ker=S.Matrix.hstack(*(coord[i] for i in sub)).T.nullspace()
        if len(ker)!=1: continue
        vec=ker[0]
        signs=[vec.dot(coord[i]) for i in face]
        if all(v>=0 for v in signs) or all(v<=0 for v in signs):
            f=tuple(i for i in face if vec.dot(coord[i])==0)
            if 0<len(f)<len(face) and S.Matrix.hstack(*(S.Matrix(RAYS[i]) for i in f)).rank()==rank-1:
                out.add(f)
    return tuple(sorted(out))

@lru_cache(None)
def pulling(face):
    if len(face)==1:return (face,)
    root=min(face)
    return tuple(tuple(sorted((root,)+simp))
                 for f in facets(face) if root not in f
                 for simp in pulling(f))

def halfopen_terms():
    all_faces=tuple(range(len(RAYS)))
    simps=pulling(all_faces)
    assert len(simps)==15 and len(set(simps))==15
    assert len(facets(all_faces))==9
    incidence=defaultdict(list)
    for j,s in enumerate(simps):
        for k in range(5):incidence[tuple(x for t,x in enumerate(s) if t!=k)].append(j)
    assert len(incidence)==55
    assert sorted(map(len,incidence.values())).count(1)==35
    assert sorted(map(len,incidence.values())).count(2)==20
    q=S.Matrix([7,11,13,17,19])
    out=[]; determinants=[]
    for simplex in simps:
        M=S.Matrix.hstack(*(S.Matrix(RAYS[i]) for i in simplex))
        D=abs(int(M.det())); assert D in (1,2)
        determinants.append(D)
        U=M.inv(); beta=U*q
        assert all(v!=0 for v in beta)
        strict=[int(bool(v<0)) for v in beta]
        p=M*S.Matrix(strict)
        exps=[int(sum(p))]
        if D==2:
            e=next(S.eye(5)[:,j] for j in range(5)
                   if any(v.q!=1 for v in U*S.eye(5)[:,j]))
            frac=[v-S.floor(v) for v in U*e]
            p2=M*S.Matrix([frac[j]+int(strict[j] and frac[j]==0) for j in range(5)])
            assert all(v.q==1 for v in p2)
            exps.append(int(sum(p2)))
        deg=[sum(RAYS[i]) for i in simplex]
        out.append((simplex, tuple(deg), tuple(exps), tuple(strict)))
    assert sorted(set(determinants))==[1,2]
    assert determinants.count(2)==5
    return out

COEFF=(1,3,9,17,35,48,76,85,108,103,108,85,76,48,35,17,9,3,1)
P=sum(c*z**i for i,c in enumerate(COEFF))
TARGET=z**7*P/((1-z)*(1-z**3)*(1-z**4)**2*(1-z**6)**3)

def gf_coeffs(N):
    num,den=S.fraction(S.cancel(TARGET))
    A=[int(S.Poly(num,z).nth(i)) for i in range(N+1)]
    D=S.Poly(den,z)
    dd=[int(D.nth(i)) for i in range(D.degree()+1)]
    out=[]
    for i in range(N+1):
        a=A[i]-sum(dd[k]*out[i-k] for k in range(1,min(i,len(dd)-1)+1))
        assert a%dd[0]==0
        out.append(a//dd[0])
    return out

def direct_prefix_normal(pos,n):
    bits=[0]*n
    for j in pos:bits[j]=1
    acc=[0]
    for v in bits:acc.append(acc[-1]+v)
    return all(acc[j+length]-acc[j] <= acc[length]
               for length in range(1,n+1) for j in range(n-length+1))

def direct_counts(nmax):
    return {n:sum(direct_prefix_normal(pos,n)
                  for pos in itertools.combinations(range(n),7)) for n in range(7,nmax+1)}

def gap_counts(nmax):
    out={}
    for n in range(7,nmax+1):
        total=0
        for a in range((n-7)//6+1):
            limit=n-7-6*a
            for b in range(limit+1):
                for c in range(limit-b+1):
                    for d in range(limit-b-c+1):
                        for e in range(limit-b-c-d+1):
                            maximum=min(b+c,c+d,d+e,c+d+e-b,limit-b-c-d-e)
                            if maximum>=0: total+=maximum+1
        out[n]=total
    return out

def main():
    assert computed_extreme_rays()==RAYS
    terms=halfopen_terms()
    cone_series=sum(sum(z**e for e in exps)/S.prod(1-z**d for d in deg)
                    for _,deg,exps,_ in terms)
    assert S.cancel(cone_series - P/((1-z**3)*(1-z**4)**2*(1-z**6)**2))==0
    assert sum(COEFF)==867
    assert S.Rational(sum(COEFF),3*4**2*6**3*factorial(6))==S.Rational(289,2488320)
    a=gf_coeffs(36)
    for n,c in direct_counts(20).items():assert c==a[n],(n,c,a[n])
    for n,c in gap_counts(27).items():assert c==a[n],(n,c,a[n])
    print('EXACT_CONE_G.F._OK; 13 rays, 9 facets, 15 pulling simplices')
    print('DIRECT_WORD_COUNTS_OK; lengths 7..20')
    print('INDEPENDENT_GAP_COUNTS_OK; lengths 7..27')
    print('LEADING_CONSTANT_OK; 289/2488320')
    print('COUNTS_7_TO_20:',[a[n] for n in range(7,21)])

if __name__=='__main__':main()
