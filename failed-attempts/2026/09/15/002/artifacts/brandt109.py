"""Brandt matrices for definite quaternion algebra B=(-2,-109), disc 109.
Basis 1,i,j,k with i^2=-2, j^2=-109, k=ij=-ji. Reduced norm N(x)=x0^2+2 x1^2+109 x2^2+218 x3^2.
Maximal order O: disc 109 => d=109=1 mod 4? For B=(-2,-109), construct maximal order via standard recipe:
O = Z + Z*i + Z*(1+j)/2? Need (1+j)/2 integral: N((1+j)/2)=(1+109)/4=27.5 not integral! Try other.
General: O = Z*e1+...+e4 maximal iff disc(O)=109^2. Enumerate candidate superorders of the naive order and test maximality via discriminant.
"""
from fractions import Fraction
import itertools
import numpy as np

def gram(a,b):
    # inner product matrix of basis wrt norm form: G with N(x)=sum G_ij x_i x_j
    pass

# Work with coordinates in Q^4, norm form Q(x)=x0^2+2x1^2+109x2^2+218x3^2.
# Naive Lipschitz-type order L = Z + Z i + Z j + Z k: Gram diag(1,2,109,218), det = 2*109*218 = 4*109^2... disc(L)= (109^2)*4? sqrt: index 2 from maximal (since disc maximal = 109^2, disc L = 4*109^2 → [O:L]=2).
# So maximal O is an index-2 superorder: O = L + Z*v with 2v in L, v integral (N(v+x) integral for all x... integrality = trace+norm integral).
# Trace(x)=2x0. v=(c0,c1,c2,c3)/2 with ci in {0,1}: v integral iff N(v) in Z and Tr(v) in Z → c0 even?? Tr(v)=c0... need c0 in {0,2}? Let's brute force: find all v in (1/2)L/L with x+v integral whenever... simpler: O must be a ring containing L with [O:L]=2, closed under mult.
from fractions import Fraction
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(a,b):
    # (a0+a1 i+a2 j+a3 k)(b0+b1 i+b2 j+b3 k), i^2=-2, j^2=-109, k=ij
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (
      a0*b0 -2*a1*b1 -109*a2*b2 +218*a3*b3,
      a0*b1 + a1*b0 -109*a2*b3 +109*a3*b2,
      a0*b2 + a2*b0 -2*a3*b1 +2*a1*b3,   # check: j*k=jij=-i*j^2? ji=-k so j*(ij)=(ji)j=-kj=-(k j); kj=(ij)j=i j^2=-109 i → -kj=109 i?? Hmm need care.
      a0*b3 + a3*b0 + a1*b2 - a2*b1,
    )
