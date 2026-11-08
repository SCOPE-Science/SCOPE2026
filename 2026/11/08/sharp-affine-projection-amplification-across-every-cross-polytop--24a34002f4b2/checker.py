"""Exact rational checks of face-skeleton affine least-squares norms.

An alternate integration expands a beta density rather than using its
closed tail integral; no third-party dependencies.
"""
from fractions import Fraction as Q
from math import comb

def closed(d,s):
    return 1+Q(s+1,2)*(1-Q(2,d*(s+1)))**s

def alternate_integrated(d,s):
    alpha=Q(d*(s+1),2)
    a=1/alpha
    if s==1:
        tail=alpha-1
    else:
        # Integrate (alpha*u-1)*(s-1)*(1-u)^(s-2) termwise from a to 1.
        tail=Q(0)
        for j in range(s-1):
            factor=Q(s-1)*Q((-1)**j*comb(s-2,j))
            tail+=factor*(alpha*(1-a**(j+2))/Q(j+2)-(1-a**(j+1))/Q(j+1))
    return 1+Q(s,d)*tail

def covariance_by_dirichlet(d,s):
    # Chance coordinate i belongs to the random support, times
    # its exact second Dirichlet moment.
    return Q(s,d)*Q(2,s*(s+1))

def volume_closed(d):
    return 1+Q(d+2,2)*(1-Q(2,(d+1)*(d+2)))**(d+1)

N=0
for d in range(2,35):
    prev=None
    for s in range(1,d+1):
        a=alternate_integrated(d,s)
        b=closed(d,s)
        assert a==b,(d,s,a,b)
        assert covariance_by_dirichlet(d,s)==Q(2,d*(s+1))
        if prev is not None: assert prev<b
        prev=b
        N+=1
    assert prev<volume_closed(d)
print('EXACT_ALTERNATE_BETA_POLYNOMIAL_INTEGRALS_OK', N)
print('EXACT_FACE_SKELETON_COVARIANCES_OK', N)
print('EXACT_FACE_LEVEL_AND_SOLID_MONOTONICITY_SAMPLES_OK',33)

# Upper bound of error of first-order binomial approximation
for d in range(2,40):
    for s in range(1,d+1):
        rem=closed(d,s)-(1+Q(s+1,2)-Q(s,d))
        assert Q(0)<=rem<=Q(1,d)
print('UNIFORM_FIRST_ORDER_REMAINDER_CERTIFICATE_SAMPLES_OK')

# Verify the exact kernel norm by enumerating the zero-skeleton
# point mass distribution: 2d signed coordinate unit vectors.
for d in range(2,40):
    alpha=d
    row=Q(1,2*d)*sum(abs(1+alpha*sign*int(i==0)) for i in range(d) for sign in (-1,1))
    assert row==closed(d,1)
print('DIRECT_DISCRETE_VERTEX_KERNEL_NORMS_OK',38)

# First and second moments for the crosspolytope volume via radial coupling.
for d in range(2,40):
    # E[R^2]=d/(d+2) with density d*r^(d-1).
    m2=Q(d,d+2)
    assert m2*covariance_by_dirichlet(d,d)==Q(2,(d+1)*(d+2))
print('EXACT_VOLUME_RADIAL_MOMENTS_OK',38)
print('ALL_CROSSPOLYTOPE_SKELETON_PROJECTION_CHECKS_OK')
