"""Exact certificates for Euclidean distances from the second hypersimplex to cycle edge polytopes."""
from fractions import Fraction as F
from itertools import combinations


def cycle_data(n, i, j):
    assert n >= 3 and 0 <= i < j < n
    ds = min(j-i, n-(j-i))
    w = [F(0) for _ in range(n)]
    if ds == 1:
        if j == i+1:
            w[i]=F(1)
        else:
            w[j]=F(1)
        target = F(0)
    elif n == 4:
        w = [F(1,4)] * n
        target = F(1)
    elif ds == 2:
        a,b = i,j
        if (j-i) % n != 2:
            a,b = j,i
        # b = a + 2 modulo n
        assert (b-a) % n == 2
        w[(a-1)%n]=F(1,3)
        w[a%n]=F(1,6)
        w[(a+1)%n]=F(1,6)
        w[(a+2)%n]=F(1,3)
        target=F(5,6)
    else:
        assert n>=6 and ds>=3
        for a in (i,j):
            w[(a-1)%n]=F(1,4)
            w[a]=F(1,4)
        target=F(3,4)
    p = [w[k-1]+w[k] for k in range(n)]
    x = [F(int(k in (i,j))) for k in range(n)]
    r = [x[k]-p[k] for k in range(n)]
    d2 = sum(t*t for t in r)
    assert sum(w)==1 and min(w)>=0 and d2==target,(n,i,j,d2,target)
    # Variational certificate: <x-p, u_e-p> <= 0 for every cycle edge u_e.
    c=sum(r[k]*p[k] for k in range(n))
    for k in range(n):
        g=r[k]+r[(k+1)%n]
        assert g<=c,(n,i,j,k,g,c)
        if w[k]: assert g==c,(n,i,j,k,g,c)
    return d2,tuple(r)


def check_exact():
    cases=0
    for n in range(3,41):
        far=[]; scores=set(); residuals=[]
        for i,j in combinations(range(n),2):
            d,r=cycle_data(n,i,j)
            cases+=1; scores.add(d)
            if n>=5 and d==F(5,6):
                far.append((i,j));residuals.append(r)
            if n==4 and d==1:
                far.append((i,j));residuals.append(r)
        if n==3: assert scores=={F(0)}
        if n==4: assert scores=={F(0),F(1)} and len(far)==2
        if n==5: assert scores=={F(0),F(5,6)} and len(far)==5
        if n>=6: assert scores=={F(0),F(5,6),F(3,4)} and len(far)==n
        assert len(residuals)==len(set(residuals))
    return cases


def check_numerical():
    import numpy as np
    from scipy.optimize import minimize
    tested=0
    max_gap=0.
    for n in range(3,12):
        A = np.zeros((n,n))
        for e in range(n):
            A[e,e]=1; A[(e+1)%n,e]=1
        pairs=list(combinations(range(n),2))
        for i,j in pairs:
            x=np.zeros(n);x[i]=x[j]=1
            def f(w):
                r=A@w-x
                return float(r@r)
            def jac(w): return 2*A.T@(A@w-x)
            opt=minimize(f, np.full(n,1/n),method='SLSQP',jac=jac,bounds=[(0,1)]*n, constraints={'type':'eq','fun':lambda w:w.sum()-1,'jac':lambda w:np.ones(n)},options={'ftol':1e-12,'maxiter':300})
            assert opt.success,(n,i,j,opt.message)
            exact=float(cycle_data(n,i,j)[0]); gap=abs(opt.fun-exact)
            max_gap=max(max_gap,gap)
            assert gap<1e-8,(n,i,j,opt.fun,exact)
            tested+=1
    return tested,max_gap

if __name__=='__main__':
    a=check_exact()
    b,g=check_numerical()
    print('CYCLE_HYPERSIMPLEX_PASS exact_pairs=%d independent_qps=%d max_squared_gap=%.3g farthest_residuals_distinct=PASS' %(a,b,g))
