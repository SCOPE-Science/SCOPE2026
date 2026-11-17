"""Reproducible finite symbolic and high-precision checks of symmetric Lozi crisis shifts.
Run: python bcnf_crisis_check.py
Uses sympy and mpmath. The proof is analytic, not a finite enumeration.
"""
import sympy as sp
import mpmath as mp

S,D=sp.symbols('S D',positive=True)

def g(u,p,v,q):
    return v*v-2*q,q*q,u*v-p-q,p*q

def phi(u,p,v,q):
    ell=(u+sp.sqrt(u*u-4*p))/2
    return q-(v+p+q-(1+v)*ell)*ell

# Exact tangent and curvature of the first renormalized curve.
u,p,v,q=g(S,D,-S,D)
H=phi(u,p,v,q)
r=sp.sqrt(2)
assert sp.simplify(H.subs({S:r,D:0}))==0
assert sp.simplify(sp.diff(H,D).subs({S:r,D:0}))==0
assert sp.simplify(sp.diff(H,D,2).subs({S:r,D:0})-12)==0
assert sp.simplify(sp.diff(H,S).subs({S:r,D:0})+8*r)==0
assert sp.simplify(-sp.diff(H,D,2).subs({S:r,D:0})/(2*sp.diff(H,S).subs({S:r,D:0}))-3*r/8)==0

# First-order derivatives: direct differentiated g, compared with closed form.
U,V=S,-S
A,B=sp.Integer(0),sp.Integer(0)
P,Q=D,D
for n in range(1,9):
    # At D=0, perturbations of determinants are zero for n>=1.
    Un=sp.expand(V*V)
    Vn=sp.expand(U*V)
    if n == 1:
        An=Bn=sp.Integer(-2)
    else:
        An=sp.expand(2*V*B)
        Bn=sp.expand(A*V+U*B)
    U,V,A,B=Un,Vn,An,Bn
    a_expected=sp.Rational(2**n+8*(-1)**n,3)*S**(2**n-2)
    b_expected=sp.Rational(-2**n+4*(-1)**n,3)*S**(2**n-2)
    assert sp.expand(A-a_expected)==0, n
    assert sp.expand(B-b_expected)==0, n

mp.mp.dps=75

def gn(s,d,n):
    t=(s,d,-s,d)
    for _ in range(n):
        u,p,v,q=t
        t=(v*v-2*q,q*q,u*v-p-q,p*q)
    return t

def phin(s,d,n):
    u,p,v,q=gn(s,d,n)
    ell=(u+mp.sqrt(u*u-4*p))/2
    return q-(v+p+q-(1+v)*ell)*ell

cases=0
for n in range(1,7):
    s0=mp.power(2,mp.mpf(1)/(2**n))
    c1=-(1+(-1)**n*mp.mpf(2)**(1-n))/(3*s0)
    for d in ('0.0002','0.0006','0.001'):
        d=mp.mpf(d)
        approximation=s0+c1*d
        if n==1: approximation+=3*mp.sqrt(2)*d*d/8
        sn=mp.findroot(lambda x:phin(x,d,n),(approximation-mp.mpf('0.0001'),approximation+mp.mpf('0.0001')))
        assert abs(phin(sn,d,n))<mp.mpf('1e-45')
        # With n fixed, first order errors are O(d^2); n=1 O(d^3).
        assert abs(sn-approximation)<(mp.mpf('3')*d**3 if n==1 else mp.mpf('40')*d*d), (n,d,sn,approximation)
        if n >= 2:
            assert sn < s0
        else:
            assert sn > s0
        cases+=1
print(f'LOZI_CRISIS_TANGENCY_CHECK_OK symbolic_first_levels=8 numerical_root_cases={cases}')
