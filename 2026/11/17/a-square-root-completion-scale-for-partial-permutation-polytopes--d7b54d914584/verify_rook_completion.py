"""Reproducible checks for distances from partial-permutation vertices to the Birkhoff polytope.
Run: python verify_rook_completion.py. Requires Python standard library;
NumPy/SciPy are used only for the optional independent numerical check.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, log, exp, sqrt


def candidate(n,k):
    q=n-k
    if q==0:
        return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    if k==0:
        return [[Fraction(1,n) for j in range(n)] for i in range(n)]
    D=n+q*(q+1)
    return [[(Fraction(D-q,D) if i==j else Fraction(0)) if i<k and j<k else
             Fraction(1,D) if (i<k) != (j<k) else Fraction(q+2,D)
             for j in range(n)] for i in range(n)]


def verify_exact():
    cases=ineq=0
    for n in range(2,8):
        for k in range(n+1):
            Y=candidate(n,k)
            assert all(sum(row)==1 for row in Y)
            assert all(sum(Y[i][j] for i in range(n))==1 for j in range(n))
            assert all(t>=0 for row in Y for t in row)
            M=[[Fraction(int(i==j and i<k)) for j in range(n)] for i in range(n)]
            value=sum((M[i][j]-Y[i][j])**2 for i in range(n) for j in range(n))
            q=n-k
            assert value==Fraction(q*(q+2),n+q*(q+1)),(n,k,value)
            baseline=sum((M[i][j]-Y[i][j])*Y[i][j] for i in range(n) for j in range(n))
            for p in permutations(range(n)):
                diff=sum(M[i][p[i]]-Y[i][p[i]] for i in range(n))-baseline
                assert diff<=0,(n,k,p,diff)
                ineq+=1
            cases+=1
    return cases,ineq


def check_distributions():
    for n in range(2,60):
        counts=[comb(n,q)**2*factorial(n-q) for q in range(n+1)]
        assert all(counts[q]==factorial(n)*comb(n,q)//factorial(q) for q in range(n+1))
        f=[Fraction(q*(q+2),n+q*(q+1)) for q in range(n+1)]
        assert all(f[q]<f[q+1] for q in range(n))
        assert f[0]==0 and f[-1]==1
    vals=[]
    for n in [100,1000,10000,1000000]:
        # Stable probability via log weights.  Verify concentration at q ~ sqrt(n)
        lo=max(0,int(sqrt(n)-9*n**.25)); hi=int(sqrt(n)+9*n**.25)+1
        ps=[]
        for q in range(lo,hi):
            # log binomial(n,q) - log factorial(q)
            from math import lgamma
            lp=lgamma(n+1)-lgamma(n-q+1)-2*lgamma(q+1)
            ps.append((q,lp))
        m=max(t for _,t in ps)
        weights=[exp(t-m) for _,t in ps]; sw=sum(weights)
        mu=sum(w*q for (q,_),w in zip(ps,weights))/sw
        var=sum(w*(q-mu)**2 for (q,_),w in zip(ps,weights))/sw
        d2=sum(w*q*(q+2)/(n+q*(q+1)) for (q,_),w in zip(ps,weights))/sw
        vals.append((n,round(mu/sqrt(n),6),round(var/sqrt(n),6),round(d2,6)))
    return vals


def verify_independent_qp():
    try:
        import numpy as np
        from scipy.optimize import minimize
    except ImportError:
        return 'not available (exact certificate still complete)'
    trials=0;max_err=0
    for n in range(2,6):
        for k in range(n+1):
            M=np.diag([1.]*k+[0.]*(n-k))
            Y=np.array(candidate(n,k),dtype=float)
            A=[]
            for i in range(n):
                mat=np.zeros((n,n));mat[i,:]=1;A.append(mat.flatten())
            for j in range(n-1):
                mat=np.zeros((n,n));mat[:,j]=1;A.append(mat.flatten())
            A=np.array(A)
            constraints=[{'type':'eq','fun':lambda z,A=A: A@z-1., 'jac':lambda z,A=A:A}]
            res=minimize(lambda z: np.sum((z-M.ravel())**2),np.ones(n*n)/n,
                         jac=lambda z: 2*(z-M.ravel()), bounds=[(0.,None)]*(n*n),
                         constraints=constraints,method='SLSQP',
                         options={'ftol':1.e-12,'maxiter':500})
            assert res.success,res.message
            err=np.linalg.norm(res.x-Y.ravel(),ord=np.inf)
            assert err<2e-6,(n,k,err)
            max_err=max(max_err,err);trials+=1
    return trials,max_err

if __name__=='__main__':
    c,ineq=verify_exact()
    moments=check_distributions()
    qp=verify_independent_qp()
    print('ROOK_BIRKHOFF_PASS exact_cases=%d exact_vertex_inequalities=%d qp=%s' %(c,ineq,qp))
    print('sample_n mean_deficiency_over_sqrt_n variance_over_sqrt_n mean_squared_distance')
    for t in moments: print(*t)
