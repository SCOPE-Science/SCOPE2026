#!/usr/bin/env python3
"""Standalone numerical checks for exact cross-polytope skeletal-clearance identities.

Requires Python 3 and NumPy. Computations support, but do not replace, the proofs.
"""
import itertools
import math
import numpy as np


def distance_squared_formula(point, j):
    a = np.sort(np.abs(point))[::-1]
    return float(np.dot(point, point) - np.dot(a[:j], a[:j])
                 + (1.0 - a[:j].sum())**2 / j)


def closest_face_bruteforce(point, j):
    d = len(point)
    best = float('inf')
    for indices in itertools.combinations(range(d), j):
        for signs in itertools.product([-1, 1], repeat=j):
            z = point[list(indices)] * np.asarray(signs)
            ordered = np.sort(z)[::-1]
            candidates = ordered - (np.cumsum(ordered)-1)/np.arange(1,j+1)
            rank = np.flatnonzero(candidates > 0)[-1] + 1
            shift = (ordered[:rank].sum()-1)/rank
            projection = np.zeros(d)
            projection[list(indices)] = np.asarray(signs)*np.maximum(z-shift,0)
            best = min(best, float(np.sum((point-projection)**2)))
    return best


def reconstruct_abs_profile(distance_sq):
    d = len(distance_sq)
    slack = math.sqrt(max(d*distance_sq[-1],0.))
    recovered = np.zeros(d)
    for j in range(d-1,0,-1):
        gap = distance_sq[j-1]-distance_sq[j]
        z = math.sqrt(max(j*(j+1)*gap,0.))
        recovered[j] = (z-slack-sum(recovered[j+1:]))/(j+1)
    recovered[0] = 1-slack-sum(recovered[1:])
    return recovered


def exact_mean(d,j):
    h = lambda n,p=1: sum(r**(-p) for r in range(1,n+1))
    m = [h(d)-h(i-1) for i in range(1,j+1)]
    v = [h(d,2)-h(i-1,2) for i in range(1,j+1)]
    mu = sum(m)
    nu = sum((min(j,r)/r)**2 for r in range(1,d+1))
    den=(d+1)*(d+2)
    return (1/j +2*d/den-2*mu/(j*(d+1))
            +((mu*mu+nu)/j-sum(x*x+y for x,y in zip(m,v)))/den)


def main():
    rng = np.random.default_rng(1002015)
    # Independent projection-to-all-faces check, including non-positive signs.
    checked=0
    for d in (2,3,4,5):
        for _ in range(35):
            raw = rng.uniform(-1,1,d)
            point = raw/(1.5*np.sum(np.abs(raw)))
            sq = [distance_squared_formula(point,j) for j in range(1,d+1)]
            for j,expected in enumerate(sq,1):
                actual=closest_face_bruteforce(point,j)
                assert abs(actual-expected)<2e-12, (d,j,actual,expected)
                checked += 1
            recovered=reconstruct_abs_profile(sq)
            assert np.max(np.abs(recovered-np.sort(np.abs(point))[::-1]))<2e-11
    # Independent exact Dirichlet formula for finite-dimensional squared means.
    for d in (3,5,8):
        E = rng.exponential(size=(110000,d+1))
        X = E[:,:d] / E.sum(axis=1)[:,None]
        S = np.sort(X,axis=1)[:,::-1]
        cumul = np.cumsum(S,axis=1)
        cumul_sq = np.cumsum(S*S,axis=1)
        total_sq=(X*X).sum(axis=1)
        for j in (1,2,d):
            empirical=(total_sq-cumul_sq[:,j-1]+(1-cumul[:,j-1])**2/j)
            assert abs(empirical.mean()-exact_mean(d,j)) < 0.006, (d,j,empirical.mean(),exact_mean(d,j))
    # Exact independent gamma-Poisson joint-limit formulas: mean and covariance.
    M=210000
    exp = rng.exponential(size=(M,5))
    arrival = np.cumsum(exp,axis=1)
    Z = 2*np.cumsum(-np.log(arrival),axis=1)/np.arange(1,6)-2
    euler=0.5772156649015328606
    psi1 = lambda j: math.pi**2/6-sum(r**-2 for r in range(1,j))
    for j in (1,2,3,5):
        em=2*euler-2*sum(1/r for r in range(1,j))-2/j
        ev=4*psi1(j)+4*(j-1)/j**2
        assert abs(Z[:,j-1].mean()-em)<.038,(j,'mean')
        assert abs(Z[:,j-1].var()-ev)<.10,(j,'variance')
    for j,k in ((1,2),(2,4),(3,5)):
        cov=4/(j*k)*sum(psi1(max(i,h)) for i in range(1,j+1) for h in range(1,k+1))
        empirical=np.cov(Z[:,j-1],Z[:,k-1],bias=True)[0,1]
        assert abs(empirical-cov)<.10,(j,k,empirical,cov)
    # Finite-dimensional convergence check, independent of the Poisson generator.
    d=1200;j=3;n=15000
    batches=[]
    for _ in range(5):
        E=rng.exponential(size=(n//5,d+1))
        X=E[:,:d]/E.sum(axis=1)[:,None]
        top=np.partition(X,-j,axis=1)[:,-j:]
        D2=(X*X).sum(axis=1)-(top*top).sum(axis=1)+(1-top.sum(axis=1))**2/j
        batches.append(d*(1/j-D2)-2*np.log(d))
    empirical=np.concatenate(batches)
    expected=2*euler-2*sum(1/r for r in range(1,j))-2/j
    assert abs(empirical.mean()-expected)<.3,(empirical.mean(),expected)
    print('CROSSPOLYTOPE_SKELETON_SIGNATURE_JOINT_GAMMA_LIMIT_OK',checked,M,n)


if __name__ == '__main__':
    main()
