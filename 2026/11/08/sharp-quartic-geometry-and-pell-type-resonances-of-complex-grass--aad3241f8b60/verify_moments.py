#!/usr/bin/env python3
"""Exact checks for complex Grassmannian fourth-moment identities.

Requires Python 3 and SymPy. Does not use numerical sampling as a proof.
"""
import sympy as sp

n, k = sp.symbols('n k', integer=True, positive=True)
parts = [
    ((4,), 1, 1, 1),
    ((3,1), 3, -1, -1),
    ((2,2), 2, 2, 0),
    ((2,1,1), 3, -1, 1),
    ((1,1,1,1), 1, 1, -1),
]

def content_ratio(partition):
    return sp.prod((k+j-i)/(n+j-i)
                   for i, length in enumerate(partition, 1)
                   for j in range(1, length+1))

alpha = sum(sp.Rational(f*chi22,8)*content_ratio(lam)
            for lam,f,chi22,chi4 in parts)
beta = sum(sp.Rational(f*chi4,4)*content_ratio(lam)
           for lam,f,chi22,chi4 in parts)
w = k*(n-k)
T = (n*n-9)*(n*n-4)*(n*n-1)
alpha_goal = 3*w*(w*(n*n+6)-4*n*n+6)/(n*n*T)
beta_goal = 6*w*(n*n+1-5*w)/(n*T)
variance = w/(n*(n*n-1))
assert sp.factor(alpha-alpha_goal) == 0
assert sp.factor(beta-beta_goal) == 0
assert sp.factor(alpha_goal/variance**2-3*(n*n-1)*(w*(n*n+6)-4*n*n+6)/(w*(n*n-9)*(n*n-4))) == 0
assert sp.factor(beta_goal/variance**2-6*n*(n*n-1)*(n*n+1-5*w)/(w*(n*n-9)*(n*n-4))) == 0
print('EXACT_SCHUR_CHARACTER_EXPANSION_AND_VARIANCE_OK')

# Independently use complex projective (rank-one) Dirichlet moments.
rank1_alpha = 3/(n*(n+1)*(n+2)*(n+3))
rank1_beta = 6/(n*(n+1)*(n+2)*(n+3))
assert sp.factor(alpha_goal.subs(k,1)-rank1_alpha) == 0
assert sp.factor(beta_goal.subs(k,1)-rank1_beta) == 0
print('EXACT_INDEPENDENT_RANK_ONE_DIRICHLET_SPECIALIZATION_OK')

for N in range(4,51):
    lo = sp.Rational(1,N) if N%2 == 0 else sp.Rational(N*N+3, N*(N*N-1))
    hi = sp.Rational(N*N-3*N+3,N*(N-1))
    vals = []
    for m in range(1,N):
        v = sp.Rational(N, m*(N-m))-sp.Rational(3,N)
        vals.append(v)
        # Two-level zero-sum representative: m copies N-m and N-m copies -m.
        power2 = m*(N-m)**2+(N-m)*m**2
        power4 = m*(N-m)**4+(N-m)*m**4
        assert v == sp.Rational(power4,power2**2)
    assert lo == min(vals) and hi == max(vals)
print('EXACT_ALL_TWO_LEVEL_SPECTRAL_ENDPOINTS_N4_TO_50_OK')

for N in range(4,61):
    for K in range(1,N):
        M=N*N+1-5*K*(N-K)
        v=sp.factor((beta_goal/variance**2).subs({n:N,k:K}))
        assert sp.sign(v)==sp.sign(M)
print('EXACT_RANK_DIMENSION_PHASE_SIGN_N4_TO_60_OK')

for N,K in [(7,2),(18,5),(47,13),(123,34)]:
    assert N*N+1 == 5*K*(N-K)
    assert beta_goal.subs({n:N,k:K})==0
    target=sp.Rational(3*(N*N-1),N*N+1)
    actual=sp.cancel((alpha_goal/variance**2).subs({n:N,k:K}))
    assert actual == target
print('EXACT_RESONANT_EUCLIDEAN_FOURTH_MOMENTS_OK')

# Check the equality family from the Lucas/Fibonacci identity L_{2j}^2-5F_{2j}^2=4.
for j in range(2,20):
    N=sp.lucas(2*j); q=sp.fibonacci(2*j)
    assert N*N-5*q*q==4
    assert (N-q)%2==0
    K=(N-q)//2
    assert N*N+1==5*K*(N-K)
print('EXACT_INFINITE_LUCAS_FIBONACCI_RESONANCE_FAMILY_OK')

# Nonvanishing third moment in the flat case avoids a false spherical 4-design conclusion.
third = 2*k*(k-n)*(2*k-n)/(n*(n*n-1)*(n*n-4))
assert third.subs({n:7,k:2}) != 0
print('THIRD_MOMENT_DESIGN_LIMITATION_CHECK_OK')
print('ALL_COMPLEX_GRASSMANNIAN_CHECKS_OK')
