"""Standalone symbolic checks for the optimal TTR3 exponential-kernel CQ sign transition.
Requires Python 3 and SymPy; no numerical root finding is used for certificates.
"""
import sympy as sp
from math import comb

z,R,t=sp.symbols('z R t', real=True)
sq=sp.sqrt(2)
v=(2-sq)/4
d=sp.expand((1-z)+(1-z)**2/sp.Integer(2)+(sq-1)*(1-z)**3+(2-sq)*(1-z)**4/4)
a=[sp.expand(d).coeff(z,k) for k in range(5)]
G=R**5-(1+3*sq)*R**4+9*(1+sq)*R**3-(37+sp.Rational(51,2)*sq)*R**2+(72+46*sq)*R-(52+34*sq)

def sign_qsqrt2(expr):
    e=sp.expand(sp.radsimp(expr))
    b=e.coeff(sq)
    c=sp.simplify(e-b*sq)
    assert c.is_Rational and b.is_Rational, (e,b,c)
    if b==0:return 1 if c>0 else (-1 if c<0 else 0)
    if c==0:return 1 if b>0 else -1
    if c>0 and b>0:return 1
    if c<0 and b<0:return -1
    s=1 if c*c>2*b*b else (-1 if c*c<2*b*b else 0)
    return s if c>0 else -s

assert sp.simplify(sp.diff(d,z)-(2-sq)*(z-2-sq/2)*(z*z-(1+sq)*z+(1+sq)))==0
assert sign_qsqrt2(v)==1
assert sign_qsqrt2(3-sq)==1
# One positive minimum: the remaining quadratic in the derivative has negative discriminant.
assert sign_qsqrt2((1+sq)**2-4*(1+sq))==-1
q_max=sp.Rational(5,8)+5*sq/16
assert sp.simplify(-d.subs(z,2+sq/2)-q_max)==0

# Coefficientwise Bernstein positivity of G' on [1,3].
D=sp.Poly(sp.expand(sp.diff(G,R).subs(R,1+2*t)),t)
assert D.degree()==4
bern=[sp.simplify(sum(D.nth(k)*sp.Rational(comb(j,k),comb(4,k)) for k in range(j+1))) for j in range(5)]
expected=[26+10*sq,20-sp.Rational(13,2)*sq,44-29*sq,130-sp.Rational(163,2)*sq,390-188*sq]
assert all(sp.simplify(x-y)==0 for x,y in zip(bern,expected))
assert all(sign_qsqrt2(x)==1 for x in bern)
lo=sp.Rational(1769,1000);hi=sp.Rational(177,100)
assert sign_qsqrt2(G.subs(R,lo))==-1
assert sign_qsqrt2(G.subs(R,hi))==1
assert sign_qsqrt2(G.subs(R,1))==-1 and sign_qsqrt2(G.subs(R,3))==1

# Exact resultant/spectral crossing identity. If P_q(R)=0, replace a0+q by -sum a_j R^j.
c0=-sum(a[j]*R**j for j in range(1,5))
c1=c0+a[1]*R
c2=c1+a[2]*R**2
c3=-a[4]*R**4
F=sp.expand(c1*c3-c3**2+c0**2-c0*c2)
assert sp.simplify(F+v*R**2*G)==0

# Certified coarse enclosures at the unique transition, based on the monotone -delta.
assert sign_qsqrt2(-d.subs(z,lo)-sp.Rational(3,5))==1
assert sign_qsqrt2(sp.Rational(31,50)+d.subs(z,hi))==1
p0=a[0]
Tlo=(p0+sp.Rational(3,5))/(v*hi**3)
Thi=(p0+sp.Rational(31,50))/(v*lo**3)
assert sign_qsqrt2(Tlo-sp.Rational(16,5))==1
assert sign_qsqrt2(sp.Rational(17,5)-Thi)==1
ulo=(1/v-hi-sp.Rational(17,5))/2
uhi=(1/v-lo-sp.Rational(16,5))/2
assert sign_qsqrt2(ulo-sp.Rational(7,10))==1
assert sign_qsqrt2(sp.Rational(11,10)-uhi)==1
left=(lo+sp.Rational(7,10))*((sp.Rational(16,5)-sp.Rational(11,10))**2+lo**2-sp.Rational(11,10)**2)
right=2*hi*(sp.Rational(17,5)-lo)**2
assert left>right

# Explicit sign-defect at q=1, lag four, with algebraic exactness.
q=sp.Integer(1)
ww=[1/(p0+q)]
for n in range(1,5):
    ww.append(sp.cancel(-sum(a[j]*ww[n-j] for j in range(1,min(n,4)+1))/(p0+q)))
w4=sp.expand(sp.radsimp(ww[4]))
assert sp.simplify(w4-(sp.Integer(109218772)-sp.Integer(77331942)*sq)/sp.Integer(6436343))==0
assert sign_qsqrt2(w4)==-1

print('PASS: TTR3 coefficients, unique sharp crossing, endpoint residue domination, exact negative weight at q=1.')
print('Bernstein coefficients for monotonicity:',bern)
print('critical R in',lo,hi,'critical q in (3/5,31/50)')
print('lag-four q=1 coefficient:',w4)
