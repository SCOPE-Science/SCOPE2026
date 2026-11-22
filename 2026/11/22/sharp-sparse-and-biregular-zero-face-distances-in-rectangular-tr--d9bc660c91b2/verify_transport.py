"""Finite exact checks of rectangular transportation face-distance bounds.

The identities for all sizes require the accompanying mathematical proof.
Python 3 standard library only for exact tests; numpy/scipy optional for numerical tests.
"""
from fractions import Fraction as Q
from itertools import combinations
import random


def proj(m,n,F):
    F=set(F); k=len(F)
    r=[sum((i,j) in F for j in range(n)) for i in range(m)]
    c=[sum((i,j) in F for i in range(m)) for j in range(n)]
    P=[[Q(int((i,j) in F))-Q(r[i],n)-Q(c[j],m)+Q(k,m*n) for j in range(n)] for i in range(m)]
    G=sum(z*z for row in P for z in row)
    expect=Q(k)-sum((Q(t*t,n) for t in r),Q(0))-sum((Q(t*t,m) for t in c),Q(0))+Q(k*k,m*n)
    assert G==expect
    return P,G,r,c


def validate_face(m,n,F,X):
    F=set(F)
    assert all(z>=0 for row in X for z in row)
    assert all(X[i][j]==0 for i,j in F)
    assert all(sum(X[i])==Q(1,m) for i in range(m))
    assert all(sum(X[i][j] for i in range(m))==Q(1,n) for j in range(n))
    return sum((X[i][j]-Q(1,m*n))**2 for i in range(m) for j in range(n))


def matching_case(m,n,k):
    F={(i,i) for i in range(k)}
    P,G,r,c=proj(m,n,F)
    D=(m-1)*(n-1)+k-1
    X=[[Q(1,m*n)-P[i][j]/D for j in range(n)] for i in range(m)]
    d2=validate_face(m,n,F,X)
    assert d2==Q(k,m*n*D), (m,n,k,d2)
    assert G==Q(k*D,m*n)


def regular_case(m,n,k):
    r=k//m; s=k//n
    F={(i,(i*r+t)%n) for i in range(m) for t in range(r)}
    assert len(F)==k
    P,G,rd,cd=proj(m,n,F)
    assert rd==[r]*m and cd==[s]*n
    X=[[Q(0) if (i,j) in F else Q(1,m*n-k) for j in range(n)] for i in range(m)]
    d2=validate_face(m,n,F,X)
    assert d2==Q(k,m*n*(m*n-k))
    assert G==Q(k*(m*n-k),m*n)


def finite_optimization_checks():
    try:
        import numpy as np
        from scipy.optimize import linprog, minimize
    except ImportError:
        return 0
    random.seed(23062023)
    tested=0
    for m,n in [(2,3),(2,4),(3,4),(3,5),(4,5)]:
        cells=[(i,j) for i in range(m) for j in range(n)]
        for k in range(1,min(m*n-1,7)+1):
            sets=list(combinations(cells,k)) if m*n<=6 else [tuple(random.sample(cells,k)) for _ in range(50)]
            for pat in sets:
                F=set(pat)
                free=[z for z in cells if z not in F]
                A=np.zeros((m+n,len(free)))
                for h,(i,j) in enumerate(free):A[i,h]=1;A[m+j,h]=1
                b=np.array([1/m]*m+[1/n]*n)
                x0=linprog(np.zeros(len(free)),A_eq=A,b_eq=b,bounds=(0,None),method='highs')
                if not x0.success:continue
                def obj(x):return float(np.sum((x-1/(m*n))**2)+k/(m*n)**2)
                fit=minimize(obj,x0.x,jac=lambda x:2*(x-1/(m*n)),bounds=[(0,None)]*len(free),constraints=[{'type':'eq','fun':lambda x:A@x-b,'jac':lambda x:A}],method='SLSQP',options={'ftol':1e-11,'maxiter':250})
                assert np.max(np.abs(A@fit.x-b))<1e-6
                P,G,r,c=proj(m,n,F)
                low=float(Q(k*k,m*m*n*n)/G)
                assert obj(fit.x)>=low-2e-7, (m,n,F,low,obj(fit.x))
                if k<=min(m,n):
                    D=(m-1)*(n-1)+k-1
                    floor=k/(m*n*D)
                    assert obj(fit.x)>=floor-2e-7
                    if any(t>1 for t in r+c):
                        assert obj(fit.x)>floor+1e-9
                if k%m==0 and k%n==0:
                    floor=k/(m*n*(m*n-k))
                    assert obj(fit.x)>=floor-2e-7
                tested+=1
    return tested


def main():
    exact=0; regular=0
    for m in range(2,16):
        for n in range(2,16):
            if m==n:continue
            for k in range(1,min(m,n)+1):
                matching_case(m,n,k); exact+=1
            for k in range(1,m*n):
                if k%m==0 and k%n==0:
                    regular_case(m,n,k); regular+=1
    numeric=finite_optimization_checks()
    print('RECTANGULAR_TRANSPORT_FACE_PASS',f'exact_matching={exact}',f'exact_biregular={regular}',f'numerical_feasible_patterns={numeric}')

if __name__=='__main__':main()
