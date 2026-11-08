#!/usr/bin/env python3
"""Independent finite checks of a quadratic Walsh restriction formula.
Only Python standard library required. Finite calculations corroborate an analytic proof.
"""
from itertools import product, combinations
from math import comb
from fractions import Fraction

def rank_mod(rows, prime=1000000007):
    if not rows: return 0
    a = [[v % prime for v in row] for row in rows]
    m, d = len(a), len(a[0]); rk = 0
    for j in range(d):
        pos = next((i for i in range(rk,m) if a[i][j]),None)
        if pos is None: continue
        a[rk],a[pos] = a[pos],a[rk]
        pivot_inv=pow(a[rk][j],-1,prime)
        a[rk]=[(u*pivot_inv)%prime for u in a[rk]]
        for i in range(rk+1,m):
            if a[i][j]:
                fac=a[i][j]
                a[i]=[(v-fac*u)%prime for v,u in zip(a[i],a[rk])]
        rk+=1
        if rk==m: break
    return rk

def check(n,r):
    singles=[(i,) for i in range(n)]
    pairs=list(combinations(range(n),2))
    sub=[()]+singles+pairs
    rows=[]
    for x in product((1,-1),repeat=n):
        if sum(v==-1 for v in x)%3==r:
            rows.append([1]+[x[i] for (i,) in singles]+[x[i]*x[j] for i,j in pairs])
    cnt=len(rows); dim=len(sub); N=len(pairs)
    # Independently calculated exact Gram from every sampling point.
    raw=[[sum(row[i]*row[j] for row in rows) for j in range(dim)] for i in range(dim)]
    def mv(v):
        return [sum(Fraction(raw[i][j],cnt)*v[j] for j in range(dim)) for i in range(dim)]
    def eq_mv(v,expected):
        if mv(v)!=expected: raise AssertionError((n,r,'wrong invariant action'))
    # Expected Fourier moments via the exact combinatorial binomial formula.
    mu=[]
    for j in range(5):
        numerator=0
        for k in range(r,n+1,3):
            for ell in range(j+1):
                if 0<=k-ell<=n-j:
                    numerator+=(-1)**ell*comb(j,ell)*comb(n-j,k-ell)
        mu.append(Fraction(numerator,cnt))
    assert mu[0]==1 and mu[3]==-3*mu[1] and mu[4]==-3*mu[2]
    for i,I in enumerate(sub):
        for j,J in enumerate(sub):
            assert Fraction(raw[i][j],cnt)==mu[len(set(I)^set(J))]
    m0,m1,m2,m3,m4=mu
    b0=m0+2*(n-2)*m2+comb(n-2,2)*m4
    b1=m0+(n-4)*m2-(n-3)*m4
    b2=m0-2*m2+m4
    a=m0-m2
    # Three trivial vectors.
    e0=[1]+[0]*n+[0]*N
    e1=[0]+[1]*n+[0]*N
    e2=[0]+[0]*n+[1]*N
    eq_mv(e0,[m0]+[m1]*n+[m2]*N)
    eq_mv(e1,[n*m1]+[m0+(n-1)*m2]*n+[2*m1+(n-2)*m3]*N)
    eq_mv(e2,[N*m2]+[(n-1)*m1+comb(n-1,2)*m3]*n+[b0]*N)
    # Two standard vectors for the standard representation.
    ss=[1,-1]+[0]*(n-2)
    pp=[int(0 in I)-int(1 in I) for I in pairs]
    v=[0]+ss+[0]*N
    w=[0]+[0]*n+pp
    eq_mv(v,[0]+[a*vv for vv in ss]+[(m1-m3)*p for p in pp])
    eq_mv(w,[0]+[(n-2)*(m1-m3)*vv for vv in ss]+[b1*p for p in pp])
    # A nonzero irreducible quadratic harmonic direction.
    q={(0,1):1,(2,3):1,(0,2):-1,(1,3):-1}
    h=[0]+[0]*n+[q.get(I,0) for I in pairs]
    eq_mv(h,[b2*z for z in h])
    K0=sum(k%3==r for k in range(n+1))
    K1=sum(k%3==r for k in range(1,n))
    K2=sum(k%3==r for k in range(2,n-1))
    target=min(3,K0)+(n-1)*min(2,K1)+n*(n-3)//2*min(1,K2)
    assert rank_mod(rows)==target
    return cnt,target

if __name__=='__main__':
    tests=0
    for n in range(4,10):
        for r in range(3):
            check(n,r);tests+=1
    print('QUADRATIC_MOD3_WALSH_VERIFY_PASS exact_spectrum_blocks_and_modular_rank',tests)
