#!/usr/bin/env python3
"""Reproducibility checks for two-sided extreme-edge limits of Haar-frame polygons.
Only standard numpy is required. Numerical experiments corroborate, not prove, asymptotics.
"""
import math
import numpy as np


def frame_edges(n, complex_frame, rng):
    if complex_frame:
        G = (rng.normal(size=(n, 2)) + 1j*rng.normal(size=(n, 2)))/math.sqrt(2)
    else:
        G = rng.normal(size=(n,2))
    S = G.conj().T @ G / n
    vals, vecs = np.linalg.eigh(S)
    inverse_root = (vecs * (vals**-0.5)) @ vecs.conj().T
    U = G @ inverse_root / math.sqrt(n)
    edge_lengths = np.sum(np.abs(U)**2, axis=1)
    z = np.sum(np.abs(G)**2,axis=1)
    delta = np.linalg.norm(np.linalg.inv(S)-np.eye(2),ord=2)
    assert np.allclose(U.conj().T @ U, np.eye(2), atol=1.e-10)
    assert np.isclose(edge_lengths.sum(),2.,atol=1.e-10)
    assert np.max(np.abs(n*edge_lengths-z)) <= delta*np.max(z)+1.e-9
    if not complex_frame:
        a,b = U[:,0],U[:,1]
        edges = np.column_stack((a*a-b*b,2*a*b))
        assert np.linalg.norm(edges.sum(axis=0)) <1e-10
        assert np.allclose(np.linalg.norm(edges,axis=1),edge_lengths,atol=1e-10)
    else:
        a,b = U[:,0],U[:,1]
        edges = np.column_stack((np.abs(a)**2-np.abs(b)**2,2*np.real(a*np.conj(b)),2*np.imag(a*np.conj(b))))
        assert np.linalg.norm(edges.sum(axis=0)) <1e-10
        assert np.allclose(np.linalg.norm(edges,axis=1),edge_lengths,atol=1e-10)
    return edge_lengths, delta


def exp_gumbel_cdf(x):
    return math.exp(-math.exp(-x))


def finite_independent(n, is_space, x=0., t=1.):
    if is_space:
        high=math.log(n)+math.log(math.log(n))+x
        low=t/math.sqrt(n)
        survival=lambda z:(1+z)*math.exp(-z)
        lower_survival=math.exp(-t*t/2)
    else:
        high=2*(math.log(n)+x)
        low=2*t/n
        survival=lambda z:math.exp(-z/2)
        lower_survival=math.exp(-t)
    upper=1-survival(high)
    lower=1-survival(low)
    pmax=upper**n
    pmin=survival(low)**n
    joint=(upper-lower)**n
    return pmax,pmin,joint,exp_gumbel_cdf(x),lower_survival


def run():
    rng=np.random.default_rng(20261113)
    print('Finite-n i.i.d. tail-law convergence (reference only):')
    for space in (False,True):
        for n in (1000, 100000):
            pmax,pmin,joint,pG,pR=finite_independent(n,space)
            print(('space' if space else 'plane'),n,'Pmax',round(pmax,5),'Pmin',round(pmin,5),'Pjoint',round(joint,5),'limits',round(pG,5),round(pR,5))
        n=1200; samples=750
        vals=[]; gramdev=[]
        for _ in range(samples):
            e,d=frame_edges(n,space,rng)
            if space:
                val=(n*e.max()-math.log(n)-math.log(math.log(n)),n**1.5*e.min())
            else:
                val=(n*e.max()/2-math.log(n),n*n*e.min()/2)
            vals.append(val); gramdev.append(d)
        vals=np.asarray(vals)
        empmax=float(np.mean(vals[:,0]<=0))
        empmin=float(np.mean(vals[:,1]>1))
        empjoint=float(np.mean((vals[:,0]<=0)&(vals[:,1]>1)))
        iid_joint=finite_independent(n,space)[2]
        print(('space' if space else 'plane'),'simulation n',n,'trials',samples, 'P(max<=0)',round(empmax,4),'P(min>1)',round(empmin,4),'Pjoint',round(empjoint,4),'iid_formula',round(iid_joint,4),'mean_delta',round(float(np.mean(gramdev)),5))
        # Checks bounded by finite-sample tolerances, not claims of exact convergence rates.
        assert abs(empjoint-iid_joint)<0.10
    print('STIEFEL_TWO_SIDED_EXTREMES_CHECKS_OK')

if __name__=='__main__':
    run()
