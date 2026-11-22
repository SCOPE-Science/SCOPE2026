"""Reproducible symbolic and numerical checks for an antipodal-pair flex theorem.
Run: python checker.py (Python 3, SymPy installed).
Analytic proof, not these finite tests, establishes the infinite-family conclusions.
"""
import cmath
import math
import sympy as sp

x = sp.Symbol('x')

def signs(m):
    if m & (m - 1) == 0:
        raise ValueError('odd factor required')
    d = next(d for d in range(3, m+1, 2) if m%d == 0)
    q = m//d
    return d, q, [(-1)**(j//q) for j in range(m)]

def verify(n):
    m = n//2
    assert n >= 6 and n%2 == 0
    d,q,sigma = signs(m)
    Q = sum(sig*x**j for j,sig in enumerate(sigma))
    assert sp.rem(Q,sp.cyclotomic_poly(n,x),x) == 0
    zeta = cmath.exp(2j*math.pi/n)
    vertices = [.5*zeta**j for j in range(n)]
    t = 2e-4/n
    a0 = vertices[1]-vertices[0]
    w0 = 1j*a0/abs(a0)
    shifts = [0j]
    for j in range(m-1):
        shifts.append(shifts[-1]+t*sigma[j]*w0*zeta**j)
    full = [vertices[j]+shifts[j%m] for j in range(n)]
    edges = [abs(full[(j+1)%n]-full[j]) for j in range(n)]
    theoretical = math.hypot(math.sin(math.pi/n),t)
    assert max(abs(a-theoretical) for a in edges) < 3e-12
    assert abs(sum(sigma[j]*zeta**j for j in range(m)))<1e-12
    ds = [abs(full[j]-full[k]) for j in range(n) for k in range(j)]
    assert abs(max(ds)-1.0)<3e-12
    assert all(abs(full[j+m]-full[j]) > 1 - 3e-12 for j in range(m))
    assert all((full[(j+1)%n].real-full[j].real)*(full[(j+2)%n].imag-full[(j+1)%n].imag) -
               (full[(j+1)%n].imag-full[j].imag)*(full[(j+2)%n].real-full[(j+1)%n].real) > 0 for j in range(n))
    assert n*theoretical > n*math.sin(math.pi/n)
    return n,d,q

if __name__=='__main__':
    for n in [6,10,12,14,18,20,22,24,26,28,30,34,36,38,40,42,44,46,48,50,54,60,66,70]:
        print('verified:', verify(n))
    for n in [4,8,16,32,64]:
        m=n//2
        assert sp.cyclotomic_poly(n,x)==x**m+1
    print('All symbolic and finite-geometric tests passed.')
