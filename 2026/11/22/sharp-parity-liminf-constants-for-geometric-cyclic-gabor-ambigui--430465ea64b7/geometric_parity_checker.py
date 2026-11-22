"""Numerical consistency checks for the parity-liminf theorem.
Use: python geometric_parity_checker.py  (requires NumPy).
Finite checks supplement, but do not prove, the asymptotic theorem.
"""
import math
import numpy as np

A = math.log(2)
THETA = math.atan2(3, 4)
C_ODD = (10.0 / 9) * math.sqrt(5.0 / 2) * A * A
C_EVEN = (20.0 / 9) * A * A

def formula(n, k, ell):
    q = math.exp(2 * A / n)
    u = q * np.exp(2j * np.pi * ell / n)
    w = (8.0 + 6j) / 5.0
    return (math.sqrt(5) / 3) * math.exp(-A * k / n) * (q - 1) * abs(u ** k - w) / abs(1-u)

def brute(n, k, ell):
    gam = np.exp((A + 0.5j * np.pi) / n)
    v = np.array([gam ** j for j in range(n)], dtype=complex)
    v /= np.linalg.norm(v)
    return abs(np.sum(np.conj(v) * np.exp(2j * np.pi * ell * np.arange(n) / n) * np.roll(v, k)))

def minimum(n):
    q = math.exp(2*A/n)
    u = q * np.exp(2j*np.pi*np.arange(n)/n)
    w = (8+6j)/5
    den = np.abs(1-u)
    coeff = math.sqrt(5)*(q-1)/3
    minv = (float('inf'), -1, -1)
    for k in range(n):
        vals = coeff*math.exp(-A*k/n) * np.abs(u**k-w)/den
        ell = int(np.argmin(vals))
        val = float(vals[ell])
        if val < minv[0]:minv=(val,k,ell)
    return minv

if __name__=='__main__':
    checked = 0
    for n in range(2,25):
        for k in range(n):
            for ell in range(n):
                lhs, rhs = brute(n,k,ell), formula(n,k,ell)
                assert math.isclose(lhs, rhs, rel_tol=2e-9, abs_tol=1e-12), (n,k,ell,lhs,rhs)
                checked += 1
    samples=[]
    for n in [400, 401, 869, 1738]:
        v,k,ell=minimum(n)
        c=C_ODD if n%2 else C_EVEN
        assert n*n*v >= c - 0.02, (n,n*n*v,c)
        samples.append((n,k,ell,n*n*v,c))
    # Construct explicit resonance indices without enumerating all modes.
    # Their scaled values approach the parity constants along dense subsequences.
    nearly=[]
    for n in [6249,12498,36625,30376]:
        if n%2:
            k=(n+1)//2
            target=n*THETA/math.pi
            ell=2*round(target/2)
        else:
            k=n//2+1
            target=n*(0.5+THETA/(2*math.pi))
            ell=2*round((target-1)/2)+1
        val=n*n*formula(n,k,ell)
        c=C_ODD if n%2 else C_EVEN
        assert abs(val-c)<0.005,(n,val,c)
        nearly.append((n,k,ell,val,c))
    print('CHECK_OK direct_coefficients=%d finite_minima=%d near_resonances=%d' %(checked,len(samples),len(nearly)))
    print('C_odd=%.12f C_even=%.12f' %(C_ODD,C_EVEN))
    for r in samples:print('finite',r)
    for r in nearly:print('resonant',r)
