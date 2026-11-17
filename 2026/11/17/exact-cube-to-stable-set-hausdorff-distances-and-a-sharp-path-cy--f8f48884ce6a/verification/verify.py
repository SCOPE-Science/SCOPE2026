#!/usr/bin/env python3
"""Independent finite diagnostics for cube-to-stable-set Euclidean distances.

Exact KKT identities use rational arithmetic; finite QPs independently check
path and cycle cases without assuming their predicted projections.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np
from scipy.optimize import minimize


def path_certificate(n):
    assert n >= 2
    if n % 2 == 0:
        y = [F(1, 2)]*n
        lam = [F(int(i % 2 == 1)) for i in range(1, n)]
        norm2 = F(n, 4)
    else:
        m = n//2
        y = [F(m if i % 2 == 1 else m+1, n) for i in range(1, n+1)]
        lam = [F(2*(m-(i+1)//2+1),n) if i%2 else F(i,n) for i in range(1,n)]
        norm2 = F(n*n-1,4*n)
    assert all(a>0 for a in y)
    assert all(a>=0 for a in lam)
    assert all(y[i]+y[i+1]==1 for i in range(n-1))
    assert all(2*y[i] == (lam[i-1] if i else 0)+(lam[i] if i<n-1 else 0) for i in range(n))
    assert sum(a*a for a in y)==norm2
    assert sum(lam) == 2*norm2
    return y, norm2


def cycle_certificate(n):
    a = n//2
    x = F(a,n)
    y = F(n-a,n)
    assert y>0
    assert n*y*y == (F(n,4) if n%2==0 else F((n+1)*(n+1),4*n))
    # Averaging every rotation of a maximal independent set makes x uniform.
    seed = [int(i%2==0 and i<2*a) for i in range(n)]
    assert sum(seed)==a
    assert all(seed[i]+seed[(i+1)%n] <= 1 for i in range(n))
    averaged=[F(sum(seed[(i-k)%n] for k in range(n)),n) for i in range(n)]
    assert averaged==[x]*n
    return y, n*y*y


def nearest_qp(n, is_cycle=False, target=None):
    if target is None: target=np.ones(n)
    edges=[(i,i+1) for i in range(n-1)]
    if is_cycle: edges.append((n-1,0))
    AA=np.zeros((len(edges),n))
    for j,(i,k) in enumerate(edges): AA[j,i]=1;AA[j,k]=1
    cons=[{'type':'ineq','fun':lambda x,A=AA: 1-A@x,'jac':lambda x,A=AA:-A}]
    if is_cycle and n%2:
        cons.append({'type':'ineq','fun':lambda x,n=n: (n-1)/2-np.sum(x),'jac':lambda x:-np.ones(n)})
    res=minimize(lambda x:np.sum((x-target)**2),np.zeros(n)+.4,
                 jac=lambda x:2*(x-target),bounds=[(0,1)]*n,
                 constraints=cons,method='SLSQP',options={'ftol':1e-12,'maxiter':1000})
    assert res.success, (n,is_cycle,res.message)
    return res.x, res.fun


def main():
    for n in range(2,301): path_certificate(n)
    for n in range(3,301): cycle_certificate(n)
    solved=0; vertex_checks=0
    for n in range(3,15):
        for cyc in (False,True):
            y,norm= (cycle_certificate(n) if cyc else path_certificate(n))
            expected=(np.ones(n)*float(1-y) if cyc else 1-np.array([float(a) for a in y]))
            got,dd=nearest_qp(n,cyc)
            assert abs(dd-float(norm))<1e-7,(n,cyc,dd,norm)
            assert np.linalg.norm(got-expected)<1e-5,(n,cyc,got,expected)
            solved+=1
    for n in range(3,8):
        for cyc in (False,True):
            _,upper=nearest_qp(n,cyc)
            for bits in product((0.,1.),repeat=n):
                if all(a==1 for a in bits):continue
                _,dd=nearest_qp(n,cyc,np.array(bits))
                assert dd<upper-1e-7,(n,cyc,bits,dd,upper)
                vertex_checks+=1
    print('CUBE_STABLE_SET_PARITY_PASS exact_paths=299 exact_cycles=298 independent_qps=%d cube_corner_checks=%d' %(solved,vertex_checks))

if __name__=='__main__':main()
