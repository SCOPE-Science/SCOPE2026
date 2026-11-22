"""Finite diagnostics for exact alias-pair kernel radius in weighted Wiener classes.

Run with Python 3 standard library. These tests corroborate, but do not
replace, the analytic proof covering infinite Fourier series.
"""
import cmath
import math
import random


def one_dim_sum(m, r):
    return min((1 + a)**r + (1 + m - a)**r for a in range(m + 1))


def formula_sum(m, r):
    if r < 1:
        return 1 + (1 + m)**r
    if r == 1:
        return m + 2
    return (1 + m//2)**r + (1 + (m + 1)//2)**r


def two_mode(m, r):
    if r < 1:
        return 0, m
    return -(m//2), m - (m//2)


checks = 0
for m in range(1, 28):
    for r in (0.2, 0.6, 0.99, 1, 1.01, 1.5, 2, 3.5):
        predicted = formula_sum(m, r)
        direct = one_dim_sum(m, r)
        assert math.isclose(predicted, direct, rel_tol=1e-12, abs_tol=1e-12)
        # Broader exact pair search; triples of aliases are not used here.
        ext = min((1+abs(k))**r + (1+abs(ell))**r
                  for k in range(-3*m, 3*m+1)
                  for ell in range(k+1, 3*m+1)
                  if (k-ell)%m == 0)
        assert math.isclose(predicted, ext, rel_tol=1e-12, abs_tol=1e-12)
        k, ell = two_mode(m, r)
        # One particular two-mode invisible witness.
        if r == 1:
            k,ell = 0,m
        assert (k-ell)%m == 0
        weight=(1+abs(k))**r+(1+abs(ell))**r
        assert math.isclose(weight, predicted, rel_tol=1e-12)
        amp = 1 / weight
        norm = (2**.5)*amp
        assert math.isclose(norm, math.sqrt(2)/predicted,rel_tol=1e-12)
        for j in range(m):
            t=j/m
            assert abs(amp*(cmath.exp(2j*math.pi*k*t)-cmath.exp(2j*math.pi*ell*t))) < 2e-12
            checks += 1

# Independent finite Fourier-nullspace tests: choose random complex
# coefficients in several alias classes with zero sum, check the bound.
rng=random.Random(170349)
for m in range(1, 17):
    for r in (0.35, 1, 2.2):
        B=math.sqrt(2)/formula_sum(m,r)
        for trial in range(125):
            coeff=[]
            for residue in range(m):
                frequencies=[residue+m*t for t in (-2,-1,0,1,2)]
                zs=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(4)]
                zs.append(-sum(zs))
                coeff.extend(zip(frequencies,zs))
            cost=sum(((1+abs(k))**r)*abs(z) for k,z in coeff)
            signal=math.sqrt(sum(abs(z)**2 for k,z in coeff))
            assert signal <= B*cost*(1+1e-12)
            checks += 1

# For product weights, direct pair optimization over a finite search box
# agrees with the axis formula for nontrivial 2D examples.
for m1,m2,r1,r2 in ((2,3,.5,2),(3,5,1,1),(4,2,2,1.6),(2,2,.8,.9),(3,4,2,2)):
    candidate=min(formula_sum(m1,r1),formula_sum(m2,r2))
    frequencies=[(i,j) for i in range(-2*m1,2*m1+1) for j in range(-2*m2,2*m2+1)]
    best=1e100
    for a,(i,j) in enumerate(frequencies):
        for k,ell in frequencies[a+1:]:
            if (k-i)%m1 or (ell-j)%m2: continue
            c=(1+abs(i))**r1*(1+abs(j))**r2+(1+abs(k))**r1*(1+abs(ell))**r2
            best=min(best,c)
    assert math.isclose(candidate,best,rel_tol=1e-12)
    checks+=1

print('WEIGHTED_WIENER_ALIAS_KERNEL_FINITE_CHECK_OK', checks)
