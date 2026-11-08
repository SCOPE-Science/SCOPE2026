"""Checks for Gaussian sliced-Wasserstein orthogonal quadrature risk.

Scientific check only.  The general theorem is proved analytically in RESULT.md.
Standard-library Python 3; no external data or dependencies.
"""
from fractions import Fraction
from math import cos, sin, sqrt, pi

checks = 0
Q = Fraction

# Exact rational moment-coefficient identities, for a range of m and r.
for mi in range(-5, 6):
    for ri in range(1, 9):
        m = Q(mi, 3)
        r = Q(ri, 5)
        single = (16*m*m*r*r + r**4) / 128
        iid = single / 2
        orth = r**4 / 128
        covariance = (r**4 - 16*m*m*r*r) / 128
        assert (single + covariance)/2 == orth
        checks += 1
        assert orth / iid == 2*r*r/(r*r+16*m*m)
        checks += 1
        assert (orth > iid) == (r > 4*abs(m))
        checks += 1

N = 8192
angles = [2*pi*j/N for j in range(N)]

def values(B, C, eps):
    out = []
    for t in angles:
        x, y = cos(t), sin(t)
        a = B[0][0]*x*x + 2*B[0][1]*x*y + B[1][1]*y*y
        b = C[0][0]*x*x + 2*C[0][1]*x*y + C[1][1]*y*y
        out.append((sqrt(1+eps*a) - sqrt(1+eps*b))**2)
    return out

def variance(vals):
    mu = sum(vals)/len(vals)
    return sum((z-mu)**2 for z in vals)/len(vals)

# Compare the complete nonlinear Gaussian integrand to the theoretical limit.
for B, C in [
    (((2.,0.),(0.,0.)), ((0.,0.),(0.,0.))),
    (((1.,0.),(0.,-1.)), ((0.,0.),(0.,0.))),
    (((5.1,0.),(0.,-3.1)), ((0.,0.),(0.,0.))),
    (((1.,0.7),(0.7,-1.)), ((0.2,-0.1),(-0.1,0.3))),
]:
    D11, D22 = B[0][0]-C[0][0], B[1][1]-C[1][1]
    D12 = B[0][1]-C[0][1]
    m = (D11+D22)/2
    r2 = ((D11-D22)/2)**2 + D12**2
    expected = 2*r2/(r2+16*m*m)
    vals = values(B,C,0.001)
    paired = [(vals[i]+vals[(i+N//4)%N])/2 for i in range(N)]
    actual = variance(paired)/(variance(vals)/2)
    assert abs(actual-expected) < 0.005, (B,C,actual,expected)
    checks += 1

# The sharp factor two is attained exactly, not only asymptotically.
for a, b in [(2.,1.), (4.,.5), (1.02,.98)]:
    for j in range(1, 400):
        t = (j+.271)*pi/701
        x,y = cos(t),sin(t)
        A = a*x*x+b*y*y
        B = b*x*x+a*y*y
        g = (sqrt(A)-sqrt(B))**2
        g_orth = (sqrt(B)-sqrt(A))**2
        assert abs(g-g_orth)<1e-13
        checks += 1
    grid = []
    for t in angles:
        x,y = cos(t),sin(t)
        grid.append((sqrt(a*x*x+b*y*y)-sqrt(b*x*x+a*y*y))**2)
    assert variance(grid) > 1e-12
    checks += 1
    paired = [(grid[i]+grid[(i+N//4)%N])/2 for i in range(N)]
    assert abs(variance(paired)/(variance(grid)/2)-2)<1e-10
    checks += 1

print(f"PASS: {checks} deterministic coefficient, asymptotic and exact-symmetry checks")
print("Analytic proof establishes all fixed-matrix small-perturbation assertions.")
