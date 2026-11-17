#!/usr/bin/env python3
"""Exact small-instance checks for two-clique polar Lipschitz covariance.

Uses only Python's standard library. Each order chamber is integrated by
Dirichlet second moments, independently of the spectral formulas.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def clique_anchor_moments(a):
    """Integrate anchored coordinates by all a! order chambers, exactly."""
    p=a-1
    m=[[F(0) for _ in range(p)] for _ in range(p)]
    mu=[F(0) for _ in range(p)]
    for order in permutations(range(a)):
        rank=[0]*a
        for k,v in enumerate(order):rank[v]=k
        # Index 0 is the shared hub. Remaining coordinates = position - hub.
        w=[[int(k<rank[i])-int(k<rank[0]) for k in range(p)]
           for i in range(1,a)]
        sums=[sum(v) for v in w]
        for i in range(p):
            mu[i]+=F(sums[i],a*factorial(a))
            for j in range(p):
                m[i][j]+=F(sums[i]*sums[j]+sum(x*y for x,y in zip(w[i],w[j])),a*(a+1)*factorial(a))
    assert all(u == 0 for u in mu), (a,mu)
    return m


def project_zero_sum(D):
    n=len(D)
    rows=[sum(r) for r in D]
    total=sum(rows)
    return [[D[i][j]-F(rows[i]+rows[j],n)+F(total,n*n)
             for j in range(n)] for i in range(n)]


def trace_square(C):
    return sum(C[i][j]*C[j][i] for i in range(len(C))
               for j in range(len(C)))


def run():
    cm={}
    for a in range(2,7):
        cm[a]=clique_anchor_moments(a)
        c=F(a+2,12*a)
        for i in range(a-1):
            for j in range(a-1):
                assert cm[a][i][j] == c*(1+(i==j)), ('clique',a,i,j,cm[a][i][j])
        # Every Weyl chamber has the same volume, 1/(a-1)!.
        assert F(factorial(a),factorial(a-1))==a
    checked_entries=0;checked_pairs=0
    for a in range(2,7):
        for b in range(2,7):
            n=a+b-1;p=a-1;q=b-1
            D=[[F(0) for _ in range(n)] for _ in range(n)]
            for i in range(p):
                for j in range(p):D[i][j]=cm[a][i][j]
            for i in range(q):
                for j in range(q):D[p+1+i][p+1+j]=cm[b][i][j]
            C=project_zero_sum(D)
            ca=F(a+2,12*a);cb=F(b+2,12*b)
            # Independent closed-form matrix prediction from clique symmetry.
            D_expected=[[F(0) for _ in range(n)] for _ in range(n)]
            for i in range(p):
                for j in range(p):D_expected[i][j]=ca*(1+(i==j))
            for i in range(q):
                for j in range(q):D_expected[p+1+i][p+1+j]=cb*(1+(i==j))
            C_expected=project_zero_sum(D_expected)
            assert C==C_expected,('projected covariance',a,b)
            # Verify block contrasts using exact matrix multiplication.
            for m,c,st in ((p,ca,0),(q,cb,p+1)):
                for k in range(1,m):
                    v=[F(0)]*n;v[st]=F(1);v[st+k]=F(-1)
                    got=[sum(C[i][j]*v[j] for j in range(n)) for i in range(n)]
                    assert got==[c*x for x in v],(a,b,m,k)
            t=sum(C[i][i] for i in range(n))-(a-2)*ca-(b-2)*cb
            tr2=trace_square(C)-(a-2)*ca**2-(b-2)*cb**2
            det=(t*t-tr2)/2
            assert t==F(a*b+a+b,6*n),('trace',a,b,t)
            assert det==F((a+2)*(b+2),144*n),('det',a,b,det)
            assert all(sum(C[i])==0 for i in range(n))
            checked_entries+=n*n;checked_pairs+=1
    # Exact monotonicity of the eigenratio at fixed dimension:
    # compare gamma=(trace)^2/det, which is strictly increasing in ab.
    count=0
    for n in range(3,90):
        ratios=[]
        for a in range(2,(n+1)//2+1):
            b=n+1-a
            k=a*b
            r=F(4*(k+n+1)**2,n*(k+2*n+6))
            ratios.append(r)
        assert all(x<y for x,y in zip(ratios,ratios[1:])),('balance',n)
        count+=len(ratios)
    print('TWO_CLIQUE_POLAR_COVARIANCE_CHECKS_PASSED',
          'clique_sizes=5','ordered_pairs='+str(checked_pairs),
          'exact_matrix_entries='+str(checked_entries),
          'balance_profiles='+str(count))

if __name__=='__main__':run()
