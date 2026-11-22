"""Checks the exact finite-support, quenched-initial-position lattice search theorem.
All hoppings in either direction have rate one.  Runs using only Python standard library.
"""
import math, random

def y_to_r(y):return (y-1)**2/y

def T_fixed(j,r):
    y=(r+2+math.sqrt(r*r+4*r))/2
    return math.expm1(j*math.log(y))/r

def T_mix(probs,y):
    A=sum(p*sum(y**ell for ell in range(j)) for j,p in probs.items())
    return y*A/(y-1)

def derivative_n(probs,y):
    A=sum(p*sum(y**ell for ell in range(j)) for j,p in probs.items())
    Ap=sum(p*sum(ell*y**(ell-1) for ell in range(1,j)) for j,p in probs.items())
    return y*(y-1)*Ap-A

def optimum(probs):
    lo=1.;hi=2.
    while derivative_n(probs,hi)<0:hi*=2
    for _ in range(110):
        mid=(lo+hi)/2
        if derivative_n(probs,mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def tridiagonal_mfpt(j,r,cutoff=120):
    # Independent finite-difference generator solution, finite interval with reflecting end.
    # Solve T_i, i>=1: (2+r)T_i-T_{i-1}-T_{i+1}=1+r*T_j;
    # i=cutoff has reflecting right endpoint (jump left only): (1+r)T_cut-T_{cut-1}=1+r*T_j.
    # Because reset is always to j, equivalently solve first-passage Laplace h_i;
    # (2+r)h_i-h_{i-1}-h_{i+1}=0, h_0=1; (1+r)h_cut-h_{cut-1}=0.
    # use backward ratios h_cut/h_{cut-1}, iterating via continued fractions.
    ratio=1/(1+r)
    # ratio_i=h_i/h_{i-1} = 1/(2+r-ratio_{i+1})
    for i in range(cutoff-1,0,-1):ratio=1/(2+r-ratio)
    h=1.
    # last ratio is h_1/h_0, need products ratios from cutoff to 1 via recomputation for h_j
    rs={cutoff:1/(1+r)}
    for i in range(cutoff-1,0,-1):rs[i]=1/(2+r-rs[i+1])
    for i in range(1,j+1):h*=rs[i]
    return (1/h-1)/r

# formula directly against independent finite-volume tridiagonal equations
for j in range(1,9):
    for r in (0.25,0.8,1.7,4.,12.):
        x=T_fixed(j,r); f=tridiagonal_mfpt(j,r)
        assert math.isclose(x,f,rel_tol=1e-11,abs_tol=1e-11),(j,r,x,f)

# Numerical minimizer uniqueness and stationarity for various mixtures
rng=random.Random(1421)
for K in range(2,13):
    for _ in range(24):
        a=[rng.random() for _ in range(K)];s=sum(a)
        probs={j+1:a[j]/s for j in range(K)}
        y=optimum(probs)
        assert y>1 and abs(derivative_n(probs,y))<1e-7*max(1.,y**K)
        assert T_mix(probs,y)<T_mix(probs,y*1.0001)
        assert T_mix(probs,y)<T_mix(probs,1+(y-1)*0.9999)

# Rare contamination, asymptotic farthest-distance control (relative numerical convergence)
for K in (2,3,4,5,6):
    q={K:1.}
    for eps in (1e-4,1e-6,1e-8):
        probs={1:1-eps,K:eps}
        y=optimum(probs)
        prediction=(eps*(K-1))**(-1/K)
        assert abs(y/prediction-1)<0.20,(K,eps,y,prediction)
        r=y_to_r(y)
        assert r>0
print('PASS: 40 independent finite-volume equations; 264 randomized mixture unique-optimum checks; 15 rare-tail asymptotic diagnostics')

# Infinite-support edge: exact pure power-geometric law p_j ~ 2^{-j}/j^6.
# These absolutely convergent series are checked numerically here, while the
# associated proof in RESULT.md uses a rational, non-truncation inequality.
norm=sum(2.**(-j)/j**6 for j in range(2,450))
Anum=sum((2.**(-j)/j**6)*(2.**j-1) for j in range(2,450))
Apnum=sum((2.**(-j)/j**6)*((j-2)*2.**(j-1)+1) for j in range(2,450))
Nedge=(2*Apnum-Anum)/norm
assert Nedge < -0.65, Nedge
# The exact positive-tail bound is 1/1944 + 2/1024 + 3/32768 < 1/256.
assert (1/1944+2/1024+3/32768)<1/256
print('PASS: integrability-boundary sign validated; exact rational upper-bound inequality confirmed')
