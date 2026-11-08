"""Exact checks of site-trapping efficiency on weighted rook networks.
Run: python checker.py
Uses SymPy, available separately from the theorem's four-projector derivation.
"""
from fractions import Fraction
from sympy import Matrix, eye, zeros, Rational

def formulas(m,n,region,resonant):
    if region=='trap': return Rational(1)
    if region=='same_row':
        base=Rational(1,n-1)
        drop=Rational((m-1)*n,m*(n-1)*(m+n-2))
    elif region=='same_column':
        base=Rational(1,m-1)
        drop=Rational((n-1)*m,n*(m-1)*(m+n-2))
    elif region=='different':
        base=Rational(1,(m-1)*(n-1))
        drop=Rational((m-n)**2,m*n*(m-1)*(n-1)*(m+n-2))
    else: raise ValueError(region)
    return base-drop if resonant else base

def independent_krylov(m,n,alpha,beta):
    N=m*n
    H=zeros(N,N)
    for i in range(m):
        for j in range(n):
            s=i*n+j
            for k in range(m):
                if k!=i: H[s,k*n+j]=alpha
            for l in range(n):
                if l!=j: H[s,i*n+l]=beta
    v=zeros(N,1);v[0]=1
    columns=[]
    for k in range(5):
        columns.append(v)
        v=H*v
    C=Matrix.hstack(*columns)
    pivots=C.rref()[1]
    B=C[:,list(pivots)]
    P=B*(B.T*B).inv()*B.T
    return P

def run():
    count=0
    for m in range(2,6):
        for n in range(2,6):
            for isres,alpha,beta in [(False,1,7),(True,n,m)]:
                # For m=2..5, n=2..5, alpha/beta=1/7 is never n/m.
                assert (alpha*m==beta*n)==isres
                P=independent_krylov(m,n,alpha,beta)
                points={'trap':0,'same_row':1,'same_column':n,'different':n+1}
                for region,idx in points.items():
                    target=formulas(m,n,region,isres)
                    got=P[idx,idx]
                    assert got==target,(m,n,region,isres,got,target)
                    count+=1
                assert P==P.T and P*P==P
                count+=2
    for q in range(2,20):
        assert formulas(q,q,'same_row',True)==Rational(1,2*(q-1))
        assert formulas(q,q,'same_column',True)==Rational(1,2*(q-1))
        assert formulas(q,q,'different',True)==Rational(1,(q-1)**2)
        count+=3
    print('PASS',count,'exact Krylov, idempotence and resonance identities')

if __name__=='__main__': run()

def dynamic_checks():
    import numpy as np
    from scipy.linalg import expm
    count=0
    for m,n in [(2,2),(2,3),(3,3),(3,4)]:
      for isres,alpha,beta in [(False,1,7),(True,n,m)]:
        N=m*n
        H=np.zeros((N,N),dtype=float)
        for i in range(m):
          for j in range(n):
            for k in range(m):
              if i!=k: H[i*n+j,k*n+j]=alpha
            for l in range(n):
              if j!=l: H[i*n+j,i*n+l]=beta
        G=-1j*H-np.diag([1.0]+[0.0]*(N-1))
        E=expm(1200*G)
        for reg,idx in {'trap':0,'same_row':1,'same_column':n,'different':n+1}.items():
          init=np.zeros(N,complex);init[idx]=1
          result=1-np.linalg.norm(E@init)**2
          expected=float(formulas(m,n,reg,isres))
          assert abs(result-expected)<1e-8,(m,n,isres,reg,result,expected)
          count+=1
    print('PASS',count,'independent non-Hermitian long-time evolution checks')
if __name__=='__main__': dynamic_checks()
