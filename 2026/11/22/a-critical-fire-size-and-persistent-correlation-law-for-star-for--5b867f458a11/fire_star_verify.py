"""Exact finite-star forest-fire cycle checks. Python 3 standard library only.

The marked renewal-integral expression and an independently constructed
absorbing continuous-time Markov chain are evaluated over rational numbers.
The all-size and scaling arguments are analytic, not consequences of these tests.
"""
from fractions import Fraction as F
from math import comb

ZERO = F(0)
ONE = F(1)

def poly_mul(a,b):
    o={}
    for (i,j,k),v in a.items():
        for (r,s,t),w in b.items():
            key=(i+r,j+s,k+t)
            o[key]=o.get(key,ZERO)+v*w
    return {key:val for key,val in o.items() if val}

def poly_pow(a,n):
    out={(0,0,0):ONE}
    for _ in range(n): out=poly_mul(out,a)
    return out

def exact_cycle_law(n,lam):
    assert lam>0 and lam!=1
    A={(0,1,0):lam/(1+lam), (1,1,0):1/(1+lam)}
    den=1-lam*lam
    B={(0,0,1):1/den, (1,0,1):lam/den,
       (0,1,0):-lam/den, (1,1,0):-1/den}
    out=[]
    for k in range(n+1):
        poly=poly_mul(poly_pow(A,n-k),poly_pow(B,k))
        integral=sum((val/(1+(1+lam)*i)/(lam+j+lam*l)
                 for (i,j,l),val in poly.items()),ZERO)
        out.append(lam*(k+1)*comb(n,k)*integral)
    return out

def independent_ctmc(n,lam):
    # State (hub occupancy, number of occupied leaves), until a fire
    # involving the occupied hub; one-vertex leaf fires do not end the cycle.
    st=[(h,k) for h in (0,1) for k in range(n+1)]
    ix={s:i for i,s in enumerate(st)}
    d=len(st)
    Q=[[ZERO]*d for _ in range(d)]
    R=[[ZERO]*(n+1) for _ in range(d)]
    def move(i,to,rate):
        Q[i][i]-=rate
        Q[i][ix[to]]+=rate
    for i,(h,k) in enumerate(st):
        if k<n: move(i,(h,k+1),F(n-k))
        if h==0:
            if k: move(i,(0,k-1),lam*k)
            move(i,(1,k),ONE)
        else:
            rate=lam*(k+1)
            Q[i][i]-=rate
            R[i][k]+=rate
    # Gauss-Jordan inversion of -Q with all n+1 absorption RHS columns.
    mat=[[-Q[i][j] for j in range(d)]+R[i][:] for i in range(d)]
    for col in range(d):
        pivot=next(i for i in range(col,d) if mat[i][col])
        mat[col],mat[pivot]=mat[pivot],mat[col]
        inv=ONE/mat[col][col]
        mat[col]=[v*inv for v in mat[col]]
        for i in range(d):
            if i!=col:
                factor=mat[i][col]
                if factor:
                    mat[i]=[x-factor*y for x,y in zip(mat[i],mat[col])]
    return mat[ix[(0,0)]][d:]

def check():
    cases=0
    for n in range(1,6):
        for lam in (F(1,4),F(1,3),F(1,2),F(2,3),F(3,2),F(2)):
            a=exact_cycle_law(n,lam)
            b=independent_ctmc(n,lam)
            assert a==b,(n,lam,a,b)
            assert sum(a,ZERO)==ONE
            assert all(x>0 for x in a)
            cases+=1
    print('STAR_FIRE_EXACT_MARKED_CYCLE_CHECKS_PASSED',cases)
if __name__=='__main__': check()
