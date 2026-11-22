#!/usr/bin/env python3
"""Finite-state checks of conditional survival selection for a resource game.

Requires numpy and scipy. These examples verify generator construction,
spectral separation, and representative conditioned laws; the general
all-size result rests on the mathematical argument in RESULT.md.
"""
from fractions import Fraction as F
import numpy as np
from scipy.linalg import eigvals, expm


def generator(n, k, ecc, ecd, edc, edd, b=1., nu=1.):
    rc = k * (1 - ecc / b)
    assert n >= 2 and k >= 2 and 0 < ecc < b < edd
    assert min(ecd, edc) >= ecc and nu > 0
    states = [(c, r) for c in range(n+1) for r in range(1, k+1)]
    idx = {s: j for j,s in enumerate(states)}
    q = np.zeros((len(states), len(states)))
    for j, (c,r) in enumerate(states):
        d = n-c
        up = b*r*(1-r/k)
        down = r*(ecc*c*(c-1)+(ecd+edc)*c*d+edd*d*(d-1))/(n*(n-1))
        cu = nu*c*d/n*max(1-r/rc, 0)
        cd = nu*c*d/n*(r/rc)
        if r<k: q[j, idx[c,r+1]] += up
        if r>1: q[j, idx[c,r-1]] += down
        if c<n: q[j, idx[c+1,r]] += cu
        if c>0: q[j, idx[c-1,r]] += cd
        q[j,j] -= up+down+cu+cd
    return q, states, rc


def top(q):
    return float(np.max(eigvals(q).real))


def exercise():
    cases=0
    max_err=0.
    for n in range(2,7):
        for k in range(2,8):
            for ecc in (.25,.5,.8):
                q,states,rc=generator(n,k,ecc,ecc,1.5,1.5)
                assert (q-np.diag(np.diag(q))>=-1e-12).all()
                assert (q.sum(axis=1)<=1e-12).all()
                assert (q.sum(axis=1)>=-1.50001).all()
                blocks=[q[c*k:(c+1)*k,c*k:(c+1)*k] for c in range(n+1)]
                eig=[top(a) for a in blocks]
                if rc>1+1e-12:
                    assert eig[-1]>max(eig[:-1])+1e-8, (n,k,ecc,eig)
                    # The positive Perron right vector increases with resources.
                    vals,vecs=np.linalg.eig(blocks[-1]); j=np.argmax(vals.real)
                    v=vecs[:,j].real
                    if v[0]<0:v=-v
                    assert np.all(np.diff(v)>1e-10), (n,k,ecc,v)
                else:
                    # With positive resource, no mixed state can reach all-cooperator.
                    for j,(c,r) in enumerate(states):
                        if c<n:
                            assert q[j,n*k:(n+1)*k].sum()==0
                cases+=1
    # Independent rational arithmetic, including exact critical capacity.
    n,k=3,2
    e=F(1,2); rc=F(k)*(1-e)
    assert rc==1
    assert [F(1,1)-F(r,1)/rc for r in (1,2)]==[0,F(-1,1)]
    q,states,_=generator(3,3,.5,.5,1.5,1.5)
    start=states.index((1,2))
    qco=q[3*3:4*3,3*3:4*3]
    spec=top(qco)
    other=max(top(q[c*3:(c+1)*3,c*3:(c+1)*3]) for c in range(3))
    assert spec>other
    for t in (10,30,60):
        z=expm(q*t)[start]
        conditioned=z[3*3:4*3].sum()/z.sum()
        if t==60: assert conditioned>1-1e-12
    # Crossing K=2 to K=3 is the sharp first integer-capacity change.
    q2,s2,rc2=generator(3,2,.5,.5,1.5,1.5)
    assert rc2==1 and rc==1
    assert np.allclose(expm(q2*35)[s2.index((1,2))][-2:],0)
    print(f'PASS: {cases} parameter families; strict Perron ordering, generator structure,')
    print('resource monotonicity, a critical exact-rational boundary, and conditional limits.')


if __name__=='__main__': exercise()
