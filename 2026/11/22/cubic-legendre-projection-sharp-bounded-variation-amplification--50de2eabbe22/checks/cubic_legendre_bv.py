#!/usr/bin/env python3
"""Exact-rational certificate of degree-3 Legendre BV stability (no external libraries)."""
from fractions import Fraction as Q
from math import comb
from functools import reduce

R=Q(15,32)
# q(t,x) = derivative of the cubic Legendre projection of a unit step at t
# represented as list of t-power coefficients for x^j, j=0,1,2.
P=[[3*R,Q(0),-10*R,Q(0),7*R],
   [Q(0),8*R,Q(0),-8*R,Q(0)],
   [-7*R,Q(0),42*R,Q(0),-35*R]]

def bernstein_coefficients(a,h):
    out=[[Q(0)]*3 for _ in range(5)]
    for j in range(3):
        p=[sum(P[j][k]*comb(k,i)*a**(k-i)*h**i for k in range(i,5)) for i in range(5)]
        for k in range(5):
            out[k][j]=sum(p[i]*Q(comb(k,i),comb(4,i)) for i in range(k+1))
    return out

def absolute_integral_upper(c, bits=40):
    """Provable upper bound for integral_-1^1 |C+B*x+A*x*x| dx.

    The cuts are roots approximated on monotonicity intervals by exact
    bisection. A misplaced root changes the sign allocation only within
    2^-bits of that root, yielding a conservative 4*M*2^-bits error.
    """
    C,B,A=map(Q,c)
    def f(x):return (A*x+B)*x+C
    def prim(x):return A*x**3/3+B*x*x/2+C*x
    pts=[Q(-1)]
    if A:
        vertex=-B/(2*A)
        if -1<vertex<1:pts.append(vertex)
    pts.append(Q(1))
    rr=[]
    for l,r in zip(pts[:-1],pts[1:]):
        if f(l)==0 or f(r)==0 or f(l)*f(r)>0:continue
        L,H=l,r
        sign0=f(L)>0
        for _ in range(bits):
            mid=(L+H)/2
            if (f(mid)>0)==sign0 and f(mid)!=0:L=mid
            else:H=mid
        rr.append((L+H)/2)
    knots=sorted(set(pts+rr))
    approx=sum(abs(prim(b)-prim(a)) for a,b in zip(knots[:-1],knots[1:]))
    M=abs(A)+abs(B)+abs(C)
    return approx+Q(4*len(rr),2**bits)*M

def legendre_derived_derivative(t):
    # Independent moment reconstruction from the first five Legendre polynomials.
    p0=Q(1)
    p1=t
    p2=(3*t*t-1)/2
    p3=(5*t**3-3*t)/2
    p4=(35*t**4-30*t*t+3)/8
    c1=(p0-p2)/2
    c2=(p1-p3)/2
    c3=(p2-p4)/2
    return [c1-Q(3,2)*c3, 3*c2, Q(15,2)*c3]

def main():
    for t in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        direct=[sum(P[j][k]*t**k for k in range(5)) for j in range(3)]
        assert direct==legendre_derived_derivative(t)
    print('EXACT_LEGENDRE_MOMENT_POLYNOMIAL_IDENTITY_PASS')
    # Exact rational comparison first: 1.8 is strictly below the true
    # central-step variation 15/4 sqrt(3/7)-5/8.
    assert Q(3,7)>Q(97,150)**2
    # For 0<t<=1/10 use the strict monotonicity of the positive-root
    # integral, and increasing positive signed integral, proved in RESULT.md.
    # For 1/10<=t<=1 the following is a continuum covering certificate.
    biggest=Q(0)
    worst=None
    count=0
    for j in range(5,50):
        a=Q(j,50)
        for k,coeff in enumerate(bernstein_coefficients(a,Q(1,50))):
            bound=absolute_integral_upper(coeff)
            if bound>biggest:biggest=bound;worst=(j,k)
            if bound>=Q(9,5):raise AssertionError((j,k,float(bound)))
            count+=1
    print('EXACT_RATIONAL_BERNSTEIN_CONTINUUM_CERTIFICATE_PASS',count,
          'greatest_upper',float(biggest),'attained_at_interval_and_coefficient',worst)
    assert biggest<Q(9,5)
    print('EXACT_CENTRAL_JUMP_STRICT_THRESHOLD_PASS')
    print('ALL_CUBIC_LEGENDRE_BV_CERTIFICATES_PASS')
if __name__=='__main__':main()
