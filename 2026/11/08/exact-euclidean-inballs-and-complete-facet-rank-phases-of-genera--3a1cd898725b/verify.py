"""Independent finite checks for Euclidean inspheres of arbitrary parking-function polytopes.

Requires only NumPy and SciPy. The all-dimensional result is proved analytically;
finite linear programs are corroborative, not a proof of universal quantifiers.
"""
from itertools import combinations
from math import sqrt
import numpy as np
from scipy.optimize import linprog


def data(b):
    n = len(b)
    S = np.cumsum(b, dtype=float)
    A = [float(sum(S[n-s:n]) - s) for s in range(1, n+1)]
    candidates = [A[s-1]/(s+sqrt(s)) for s in range(1, n+1)]
    return A, candidates


def full_lp(b):
    n = len(b)
    S = np.cumsum(b, dtype=float)
    normals = []
    upper = []
    for i in range(n):
        row = np.zeros(n+1)
        row[i] = -1
        row[-1] = 1
        normals.append(row)
        upper.append(-1.)
    for k in range(1, n+1):
        u = float(sum(S[n-k:n]))
        for I in combinations(range(n), k):
            row = np.zeros(n+1)
            row[list(I)] = 1
            row[-1] = sqrt(k)
            normals.append(row)
            upper.append(u)
    obj = np.zeros(n+1)
    obj[-1] = -1
    sol = linprog(obj, A_ub=np.asarray(normals), b_ub=np.asarray(upper), bounds=[(None, None)]*n+[(0, None)], method="highs")
    assert sol.success, sol.message
    return sol.x


def make_phase(n, k):
    # An integer perturbation of a single-spike monotone increment vector.
    B = 10000000
    c = k/(2*sqrt(k)+1)
    w = [B+j for j in range(n-1)] + [int(round(B*(1+c)))+n-1]
    assert all(w[i]<w[i+1] for i in range(n-1))
    return [w[0]+1]+[w[i]-w[i-1] for i in range(1,n)]


def run():
    trials=0
    all_phases=0
    for n in range(2,7):
        for k in range(1,n+1):
            b=make_phase(n,k)
            A, fs = data(b)
            idx = int(np.argmin(fs))+1
            assert idx==k, (n,k,b,fs)
            # Check all 2^n defining hyperplanes, not just symmetrized constraints.
            x=full_lp(b)
            r=min(fs)
            assert abs(x[-1]-r) < 1e-5*max(r,1), (n,k,r,x)
            assert max(abs(x[:n]-(1+r))) < 1e-5*max(r,1), (n,k,x)
            active=[s for s in range(1,n+1) if abs(fs[s-1]-r)<1e-8*max(r,1)]
            assert active == [k]
            all_phases+=1
            trials+=1
    for n in range(2,7):
        for a in (1,2,4,9,20):
            for b0 in (1,2,3,5):
                b=[a]+[b0]*(n-1)
                _, fs=data(b)
                r=min(fs)
                assert abs(r-min(fs[0],fs[-1]))<1e-9*max(r,1)
                x=full_lp(b)
                assert abs(x[-1]-r)<1e-6*max(r,1)
                trials+=1
    b=[69,1,31]
    A,fs=data(b)
    assert int(np.argmin(fs))==1, (A,fs)
    x=full_lp(b)
    assert abs(x[-1]-min(fs))<1e-7
    trials+=1
    print(f"ARBITRARY_PARKING_INBALL_CHECKS_PASSED trials={trials} distinct_rank_phase_witnesses={all_phases}")

if __name__ == "__main__":
    run()
