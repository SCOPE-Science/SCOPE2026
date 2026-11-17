"""Independent numerical facial-distance enumeration for weighted cross-polytopes.

Requires NumPy and SciPy. The theoretical distances are compared with
unconstrained convex-pair QP solutions, not used as constraints by the solver.
"""
from itertools import combinations, product
import numpy as np
from scipy.optimize import minimize


def face_vertices(a, I, signs):
    k = len(a)
    out = []
    for i, sign in zip(I, signs):
        v = np.zeros(k)
        v[i] = sign * a[i]
        out.append(v)
    return np.array(out)


def complement_vertices(a, I, signs):
    d = len(a)
    signmap = dict(zip(I, signs))
    vertices = []
    for i in range(d):
        for s in [-1, 1]:
            if i in signmap and s == signmap[i]:
                continue
            p = np.zeros(d)
            p[i] = s*a[i]
            vertices.append(p)
    return np.array(vertices)


def qp_dist(A, B):
    k, l = len(A), len(B)
    M = np.concatenate((A.T, -B.T), axis=1)
    Q = M.T @ M
    z0 = np.ones(k+l)
    z0[:k] /= k
    z0[k:] /= l
    constraints = [{'type':'eq','fun':lambda z:np.sum(z[:k])-1,'jac':lambda z: np.r_[np.ones(k), np.zeros(l)]},
                   {'type':'eq','fun':lambda z:np.sum(z[k:])-1,'jac':lambda z: np.r_[np.zeros(k), np.ones(l)]}]
    sol = minimize(lambda z: z@Q@z, z0, jac=lambda z: 2*Q@z,
                   method='SLSQP', bounds=[(0,1)]*(k+l), constraints=constraints,
                   options={'ftol':2e-13,'maxiter':1000})
    assert sol.success or (abs(np.sum(sol.x[:k])-1)<1e-8 and abs(np.sum(sol.x[k:])-1)<1e-8)
    return np.sqrt(max(0,sol.fun))


def check(a):
    n = len(a)
    worst = 0.
    count = 0
    min_obs = float('inf')
    min_expected = 1/np.sqrt(sum(a**-2)-min(a**-2))
    for k in range(1,n+1):
        for I in combinations(range(n),k):
            for signs in product([-1,1], repeat=k):
                A = face_vertices(a,I,signs)
                B = complement_vertices(a,I,signs)
                observed = qp_dist(A,B)
                predicted = (1/np.sqrt(sum((1/a[i])**2 for i in I))
                             if k<n else 2/np.sqrt(sum(a**-2)))
                error = abs(observed-predicted)
                worst=max(worst,error)
                assert error < 3e-6, (a,I,signs,observed,predicted)
                min_obs=min(min_obs,observed)
                count+=1
    assert abs(min_obs-min_expected)<3e-6
    return count,worst,min_expected

if __name__=='__main__':
    families = [np.array(a, dtype=float) for a in
       ([1,1], [1,2], [1,1,1], [1,2,3], [2,2,5,5], [1,2,3,6], [1,1,1,1,1], [1,2,3,4,7])]
    total=0
    for a in families:
        count,err,pred=check(a)
        print('dimension',len(a),'axes',','.join(map(str,a)),'face checks',count,'max error',f'{err:.2e}','facial distance',f'{pred:.9f}')
        total+=count
    print('ALL PASSED:', total, 'face/complement distance checks')
