"""Finite checks accompanying the critical-lattice boxcar theorem.

No finite test substitutes for the all-dimensions trigonometric proof.
Run: python CHECK.py
Requires Python 3 and NumPy.
"""
import math
import numpy as np

checks = 0

def dirichlet_squared(b, q):
    if q == 0:
        return np.zeros(b)
    j = np.arange(b)
    theta = np.pi * j / b
    out = np.empty(b, dtype=float)
    out[0] = float(q*q)
    out[1:] = (np.sin(q*theta[1:]) / np.sin(theta[1:]))**2
    return out

# Matrix-level singular-value test, independent of the decomposition formula.
for a in range(1, 5):
    for b in range(2, 10):
        n = a*b
        j = np.arange(n)
        for r in range(1, n+1):
            g = np.zeros(n)
            g[:r] = 1
            columns = [np.roll(g,a*k)*np.exp(2j*np.pi*l*j/a)
                       for k in range(b) for l in range(a)]
            X = np.column_stack(columns)
            obtained = np.linalg.svd(X,compute_uv=False)**2
            q,s = divmod(r,a)
            expected = np.concatenate([a*dirichlet_squared(b,q+(u<s))
                                       for u in range(a)])
            assert np.allclose(np.sort(obtained),np.sort(expected),rtol=2e-9,atol=2e-8)
            checks += 1

# All admissible overlapping interval lengths: exact optimizers and sharp ratio.
for b in range(3, 152, 2):
    alpha = math.pi/(2*b)
    target = 1/(math.sin(alpha)**2)
    for a in range(1, 8):
        optimizers = []
        for r in range(a+1,a*b+1):
            q,s = divmod(r,a)
            qlist = [q+(u<s) for u in range(a)]
            if any(math.gcd(v,b) != 1 for v in qlist):
                continue
            spec = np.concatenate([dirichlet_squared(b,v) for v in qlist])
            cond = float(max(spec)/min(spec))
            assert cond >= target*(1-2e-8), (a,b,r,cond,target)
            if abs(cond/target-1)<2e-8:
                optimizers.append(r)
            checks += 1
        assert optimizers == list(range(a+1,2*a+1)), (a,b,optimizers)
        checks += 1

# A quantitative check of the strict Dirichlet-kernel inequality.
for b in range(3, 502, 2):
    alpha = math.pi/(2*b)
    for q in range(3,b):
        if math.gcd(q,b)>1:
            continue
        m = min(dirichlet_squared(b,q)[1:])**0.5
        assert m < q*math.sin(alpha)*(1-1e-10), (b,q,m)
        checks += 1

print('PASS:',checks,'finite checks. Universal claim uses the analytic proof.')
