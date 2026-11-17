"""Reproducible finite tests for the disjoint-event Fourier-commutator theorem.

These tests supplement, but do not replace, the analytical argument.
Requires Python 3.9+ and numpy.
"""
import math
import numpy as np

pi = math.pi

def radius(mass):
    return math.sin(pi * mass) / pi

def bound(masses):
    a,b,c = masses
    if min(masses) < -1e-13 or abs(sum(masses)-1)>1e-12:
        raise ValueError('masses must sum to one')
    if min(masses) <= 0:
        return 0.0
    masses=sorted(masses)
    if masses[2] >= 0.5:
        return radius(masses[0])*radius(masses[1])
    return pi*radius(a)*radius(b)*radius(c)

def interval_moment(start, fraction):
    if fraction == 0:
        return 0.0j
    return (math.sin(pi*fraction)/pi)*np.exp(2j*pi*(start+fraction/2))

def area(z,w):
    return abs((z*np.conj(w)).imag)

def gram_area(xs):
    x,y,z=xs
    return max(0.,(2*x*y+2*x*z+2*y*z-x*x-y*y-z*z)/4)**0.5

checks=0
# Every partition into three contiguous arcs attains the acute-triangle bound.
for i in range(1,30):
    for j in range(1,30):
        a,b=i/60,j/60
        c=1-a-b
        if c<=0 or max(a,b,c)>=.5:continue
        z1=interval_moment(0,a);z2=interval_moment(a,b)
        assert abs(area(z1,z2)-bound((a,b,c)))<4e-14
        checks+=1
# In the obtuse regime, orthogonal centered arcs attain the bound.
for i in range(1,48):
    for j in range(1,48):
        u=i/200;v=j/200
        if u+v >.5:continue
        z1=interval_moment(-u/2,u)
        z2=interval_moment(.25-v/2,v)
        assert abs(area(z1,z2)-bound((u,v,1-u-v)))<4e-14
        checks+=1
# Finite-grid circle events have moments from exact cell integrals, not point samples.
rng=np.random.default_rng(20611024)
for n in (30,60,90,150,240):
    j=np.arange(n)
    zcell=np.exp(2j*pi*(j+.5)/n)*(math.sin(pi/n)/pi)
    for rep in range(1000):
        colors=rng.integers(0,3,size=n)
        ms=[int(np.sum(colors==k))/n for k in (0,1,2)]
        zs=[np.sum(zcell[colors==k]) for k in (0,1,2)]
        assert abs(sum(zs))<1e-12
        assert area(zs[0],zs[1])<=bound(ms)+3e-13, (n,ms,area(zs[0],zs[1]),bound(ms))
        checks+=1
# Supporting-plane inequality: exact Heron Gram determinant and positive gradients.
for _ in range(10000):
    masses=rng.dirichlet([2,2,2])
    if max(masses)>=.5: continue
    R=np.array([radius(float(x)) for x in masses]);X=R*R
    D0=gram_area(X)
    weights=np.array([(X[(i+1)%3]+X[(i+2)%3]-X[i])/(4*D0) for i in range(3)])
    assert min(weights)>-1e-12
    # Random feasible triple: scale a contiguous partition's three Fourier vectors
    zs=[interval_moment(0,float(masses[0])),interval_moment(float(masses[0]),float(masses[1]))]
    zs.append(-sum(zs))
    # Equal contraction of all vectors preserves the sum-zero relation.
    t=float(rng.random());xs=np.array([abs(z*t)**2 for z in zs]);D=gram_area(xs)
    assert D<=float(weights@xs)+1e-12
    assert float(weights@xs) <= D0+1e-12
    checks+=1
# Direct qubit-block commutator normalization.
V=np.array([[0.,0.],[1.,0.]],dtype=complex)
for _ in range(300):
    za=rng.normal()+1j*rng.normal();zb=rng.normal()+1j*rng.normal()
    A=za*V+za.conjugate()*V.conj().T
    B=zb*V+zb.conjugate()*V.conj().T
    assert abs(np.linalg.norm(A@B-B@A,ord=2)-2*area(za,zb))<1e-11
    checks+=1
# The unrestricted disjoint-event maximum occurs for three equal arcs.
global_det=3*math.sqrt(3)/(8*pi*pi)
assert abs(bound((1/3,1/3,1/3))-global_det)<1e-14
assert global_det > radius(.25)**2
print(f'PASS: {checks} finite checks; global sharp determinant={global_det:.15f}')
