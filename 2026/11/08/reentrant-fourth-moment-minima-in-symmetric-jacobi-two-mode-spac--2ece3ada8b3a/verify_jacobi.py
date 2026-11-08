"""Exact fourth-moment and optimizer identities for symmetric Jacobi modes.

Run with Python 3 and SymPy. All universal claims are established by the
algebraic formulas and sign arguments in RESULT.md, not by the finite tests.
"""
from fractions import Fraction
from math import comb
import sympy as S

a=S.symbols('a', positive=True)
u=S.symbols('u', real=True)
def even_moment(j):
    z=S.Integer(1)
    for k in range(1,j+1):
        z *= S.Rational(2*k-1,1)/(2*a+2*k-1)
    return S.factor(z)
v2,v4,v6,v8=[even_moment(j) for j in range(1,5)]
variance=S.factor(v4-v2**2)
assert S.simplify(variance-4*a/((2*a+1)**2*(2*a+3)))==0

A=S.factor(v4/v2**2)
C=S.factor((v6-2*v2*v4+v2**3)/(v2*variance))
B=S.factor((v8-4*v2*v6+6*v2**2*v4-3*v2**4)/variance**2)
assert S.factor(A-3*(2*a+1)/(2*a+3))==0
assert S.factor(C-(10*a+1)/(2*a+5))==0
assert S.factor(B-3*(2*a+3)*(10*a*a-3*a+2)/(a*(2*a+5)*(2*a+7)))==0

D=S.factor(A-6*C+B)
K=S.factor(A*u*u+6*C*u*(1-u)+B*(1-u)*(1-u))
u_star=S.factor((B-3*C)/D)
K_star=S.factor(K.subs(u,u_star))
assert S.factor(K-K_star-D*(u-u_star)**2)==0
assert S.factor((A-3*C)+6*(8*a*a+10*a-1)/((2*a+3)*(2*a+5)))==0
assert S.factor((B-3*C)+18*(2*a+1)*(4*a-1)/(a*(2*a+5)*(2*a+7)))==0
assert S.factor((B-A)-6*(a+1)*(2*a-1)*(8*a*a+10*a-9)/(a*(2*a+3)*(2*a+5)*(2*a+7)))==0
assert S.factor(S.diff(K,u).subs(u,0)-2*(3*C-B))==0
assert S.factor(S.diff(K,u).subs(u,1)-2*(A-3*C))==0
print('EXACT_JACOBI_MOMENTS_AND_NORMALIZED_QUARTIC_OK')
print('EXACT_CRITICAL_DERIVATIVES_AND_ENDPOINT_FACTORIZATIONS_OK')
print('EXACT_INTERIOR_QUADRATIC_DEFICIT_OK')

# Independently derive symmetric-beta moments by the raw beta integral
# E[(2Y-1)^r] = sum_j binom(r,j) 2^j (-1)^(r-j) (a)_j/(2a)_j.
def raw_moment(r):
    ans=S.Integer(0)
    for j in range(r+1):
        ans+=S.binomial(r,j)*2**j*(-1)**(r-j)*S.rf(a,j)/S.rf(2*a,j)
    return S.factor(ans)
for r in range(9):
    assert S.simplify(raw_moment(r)-(even_moment(r//2) if r%2==0 else 0))==0
print('INDEPENDENT_BETA_BINOMIAL_MOMENT_INTEGRAL_OK_0_TO_8')

alpha0=(S.sqrt(33)-5)/8
beta=(S.sqrt(97)-5)/8
assert S.simplify(8*alpha0**2+10*alpha0-1)==0
assert S.simplify(8*beta**2+10*beta-9)==0
assert 0<float(alpha0)<.25<.5<float(beta)<1
for z in [S.Rational(1,100),S.Rational(1,20),S.Rational(1,10),S.Rational(1,5),
          S.Rational(1,4),S.Rational(3,10),S.Rational(1,2),S.Rational(11,20),
          S.Rational(3,5),S.Rational(7,10),S.Integer(1),S.Integer(2),S.Integer(10)]:
    Av,Bv,Cv=[S.Rational(t.subs(a,z)) for t in (A,B,C)]
    Ds=Av-6*Cv+Bv
    st=(Bv-3*Cv)/Ds
    for j in range(1001):
        v=S.Rational(j,1000)
        kval=Av*v*v+6*Cv*v*(1-v)+Bv*(1-v)*(1-v)
        candidates=[Av,Bv]
        if 0<st<1:candidates.append(Av*st*st+6*Cv*st*(1-st)+Bv*(1-st)*(1-st))
        assert min(candidates)<=kval<=max(candidates)
    if z<alpha0:assert 0<st<1 and Ds>0
    if alpha0<=z<=S.Rational(1,4):assert Av<=Bv and (Av-3*Cv)<=0 and (Bv-3*Cv)>=0
    if z>S.Rational(1,4):assert 0<st<1 and Ds<0
print('EXACT_RATIONAL_PHASE_CHECKS_OK_13_PARAMETERS_13013_TESTS')

# Independent raw polynomial fourth-moment integration at representative
# coefficient pairs, without using the normalized-energy quartic formula.
for alpha in [S.Rational(1,20),S.Rational(1,10),S.Rational(1,4),S.Rational(1,2),S.Integer(1),S.Integer(3)]:
    for c1,c2 in [(1,0),(0,1),(1,1),(2,-3),(-3,5),(5,7)]:
        z=S.symbols('z')
        poly=S.Poly((c1*z+c2*(z*z-v2.subs(a,alpha)))**4,z)
        E4=sum(coef*raw_moment((i[0])).subs(a,alpha) for i,coef in poly.terms())
        E2=c1*c1*v2.subs(a,alpha)+c2*c2*variance.subs(a,alpha)
        energy_frac=S.Rational(c1*c1)*v2.subs(a,alpha)/E2
        pred=K.subs({a:alpha,u:energy_frac})
        assert S.factor(E4/E2**2-pred)==0
print('INDEPENDENT_RAW_FOURTH_MOMENT_POLYNOMIAL_CHECKS_OK_36')
print('EXAMPLE_ALPHA_ONE_MIXED_MAX_ENERGY',S.factor(u_star.subs(a,1)),S.factor(K_star.subs(a,1)))
print('ALL_SYMMETRIC_JACOBI_FOURTH_MOMENT_CHECKS_PASSED')
