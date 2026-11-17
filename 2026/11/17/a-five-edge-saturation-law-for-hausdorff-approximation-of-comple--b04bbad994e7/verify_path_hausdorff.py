#!/usr/bin/env python3
"""Exact projection certificates and independent small-order numerical checks.

Uses standard-coordinate Euclidean metric throughout. Requires Python 3;
optional numerical stage uses NumPy/SciPy when present.
"""
from fractions import Fraction as F


def edges_to_vector(a):
    n = len(a) + 1
    y = [F(0) for _ in range(n)]
    for k, t in enumerate(a):
        y[k] += t
        y[k+1] -= t
    return y


def residual(a, i, j):
    y = edges_to_vector(a)
    r = [-v for v in y]
    r[i] += 1
    r[j] -= 1
    return r


def kkt(a, i, j):
    r = residual(a,i,j)
    if sum(map(abs,a)) != 1:
        raise AssertionError('wrong l1 norm')
    g = [r[k]-r[k+1] for k in range(len(a))]
    act = [k for k in range(len(a)) if a[k] != 0]
    lam = g[act[0]] if a[act[0]]>0 else -g[act[0]]
    assert lam >= 0
    for k in range(len(a)):
        if a[k] > 0: assert g[k] == lam, (k,g[k],lam)
        elif a[k] < 0: assert g[k] == -lam, (k,g[k],lam)
        else: assert abs(g[k]) <= lam, (k,g[k],lam)
    return sum(x*x for x in r)


def exact_certificate(n,i,j):
    assert 0 <= i < j < n
    d = j-i
    a = [F(0) for _ in range(n-1)]
    if i == 0 and j == n-1 and n <= 5:
        patterns = {3:[F(1,2),F(1,2)],
                    4:[F(2,5),F(1,5),F(2,5)],
                    5:[F(2,5),F(1,10),F(1,10),F(2,5)]}
        a = patterns[n]
    elif d >= 5:
        if i == 0:
            a[0]=F(5,12)
            a[1]=F(1,12)
        else:
            a[i-1]=-F(1,4)
            a[i]=F(1,4)
        if j == n-1:
            a[n-3]=F(1,12)
            a[n-2]=F(5,12)
        else:
            a[j-1]=F(1,4)
            a[j]=-F(1,4)
    else:
        return None
    dist2 = kkt(a,i,j)
    expected = F(11,12) if i==0 and j==n-1 and n>=6 else (
      F(5,6) if (i==0) != (j==n-1) else F(3,4)) if d>=5 else {
          3:F(1,2),4:F(4,5),5:F(9,10)}[n]
    assert dist2 == expected, (n,i,j,dist2,expected)
    return dist2, a


def upper_candidate(n,i,j):
    d = j-i
    a = [F(0) for _ in range(n-1)]
    if d==1:
        a[i] = F(1)
    elif d==2:
        a[i]=a[i+1]=F(1,2)
    elif d==3:
        for k,t in enumerate([F(2,5),F(1,5),F(2,5)]):a[i+k]=t
    elif d>=4:
        if i==0 and j==n-1:
            assert d>=5
        elif i==0:
            a[0]=F(5,12); a[1]=F(1,12)
            a[j-1]=F(1,4); a[j]=-F(1,4)
        elif j==n-1:
            a[i-1]=-F(1,4);a[i]=F(1,4)
            a[n-3]=F(1,12);a[n-2]=F(5,12)
        else:
            a[i-1]=-F(1,4);a[i]=F(1,4)
            a[j-1]=F(1,4);a[j]=-F(1,4)
    assert sum(map(abs,a)) <= 1
    r = residual(a,i,j)
    return sum(x*x for x in r), a


def verify_exact(maxn=40):
    count=0; long_cases=0; upper_cases=0
    for n in range(3,maxn+1):
        top=F(1,2) if n==3 else F(4,5) if n==4 else F(9,10) if n==5 else F(11,12)
        assert exact_certificate(n,0,n-1)[0]==top
        for i in range(n):
            for j in range(i+1,n):
                count += 1
                if j-i>=5:
                    d2,_=exact_certificate(n,i,j)
                    long_cases += 1
                    assert d2<=top
                    assert (d2==top)==(i==0 and j==n-1)
                elif not (i==0 and j==n-1):
                    d2,_=upper_candidate(n,i,j)
                    upper_cases += 1
                    assert d2<top, (n,i,j,d2,top)
                    if n>=7 and ((i==0) != (j==n-1)) and j-i==4:
                        assert d2==F(5,6)
                        # The candidate fails the first-order condition:
                        # the intervening zero edge has absolute residual gradient 1/3 > 1/4.
                        a=upper_candidate(n,i,j)[1]
                        r=residual(a,i,j)
                        g=[r[k]-r[k+1] for k in range(n-1)]
                        assert max(map(abs,g))>F(1,4)
        if n>=7:
            second=[(i,j) for i in range(n) for j in range(i+1,n)
                     if (i==0) != (j==n-1) and j-i>=5]
            assert len(second)==2*(n-6), (n,len(second))
    return count,long_cases,upper_cases


def numerical_check():
    import numpy as np
    from scipy.optimize import minimize
    total=0;worst_error=0.
    for n in range(3,11):
        E=np.eye(n)[:,:-1]-np.eye(n)[:,1:]
        top=float(exact_certificate(n,0,n-1)[0])
        for i in range(n):
            for j in range(i+1,n):
                d2_exact=exact_certificate(n,i,j)
                if d2_exact is None:
                    continue
                v=np.eye(n)[i]-np.eye(n)[j]
                def objective(z):
                    a=z[:n-1]-z[n-1:]
                    return .5*np.dot(E@a-v,E@a-v)
                def jac(z):
                    a=z[:n-1]-z[n-1:]
                    g=E.T@(E@a-v)
                    return np.r_[g,-g]
                res=minimize(objective,np.zeros(2*(n-1)),jac=jac,
                     bounds=[(0,None)]*(2*(n-1)),
                     constraints=[{'type':'ineq','fun':lambda z:1.-z.sum(),
                                   'jac':lambda z:-np.ones_like(z)}],
                     method='SLSQP',options={'maxiter':1200,'ftol':1e-12})
                if not res.success or abs(2*res.fun-float(d2_exact[0]))>2e-7:
                    raise AssertionError((n,i,j,res.message,2*res.fun,d2_exact[0]))
                worst_error=max(worst_error, abs(2*res.fun-float(d2_exact[0])))
                total+=1
    return total,worst_error


if __name__ == '__main__':
    total,longs,uppers=verify_exact()
    print('EXACT_KKT_PASS', 'n=3..40', 'pairs=',total,'long_projections=',longs,'short_upper_bounds=',uppers)
    cases,error=numerical_check()
    print('INDEPENDENT_QP_PASS','cases=',cases,'max_squared_error=',format(error,'.3g'))
    print('PATH_ROOT_HAUSDORFF_PASS max_squared=[1/2,4/5,9/10,11/12] second_shell_n>=7=5/6')
