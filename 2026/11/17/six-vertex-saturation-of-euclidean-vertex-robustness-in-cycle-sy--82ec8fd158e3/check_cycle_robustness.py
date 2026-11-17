"""Exact rational projection certificates and independent finite quadratic programming tests.
Run: python check_cycle_robustness.py
"""
from fractions import Fraction as F
from math import sqrt
import numpy as np
from scipy.optimize import minimize


def roots(n):
    out=[]
    for j in range(n):
        r=[0]*n
        r[j]=1
        r[(j+1)%n]=-1
        out.append(r)
    return out


def coeffs(n):
    if n==3: return [F(1,2),F(1,2)]
    if n==4: return [F(2,5),F(1,5),F(2,5)]
    if n==5: return [F(2,5),F(1,10),F(1,10),F(2,5)]
    return [F(5,12),F(1,12)]+[F(0)]*(n-5)+[F(1,12),F(5,12)]


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def rational_certificate(n):
    r=roots(n)
    s=coeffs(n)
    assert len(s)==n-1 and sum(s)==1 and all(x>=0 for x in s)
    target=r[0]
    x=[-sum(s[j-1]*r[j][k] for j in range(1,n)) for k in range(n)]
    y=[target[k]-x[k] for k in range(n)]
    norm=dot(y,y)
    expected={3:F(1,2),4:F(4,5),5:F(9,10)}.get(n,F(11,12))
    assert norm==expected,(n,norm,expected)
    all_other=[[-z for z in target]]+[r[j] for j in range(1,n)]+[[-z for z in r[j]] for j in range(1,n)]
    support=dot(y,x)
    assert dot(y,target)-support==norm
    assert all(dot(y,z)<=support for z in all_other)
    tight=[i for i,z in enumerate(all_other) if dot(y,z)==support]
    assert len(tight)==min(n-1,4), (n,tight)
    assert tight==list(range(n,n+min(n-1,4))) if n<6 else tight==[n,n+1,2*n-3,2*n-2],(n,tight)
    return norm,len(tight)


def independent_numerical(n):
    r=np.asarray(roots(n),dtype=float)
    a=np.asarray([-r[0]]+[r[j] for j in range(1,n)]+[-r[j] for j in range(1,n)])
    target=r[0]
    D=a-target
    w=np.ones(len(a))/len(a)
    result=minimize(lambda p: np.dot(p@D,p@D),w,
                    jac=lambda p: 2*D@(p@D),
                    bounds=[(0,1)]*len(a),
                    constraints=[{'type':'eq','fun':lambda p:p.sum()-1,'jac':lambda p:np.ones(len(p))}],
                    method='SLSQP', options={'ftol':1e-12,'maxiter':1500})
    assert result.success, (n,result.message)
    assert abs(result.fun-float(rational_certificate(n)[0]))<5e-8,(n,result.fun)
    return result.fun

if __name__=='__main__':
    count=0
    for n in range(3,161):
        rational_certificate(n)
        count+=1
    for n in range(3,19):
        independent_numerical(n)
    print(f'CYCLE_VERTEX_ROBUSTNESS_PASS exact_n={count} independent_qp_n=16 cutoff=6 plateau_squared=11/12')
