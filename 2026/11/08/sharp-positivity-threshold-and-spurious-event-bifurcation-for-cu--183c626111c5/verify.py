"""Reproduce exact-arithmetic certificates and high-precision constants for
positivity of the ordinary endpoint-Hermite cubic for exponential decay.
Run: python verify.py .  Dependencies: sympy 1.14, mpmath 1.3.
"""
from fractions import Fraction as Q
from math import factorial, comb
import mpmath as mp
import sympy as sp

checks = 0

def check(expr, label):
    global checks
    assert bool(expr), label
    checks += 1

def inverse_exponential_bounds(z, N=48):
    """Rational enclosure of exp(-z) for 0 < z < N+2."""
    assert 0 < z < N + 2
    S = sum(z**k / Q(factorial(k)) for k in range(N+1))
    term = z**(N+1) / Q(factorial(N+1))
    upper_exp = S + term/(1-z/Q(N+2))
    return Q(1)/upper_exp, Q(1)/S

def coefficients(z, r):
    return [Q(1), -z, Q(-3)+2*z+(3+z)*r, 2-z-(2+z)*r]

def local_bernstein(a, l, u):
    delta = u-l
    power = [sum(a[j]*comb(j,k)*l**(j-k)*delta**k
                 for j in range(k,4)) for k in range(4)]
    return [power[0], power[0]+power[1]/3,
            power[0]+2*power[1]/3+power[2]/3, sum(power)]

s,z,r=sp.symbols('s z r',real=True)
A=2-z-(2+z)*r
B=-3+2*z+(3+z)*r
H=1-z*s+B*s**2+A*s**3
basis=(1-3*s*s+2*s**3)-z*s*(1-s)**2+r*(3*s*s-2*s**3)-z*r*(s**3-s**2)
check(sp.expand(H-basis)==0,'Hermite basis identity')
check(sp.expand(H.subs(s,0)-1)==0,'left value')
check(sp.expand(H.subs(s,1)-r)==0,'right value')
check(sp.expand(sp.diff(H,s).subs(s,0)+z)==0,'left slope')
check(sp.expand(sp.diff(H,s).subs(s,1)+z*r)==0,'right slope')
dz=sp.diff(H,z)+sp.diff(H,r)*(-r)
asserted=-s*(1-s)**2-r*s*s*((2-s)+z*(1-s))
check(sp.expand(dz-asserted)==0,'strict decay in z')
Delta=sp.discriminant(H,s)
check(sp.expand(Delta-(B**2*z**2+4*A*z**3-4*B**3-27*A*A-18*A*B*z))==0,'discriminant identity')

# A concrete exact-rational certificate that the full cubic is positive
# at z=19/5, not merely at a few sampled points.  The coefficient of
# r in H is s^2[(3-2s)+z(1-s)] >=0, so use the rational LOWER bound rlo.
for z0 in (Q(7,2), Q(19,5)):
    rlo,rhi=inverse_exponential_bounds(z0)
    check(rlo<rhi,'ordered exponential enclosure')
    a=coefficients(z0,rlo)
    positive=[]
    for j in range(4):
        positive+=local_bernstein(a,Q(j,4),Q(j+1,4))
    for idx,c in enumerate(positive):
        check(c>0,f'Bernstein strict positivity z={z0}, coefficient {idx}')

# At z=7/2 the interpolant stays positive yet is not monotone:
# its derivative at s=4/5 is strictly positive, while endpoint slopes are negative.
z0=Q(7,2); s0=Q(4,5)
rlo,rhi=inverse_exponential_bounds(z0)
d0=2*(3+z0)*s0-3*(2+z0)*s0*s0
r_for_lower=rlo if d0>=0 else rhi
a=coefficients(z0,r_for_lower)
positive_derivative=a[1]+2*a[2]*s0+3*a[3]*s0*s0
check(positive_derivative>0,'positive derivative of positive interpolant z=7/2')

# A certified negative value at z=39/10, s=2/3.  Bound affine dependence
# on r by rational intervals, taking the upper r bound to upper-bound H.
z0=Q(39,10);s0=Q(2,3)
rlo,rhi=inverse_exponential_bounds(z0)
a=coefficients(z0,rhi)
P=sum(a[k]*s0**k for k in range(4))
check(P<0,'certified negative H_(39/10)(2/3)')

# High-precision solve of the unique tangency (analytic proof of uniqueness
# is in RESULT.md).  This is numeric reproduction, not the infinite proof.
mp.mp.dps=80
def hm(zz,ss):
    er=mp.exp(-zz)
    return 1-zz*ss+(-3+2*zz+(3+zz)*er)*ss**2+(2-zz-(2+zz)*er)*ss**3
def sm(zz,ss):
    er=mp.exp(-zz)
    AA=2-zz-(2+zz)*er
    BB=-3+2*zz+(3+zz)*er
    return -zz+2*BB*ss+3*AA*ss**2
zz,ss=mp.findroot((hm,sm),(mp.mpf('3.87'),mp.mpf('.676')),
                   solver='mdnewton',tol=mp.mpf('1e-65'))
curvature=mp.diff(lambda x:hm(zz,x),ss,2)
dzval=mp.diff(lambda x:hm(x,ss),zz)
K=mp.sqrt(-2*dzval/curvature)
check(abs(hm(zz,ss))<mp.mpf('1e-65'),'zero value at contact')
check(abs(sm(zz,ss))<mp.mpf('1e-65'),'zero slope at contact')
check(mp.mpf('3.8')<zz<mp.mpf('3.9'),'root lies inside certified bracket')
check(mp.mpf('.67')<ss<mp.mpf('.69'),'contact interior')
check(curvature>0 and dzval<0,'nondegenerate sign conditions')
for delta in (mp.mpf('1e-8'),mp.mpf('1e-10')):
    lo=mp.findroot(lambda x:hm(zz+delta,x),ss-K*mp.sqrt(delta))
    hi=mp.findroot(lambda x:hm(zz+delta,x),ss+K*mp.sqrt(delta))
    check(lo<ss<hi and abs((hi-lo)/(2*mp.sqrt(delta))-K)<mp.mpf('.001'),
          'square root splitting')

print('PASS:',checks,'independent symbolic/rational/numerical assertions')
print('threshold z* =',mp.nstr(zz,65))
print('contact s* =',mp.nstr(ss,65))
print('curvature =',mp.nstr(curvature,55))
print('dz H =',mp.nstr(dzval,55))
print('root splitting K =',mp.nstr(K,55))
print('certificates: H_(19/5)(s)>0 on [0,1]; H_(39/10)(2/3)<0')
