"""Finite diagnostics for a logarithmic singular-value law for Dirichlet Volterra operators.

The infinite-dimensional proof is in RESULT.md; finite tests do not prove that limit.
"""
import cmath
import math
from fractions import Fraction

checks = 0

def verify(condition, message):
    global checks
    assert condition, message
    checks += 1

def convolution_image(vector, weights):
    out = {}
    for n, x in vector.items():
        for m, coefficient in weights.items():
            out[m*n] = out.get(m*n, 0j) + coefficient*x
    return {n:z for n,z in out.items() if abs(z)>1e-12}

def squared_norm(v):
    return sum(abs(z)**2 for z in v.values())

def logarithm_diagonal(v):
    return {k:val/math.log(k) for k,val in v.items()}

def translate(v, r):
    return {r*n:z for n,z in v.items()}

# The normalized polynomial 1 + 2z - 3z^2 has an exact 64/3 squared maximum.
for j in range(1001):
    theta=2*math.pi*j/1000
    z=cmath.exp(1j*theta)
    magnitude=abs(1+2*z-3*z*z)**2
    t=math.cos(theta)
    verify(abs(magnitude-(20-8*t-12*t*t))<2e-12, 'trigonometric identity')
    verify(magnitude<=64/3+2e-12, 'sharp polynomial upper bound')
z=complex(-1/3,math.sqrt(8)/3)
verify(abs(abs(1+2*z-3*z*z)**2-64/3)<1e-12,'attained polynomial maximum')
verify(Fraction(20)-Fraction(8)*(-Fraction(1,3))-Fraction(12)*Fraction(1,9)==Fraction(64,3),'exact rational optimum')

# Multiplicative convolution is compatible with dilation; logarithmic division
# commutes with the coefficient formula for the Volterra operator.
weights={2:math.log(2),4:2*math.log(2),8:-3*math.log(2)}
x={1:1/3+1j/2,3:-1/4+1j/5,7:1/6-1j/8}
Bx=convolution_image(x,weights)
for r in range(1,100):
    translated=translate(x,r)
    actual=convolution_image(translated,weights)
    expected=translate(Bx,r)
    verify(actual.keys()==expected.keys(),'multiplicative translation support')
    for k in actual:
        verify(abs(actual[k]-expected[k])<1e-12,'commutation with translation')
    v=logarithm_diagonal(actual)
    direct={k:sum(coeff*xi for m,coeff in weights.items() for n,xi in translated.items() if m*n==k)/math.log(k) for k in actual}
    for k in actual:
        verify(abs(v[k]-direct[k])<1e-12,'Volterra coefficient identity')

# Pairwise disjoint supports give orthogonal inputs AND convolution images,
# with a quantitative cardinality fraction in each interval [R,2R].
H=set(x)|set(Bx)
C=len(H)**2+1
for R in (100,201,500,809):
    selected=[]
    occupied=set()
    for r in range(R,2*R+1):
        support={r*h for h in H}
        if support.isdisjoint(occupied):
            selected.append(r)
            occupied.update(support)
    verify(len(selected)>= (R+1)/C,'uniform disjoint packing bound')
    images=[]
    for r in selected:
        v=translate(Bx,r)
        images.append(v)
        image_norm=squared_norm(logarithm_diagonal(v))
        lower=squared_norm(Bx)/(math.log(2*R*max(Bx))**2)
        verify(image_norm+1e-13>=lower,'singular-value test-subspace bound')
    for i in range(len(images)):
        for j in range(i+1,len(images)):
            verify(set(images[i]).isdisjoint(images[j]),'orthogonal disjoint images')

# For a monomial symbol, all columns are mutually orthogonal and its exact
# singular values are |b_m| log(m)/log(m(n)) (with descending n).
for m in (2,3,5,12):
    for n in range(1,150):
        result=logarithm_diagonal(convolution_image({n:1}, {m:math.log(m)}))
        verify(len(result)==1,'single monomial shift')
        verify(abs(math.sqrt(squared_norm(result))-math.log(m)/math.log(m*n))<1e-14,'monomial exact singular value')
        if n<149:
            verify(math.log(m)/math.log(m*n)>math.log(m)/math.log(m*(n+1)),'singular sequence monotonic')
print('PASS',checks,'finite diagnostic assertions')
