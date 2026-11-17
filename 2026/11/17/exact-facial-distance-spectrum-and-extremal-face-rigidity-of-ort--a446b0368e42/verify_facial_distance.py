"""Independent finite checks for facial separation of orthogonal cubical joins.
No finite check is used as a proof of statements for unbounded dimensions.
Run: python cubical_join_facial_verifier.py
"""
from itertools import product
from math import sqrt
import numpy as np
from scipy.optimize import minimize

def vertices(p,q):
    A=np.array([list(s)+[0.]*q for s in product((-1.,1.),repeat=p)])
    B=np.array([[0.]*p+list(s) for s in product((-1.,1.),repeat=q)])
    return np.concatenate((A,B)),len(A)

def evaluate(p,q,k,l):
    V,na=vertices(p,q)
    # Exactly one of k,l zero: face from a single cube.
    assert k or l
    if l==0:
        f=np.array([all(x[:k]>0) for x in V]) & (np.arange(len(V))<na)
        expected=1. if k==1 else 2/sqrt(k)
    elif k==0:
        f=np.array([all(x[p:p+l]>0) for x in V]) & (np.arange(len(V))>=na)
        expected=1. if l==1 else 2/sqrt(l)
    else:
        a=np.array([all(x[:k]>0) for x in V]) & (np.arange(len(V))<na)
        b=np.array([all(x[p:p+l]>0) for x in V]) & (np.arange(len(V))>=na)
        f=a|b
        expected=2/(max(k,l)*sqrt(1/k+1/l))
    F=V[f];C=V[~f];m=len(F);n=len(C)
    def fun(w):
        z=w[:m]@F-w[m:]@C
        return float(z@z)
    def jac(w):
        z=w[:m]@F-w[m:]@C
        return np.r_[2*(F@z),-2*(C@z)]
    z0=np.r_[np.ones(m)/m,np.ones(n)/n]
    constraints=[{'type':'eq','fun':lambda w:np.sum(w[:m])-1,'jac':lambda w:np.r_[np.ones(m),np.zeros(n)]},
                 {'type':'eq','fun':lambda w:np.sum(w[m:])-1,'jac':lambda w:np.r_[np.zeros(m),np.ones(n)]}]
    res=minimize(fun,z0,jac=jac,method='SLSQP',bounds=[(0.,1.)]*(m+n),constraints=constraints,
                 options={'maxiter':500,'ftol':1e-12})
    if not res.success and abs(sqrt(max(0,res.fun))-expected)>2e-6:
        raise AssertionError((p,q,k,l,res.message,res.fun,expected))
    assert abs(sqrt(max(0,res.fun))-expected)<2e-6,(p,q,k,l,sqrt(res.fun),expected)
    return expected

def main():
    checked=0
    for p,q in [(1,2),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        candidates=[]
        for k in range(1,p+1):
            candidates.append(evaluate(p,q,k,0));checked+=1
        for l in range(1,q+1):
            candidates.append(evaluate(p,q,0,l));checked+=1
        for k in range(1,p+1):
            for l in range(1,q+1):
                candidates.append(evaluate(p,q,k,l));checked+=1
        assert abs(min(candidates)-2/sqrt(q*(q+1)))<1e-12
        type_minimizers=sum(abs(v-min(candidates))<1e-12 for v in candidates)
        assert type_minimizers==(2 if p==q else 1)
        minimizer_face_count=(2*p*2**q)+(2*q*2**p if p==q else 0)
        assert minimizer_face_count>0
        print(f'{p=}, {q=}, min={min(candidates):.12f}, face-types checked={p+q+p*q}')
    print('PASS',checked,'independent constrained quadratic optimizations; plus global face-type minima.')
if __name__=='__main__': main()
