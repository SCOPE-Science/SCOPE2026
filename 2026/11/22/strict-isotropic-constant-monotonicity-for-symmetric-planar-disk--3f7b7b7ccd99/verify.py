"""Exact rational Taylor certificate and independent moment checks for circular lenses.
Run: python verify.py  (requires sympy and mpmath).
The finite tests supplement the analytic argument in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb, factorial, pi
import sympy as S
import mpmath as mp

checks = 0

def check(pred, message):
    global checks
    assert pred, message
    checks += 1

def cos_power(n):
    d = {}
    for j in range(n + 1):
        freq = abs(n - 2 * j)
        d[freq] = d.get(freq, Q(0)) + Q(comb(n, j), 2**n)
    return d

def sin_cos_power(n):
    d = {}
    for k, b in cos_power(n).items():
        if k == 0:
            d[1] = d.get(1, Q(0)) + b
        else:
            d[k+1] = d.get(k+1, Q(0)) + b/2
            d[k-1] = d.get(k-1, Q(0)) - b/2
    return d

# Fourier data for P(theta)=sum coefficient*theta**p*trig(k*theta),
# obtained via ordinary product-to-sum identities; independently reconstructed below.
f = {}
def add(p, kind, power_coeffs, multiplier):
    for k, b in power_coeffs.items():
        if kind == 'sin' and k == 0:
            continue
        sign = -1 if kind == 'sin' and k < 0 else 1
        key = (p, kind, abs(k))
        f[key] = f.get(key, Q(0)) + Q(multiplier) * b * sign

for k, v in ((7, 6), (5, -54), (3, 90), (1, -42)):
    add(0, 'cos', cos_power(k), v)
for k, v in ((6, 2), (4, -45), (2, 21), (0, 22)):
    add(1, 'sin', sin_cos_power(k), v)
for k, v in ((5, 18), (3, -18)):
    add(2, 'cos', cos_power(k), v)
add(3, 'sin', {1: Q(1)}, -9)

expected = {(0,'cos',1):Q(-159,32), (0,'cos',3):Q(243,32),
 (0,'cos',5):Q(-87,32), (0,'cos',7):Q(3,32),
 (1,'sin',1):Q(697,32), (1,'sin',3):Q(-93,32),
 (1,'sin',5):Q(-85,32), (1,'sin',7):Q(1,32),
 (2,'cos',1):Q(-9,4), (2,'cos',3):Q(9,8),
 (2,'cos',5):Q(9,8), (3,'sin',1):Q(-9)}
check({k:v for k,v in f.items() if v} == expected, 'Fourier identity')

def taylor_coeff(m):
    z = Q(0)
    for (p, kind, k), v in f.items():
        r = 2*m - p
        if r < 0: continue
        if kind == 'cos' and r % 2 == 0:
            z += v * Q((-1)**(r//2) * k**r, factorial(r))
        elif kind == 'sin' and r % 2 == 1:
            z += v * Q((-1)**((r-1)//2) * k**r, factorial(r))
    return z

for m in range(8):
    check(taylor_coeff(m) == 0, f'zero coefficient {m}')
check(taylor_coeff(8)==Q(-64,55125), 'coefficient 16')
check(taylor_coeff(9)==Q(1312,1819125), 'coefficient 18')
check(taylor_coeff(10)==Q(-25304,118243125), 'coefficient 20')
check(taylor_coeff(11)==Q(302476,7449316875), 'coefficient 22')

b = Q(121, 49)  # theta^2 < (11/7)^2, since pi/2 < 11/7
# H(z) consists of the first four nonzero terms after theta^16.
H_b = sum((taylor_coeff(m) * b**(m-8) for m in range(8,12)), Q(0))
check(H_b==Q(-5858491732,79673152820625), 'exact cubic bound')
# H'(z) has positive leading coefficient and strictly negative discriminant.
a3=taylor_coeff(11);a2=taylor_coeff(10);a1=taylor_coeff(9)
discriminant=(2*a2)**2 - 4*(3*a3)*a1
check(a1>0 and a3>0 and discriminant<0, 'H strictly increasing')
for m in range(12,22,2):
    check(taylor_coeff(m)<0, f'negative Taylor coefficient {m}')
    check(taylor_coeff(m+1)>0, f'positive Taylor coefficient {m+1}')
    check(b*taylor_coeff(m+1)<-taylor_coeff(m), f'negative Taylor pair {m}')
check(taylor_coeff(22)<0, 'last coefficient negative')
# Rigorous Lagrange remainder after total degree 44.
# Each theta^p trig(k theta) contributes at most theta^45 k^(45-p)/(45-p)!.
E=sum((abs(v)*Q(k**(45-p),factorial(45-p))
       for (p,kind,k),v in f.items()), Q(0))
relative_error_bound=E*Q(11,7)**29
check(relative_error_bound < -H_b, 'whole-interval strict certificate')

# Symbolic derivative and geometric slice formulas.
a,T=S.symbols('a T', real=True)
s=S.sqrt(1-a*a)
A=2*(T-a*s)
X=(3*(1+4*a*a)*T-a*s*(13+2*a*a))/6
Y=(3*T+a*s*(2*a*a-5))/6
D=lambda q:S.diff(q,a)-S.diff(q,T)/s
P=-9*T**3*s+18*T**2*a**5-18*T**2*a**3+2*T*a**6*s-45*T*a**4*s+21*T*a*a*s+22*T*s+6*a**7-54*a**5+90*a**3-42*a
check(S.simplify((D(X)*Y+X*D(Y))*A-4*X*Y*D(A)+4*a*P/(9*s))==0, 'differentiation identity')
# Independent antiderivatives evaluated at a and 1.
u=S.symbols('u',real=True)
I0=(T-a*s)/2
I1=s**3/3
I2=(T-a*s*(2*a*a-1))/8
check(S.simplify(X-4*(I2-2*a*I1+a*a*I0))==0, 'axial second moment')
check(S.simplify(Y-(3*T+a*s*(2*a*a-5))/6)==0, 'transverse second moment')
check(S.simplify(A-4*I0)==0, 'area')

mp.mp.dps=40
for i in range(1,29):
    aa=mp.mpf(i)/30
    theta=mp.acos(aa)
    ss=mp.sqrt(1-aa*aa)
    Ar=2*(theta-aa*ss)
    Xr=(3*(1+4*aa*aa)*theta-aa*ss*(13+2*aa*aa))/6
    Yr=(3*theta+aa*ss*(2*aa*aa-5))/6
    An=4*mp.quad(lambda v:mp.sqrt(1-v*v),[aa,1])
    Xn=4*mp.quad(lambda v:(v-aa)**2*mp.sqrt(1-v*v),[aa,1])
    Yn=mp.mpf(4)/3*mp.quad(lambda v:(1-v*v)**mp.mpf('1.5'),[aa,1])
    check(abs(Ar-An)<mp.mpf('1e-32'),'area quadrature')
    check(abs(Xr-Xn)<mp.mpf('1e-32'),'axial quadrature')
    check(abs(Yr-Yn)<mp.mpf('1e-32'),'transverse quadrature')
    check(Xr>0 and Yr>0 and Ar>0,'moment positivity')

# Exact rescaled parabolic endpoint, verified by beta integration.
x=S.symbols('x', nonnegative=True)
I=S.integrate(4*S.sqrt(1-x),(x,0,1))
Jx=S.integrate(4*x*x*S.sqrt(1-x),(x,0,1))
Jy=S.integrate(S.Rational(4,3)*(1-x)**S.Rational(3,2),(x,0,1))
check((I,Jx,Jy)==(S.Rational(8,3),S.Rational(64,105),S.Rational(8,15)), 'endpoint moments')
check(S.factor(Jx*Jy/I**4)==S.Rational(9,1400), 'endpoint isotropic constant')
print('PASS:',checks,'exact/symbolic/numerical assertions')
print('P upper bound margin:',float(-H_b-relative_error_bound))
