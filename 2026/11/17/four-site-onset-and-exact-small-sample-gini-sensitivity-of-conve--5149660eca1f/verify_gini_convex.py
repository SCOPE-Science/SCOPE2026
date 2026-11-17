#!/usr/bin/env python3
"""Finite exact-arithmetic certificates for convex-sequence Gini stability.
No third-party packages are needed. All enumerated fractions are exact.
"""
from fractions import Fraction as F
from itertools import combinations

EXPECTED = {2:F(1), 3:F(1), 4:F(10,9), 5:F(41,35),
            6:F(213,175), 7:F(191,153), 8:F(463,357)}

def inverse(a):
    n=len(a)
    b=[[F(v) for v in a[i]]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(k for k in range(j,n) if b[k][j])
        b[j],b[pivot]=b[pivot],b[j]
        val=b[j][j]
        b[j]=[v/val for v in b[j]]
        for i in range(n):
            if i!=j:
                val=b[i][j]
                if val:b[i]=[b[i][k]-val*b[j][k] for k in range(2*n)]
    return [line[n:] for line in b]

def active_projector(n,face):
    rows=[]
    for i in face:
        r=[F(0)]*n
        for j,v in [(i,1),(i+1,-2),(i+2,1)]:r[j]=F(v)
        rows.append(r)
    if not rows:return [[F(int(i==j)) for j in range(n)] for i in range(n)]
    m=len(rows)
    gram=[[sum(rows[i][k]*rows[j][k] for k in range(n)) for j in range(m)] for i in range(m)]
    ginv=inverse(gram)
    P=[]
    for i in range(n):
        r=[]
        for j in range(n):
            correction=sum(rows[a][i]*ginv[a][b]*rows[b][j] for a in range(m) for b in range(m))
            r.append(F(int(i==j))-correction)
        P.append(r)
    return P

def gini(v):
    n=len(v)
    return sum((abs(v[i]-v[j]) for i in range(n) for j in range(i+1,n)),F(0))

def face_gain(P):
    n=len(P)
    best=(F(0),None)
    # Subsets omitting the last coordinate give exactly one representative
    # of each nontrivial complementary pair; P*1=1 preserves Gini.
    for mask in range(1,1<<(n-1)):
        S=[i for i in range(n-1) if mask>>i & 1]
        k=len(S)
        q=[sum(P[i][j] for j in S) for i in range(n)]
        value=gini(q)/F(k*(n-k))
        if value>best[0]:best=(value,S)
    return best

def main():
    tests=0
    max_at={}
    for n in range(2,9):
        best=(F(0),None,None)
        for mask in range(1<<(n-2)):
            face=[i for i in range(n-2) if mask>>i&1]
            P=active_projector(n,face)
            assert all(sum(row)==1 for row in P)
            tests+=n
            assert all(P[i][j]==P[j][i] for i in range(n) for j in range(n))
            tests+=n*n
            assert all(sum(P[i][k]*P[k][j] for k in range(n))==P[i][j]
                       for i in range(n) for j in range(n))
            tests+=n*n
            gain,cut=face_gain(P)
            tests += (1<<(n-1))-1
            if gain>best[0]:best=gain,face,cut
        assert best[0]==EXPECTED[n],(n,best,EXPECTED[n])
        tests+=1
        max_at[n]=best
        print('EXACT n=',n,'faces=',1<<(n-2),'cut_reps=',(1<<(n-1))-1,
              'norm=',str(best[0]),'active=',best[1],'cut=',best[2])
    # An attained finite-distance four-site witness with strict complementarity.
    n=4
    P=active_projector(n,[0]);y=[F(0),F(0),F(0),F(1)]
    B=[F(1),F(-2),F(1),F(0)]
    a=[y[i]-B[i] for i in range(n)]
    eps=F(1,10)
    z=[a[i]+(eps if i==0 else F(0)) for i in range(n)]
    fit=[sum(P[i][j]*z[j] for j in range(n)) for i in range(n)]
    fit0=[sum(P[i][j]*a[j] for j in range(n)) for i in range(n)]
    def curvature(v,i):return v[i]-2*v[i+1]+v[i+2]
    assert fit0==y
    assert curvature(fit,0)==0 and curvature(fit,1)>0
    lam=-sum(B[i]*(z[i]-fit[i]) for i in range(n))/sum(t*t for t in B)
    assert lam>0 and all(fit[i]-z[i]==lam*B[i] for i in range(n))
    assert gini([fit[i]-fit0[i] for i in range(n)])==F(10,9)*gini([z[i]-a[i] for i in range(n)])
    tests+=5
    print('EXACT_FOUR_SITE_FINITE_WITNESS',a,z,fit,'ratio=10/9')
    # The fixed 3-site active face gives strict amplification in each n>=4.
    for n in range(4,31):
        P=active_projector(n,[0])
        q=[P[i][0] for i in range(n)]
        assert gini(q)/F(n-1)==F(4*n-6,3*(n-1))>1
        tests+=1
    print('GENERAL_EMBEDDED_FACE_RATIONAL_LOWER_FORMULA_PASS_N4_TO30')
    print('ALL_EXACT_CONVEX_GINI_CHECKS_PASS',tests)
if __name__=='__main__':main()
