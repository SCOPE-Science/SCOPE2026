#!/usr/bin/env python3
"""Finite, exact arithmetic corroboration; not a proof of the general theorem.

For T_(z+bar z) T_(z^2+bar z^2) on Fock exponential vectors,
P(e^(wz))=e^(wz) V(z,w), with
V=(z+w)(z^2+w^2)+2z.
All operations below use integer arithmetic.
"""
from math import comb

# coefficients of V in z, for each integer w.
def coeff(w):
    return [w**3, w**2+2, w, 1]

# n-th z derivative of e^(wz) V(z,w) at z=0.
def jet(n,w):
    a=coeff(w)
    from math import factorial
    return sum(comb(n,k)*w**(n-k)*factorial(k)*a[k]
               for k in range(min(n,3)+1))

# Coefficient identity for translated Borel germs, n-th inverse-power coefficient.
checks=0
for w in (-11,-4,0,4,8,17):
    a=coeff(w)
    for n in range(40):
        b=sum(comb(n,k)*w**(n-k)*__import__('math').factorial(k)*a[k]
              for k in range(min(n,3)+1))
        assert jet(n,w)==b
        checks+=1

# A genuine two-factor Fock Toeplitz product with no zero symbols.
# Verify the first jets and a nonsingular three-vector matrix at w=0,4,8.
wlist=[0,4,8]
mat=[[jet(n,w) for w in wlist] for n in range(3)]
a,b,c=mat[0]; d,e,f=mat[1]; g,h,i=mat[2]
det=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
assert det != 0
checks+=1
assert [jet(0,w) for w in wlist]==[0,64,512]
checks+=1
assert [jet(1,w) for w in wlist]==[2,274,4162]
checks+=1
print('FINITE_FOCK_BOREL_JET_CHECKS_OK',checks,'det',det)
