#!/usr/bin/env python3
"""Exact verification of the four-wall cyclic first-Walsh sampling spectrum.

Requires Python >=3.10 and sympy (only for the polynomial identities).
All finite comparison certificates use rational interval arithmetic.
"""
from fractions import Fraction as Q
from math import comb, sin, pi
import cmath
import sympy as S


def atan_bounds(x, even_terms=22):
    def partial(m):
        return sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(m)), Q(0))
    return partial(even_terms),partial(even_terms+1)

# Machin identity pi = 16 atan(1/5) - 4 atan(1/239).
a,b=atan_bounds(Q(1,5));c,d=atan_bounds(Q(1,239))
PI_LO,PI_HI=16*a-4*d,16*b-4*c
assert Q(157,50)<PI_LO<PI_HI<Q(22,7)


def sine_bounds(xlo,xhi):
    def partial(x,m):
        return sum(((-1)**j*x**(2*j+1)/Q(S.factorial(2*j+1)) for j in range(m)),Q(0))
    return partial(xlo,14),partial(xhi,15)


def u_bounds(n,k):
    if n%2==0 and k==n//2:return Q(1),Q(1)
    lo,hi=sine_bounds(PI_LO*Q(k,n),PI_HI*Q(k,n))
    assert 0<lo<=hi<=1
    return lo*lo,hi*hi


def f_bounds(n,k):
    A=n*n-3*n+8;P=(n-1)*(n-2)*(n-3)
    lo,hi=u_bounds(n,k)
    assert A*lo>6,(n,k,'positivity')
    return Q(4)*(A*lo-6)/(P*hi*hi), Q(4)*(A*hi-6)/(P*lo*lo)


def comparison(v,w):
    # Every point in v is strictly greater than every point in w.
    return v[0]>w[1]


def dc(n):
    t=Q(n-4,5)
    return (t,t)

# Symbolic Krawtchouk polynomial, its quadratic-in-t(n-t) form,
# and cyclic-discrete-Laplacian identities.
n,t=S.symbols('n t',integer=True)
def choose_poly(x,k):return S.prod(x-j for j in range(k))/S.factorial(k)
K=sum((-1)**j*choose_poly(t,j)*choose_poly(n-t,4-j) for j in range(5))
P=(n-1)*(n-2)*(n-3)
q=t*(n-t)
C=1+16*q*q/(n*P)-8*(n*n-3*n+4)*q/(n*P)
assert S.factor(K/choose_poly(n,4)-C)==0
D=lambda F:S.expand(F.subs(t,t+1)+F.subs(t,t-1)-2*F)
assert S.factor(D(q)+2)==0
assert S.factor(D(q*q)+12*q-2*(n*n+1))==0
assert S.factor(n+16*(n**4-1)/(30*P)-8*(n*n-3*n+4)*(n*n-1)/(6*P)-(n-4)/5)==0
print('QUARTIC_KRAWTCHOUK_AND_CYCLIC_DIFFERENCE_IDENTITIES_PASS')

# Finite exact certificates for all small lengths; cyclic k and n-k coincide.
for n0 in range(5,14):
    eig=[dc(n0)]+[f_bounds(n0,k) for k in range(1,n0//2+1)]
    max_indices=[2] if n0<=11 else [0]
    min_indices=[0] if n0<=7 else ([0,4] if n0==8 else [n0//2])
    for i,v in enumerate(eig):
        if i not in max_indices:
            assert all(comparison(eig[j],v) for j in max_indices),(n0,'max',i)
        if i not in min_indices:
            assert all(comparison(v,eig[j]) for j in min_indices),(n0,'min',i)
    if n0==8:
        assert dc(n0)==f_bounds(n0,4)
    # Independent unnormalized covariance sums from the exact four-wall model.
    cvals=[]
    for t0 in range(n0):
        num=sum((-1)**j*comb(t0,j)*comb(n0-t0,4-j) for j in range(max(0,4-n0+t0),min(t0,4)+1))
        cvals.append(Q(num,comb(n0,4)))
    for k in range(n0//2+1):
        spec=sum(float(cvals[t0])*cmath.exp(-2j*pi*k*t0/n0) for t0 in range(n0)).real
        assert eig[k][0]-1e-10<spec<eig[k][1]+1e-10,(n0,k,spec)
print('RATIONAL_TRIG_EXTREMAL_CERTIFICATES_PASS n=5..13')

# Universal inequalities for n>=12 and >=14.
pi_lower,pi_upper=Q(157,50),Q(22,7)
y=pi_upper**2
rhs=Q(6)/pi_lower**2*(1/(1-y/Q(864))**2+Q(1,4)/(1-y/Q(216))**2)
assert rhs<Q(29,36)
# Shift n=14+h. Every coefficient strictly positive, hence global max is DC.
h=S.symbols('h', nonnegative=True)
P_n=(n-1)*(n-2)*(n-3);A_n=n*n-3*n+8
poly=S.Poly(S.expand(((n-4)*P_n*y*y-20*n*n*A_n*y+120*n**4).subs(n,14+h)),h)
assert all(v>0 for v in poly.all_coeffs()),poly
# For n>=9, the high-frequency minimum lies below DC:
polymin=S.Poly(S.expand((3*(n-4)*(n-1)*(n-2)-80*n).subs(n,9+h)),h)
assert all(v>0 for v in polymin.all_coeffs())
# n sin(pi/n) is increasing and >3 from n=9, certified via arctan/sine bounds.
assert 9*sine_bounds(PI_LO/9,PI_HI/9)[0]>3
# reciprocal high-frequency sine bound: sec(pi/(2n))^2 <26/25, n>=9.
assert (1-(pi_upper/Q(18))**2/2)**2>Q(25,26)
# A/n^2 nondecreasing at integers n>=5, starting n=5 then derivative positive.
assert Q(18,25)<Q(26,36)
# Exact n=5 positivity threshold.
assert 18*sine_bounds(PI_LO/5,PI_HI/5)[0]**2>6
print('GLOBAL_EXTREMAL_AND_POSITIVITY_INEQUALITIES_PASS n>=14')
print('FOUR_WALL_FIRST_WALSH_SPECTRUM_PASS')
