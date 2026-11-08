"""Independent algebraic and high-precision spot checks for the stability-boundary theorem.

The proof of global strict monotonicity is analytic; this finite program is
not a replacement for the rearrangement argument in RESULT.md.
"""
from fractions import Fraction
import math
import sympy as s
import mpmath as mp

checks = 0

def check(statement, label):
    global checks
    if not statement:
        raise AssertionError(label)
    checks += 1

x,t,q = s.symbols('x t q', nonnegative=True, real=True)
N = (1-x*(1-t))**2 + q*(1-t)**2
D = (1+x*t)**2 + q*t**2
R2 = N/D
C = 1-2*t+2*x*t*(1-t)
check(s.simplify(s.diff(R2,q) - C/D**2) == 0,
      'exact derivative factorization')
A=(1-t)*(1+x*t)
B=t*(1-x*(1-t))
check(s.expand(A+B-1)==0, 'complementary factors sum to one')
check(s.expand(A-B-C)==0, 'complementary factors differ as claimed')
check(s.simplify(s.diff(D,t)-2*(x+(x*x+q)*t))==0,
      'logarithmic antiderivative')
check(s.simplify(s.diff(1/D,t) + s.diff(D,t)/D**2)==0,
      'denominator derivative')

# Exact Taylor coefficients of the real-axis and imaginary-axis restrictions.
X=s.symbols('X',real=True)
f0=X**2/(1+X)-2*s.log(1+X)
check(s.simplify(s.diff(f0,X)-(X*X-2)/(1+X)**2)==0,
      'real-axis derivative')
check(s.expand(s.series(f0,X,0,3).removeO() + 2*X - 2*X**2)==0,
      'real-axis series')
Y=s.symbols('Y',real=True)
fimag=-s.log(1+Y**2)+Y*s.atan(Y)
check(s.expand(s.series(fimag,Y,0,6).removeO() - Y**4/6)==0,
      'imaginary-axis quartic coefficient')
Fq0=X*(3+2*X)/(3*(1+X)**3)
check(s.simplify(-1/(1+X)**2+1/(1+X)-X**2/(3*(1+X)**3)-Fq0)==0,
      'boundary transverse derivative')

# Uniform-in-stratum exact rational derivative positivity on a broad rational grid.
for xn in range(0,19):
    xx=s.Rational(xn,3)
    for qn in range(0,13):
        qq=s.Rational(qn,5)
        last=None
        for tn in range(0,41):
            tt=s.Rational(tn,40)
            weight=s.factor(D.subs({x:xx,q:qq,t:tt})**(-2))
            if last is not None:
                check(weight<=last,'monotone paired weight')
            last=weight
        for tn in range(0,20):
            tt=s.Rational(tn,40)
            check(s.factor(1-2*tt)>=0,'first-half antisymmetry sign')
            check(s.factor(C.subs({x:xx,t:tt}))>=0,'nonnegative numerator left half')

mp.mp.dps=60

def defect(xx, yy):
    xx,yy=mp.mpf(xx),mp.mpf(yy)
    if yy==0:
        return xx**2/(1+xx)-2*mp.log1p(xx)
    return -mp.log((1+xx)**2+yy**2)+(xx**2+yy**2)*mp.atan(yy/(1+xx))/yy

def integral(xx, yy):
    zz=-mp.mpf(xx)+1j*mp.mpf(yy)
    return mp.quad(lambda tt: abs(1+zz/(1-tt*zz))**2, [0,1])-1

xcrit=mp.findroot(lambda xx:defect(xx,0),(4,mp.mpf('4.1')))
check(4<xcrit<mp.mpf('4.04'),'real-axis cutoff interval')
check(abs(xcrit-mp.mpf('4.03361046935773630689434638449791867'))<mp.mpf('1e-32'),
      'critical root digits')

for xx in ('0.00001','0.01','0.1','0.5','1','2','3','4'):
    check(defect(xx,0)<0,'interior real-axis stability')
    high=mp.mpf(10)
    low=mp.mpf(0)
    for _ in range(155):
        mid=(low+high)/2
        if defect(xx,mid)>0: high=mid
        else: low=mid
    yy=(low+high)/2
    check(abs(defect(xx,yy))<mp.mpf('2e-39'),'boundary residual')
    for zz in (yy/3, yy*mp.mpf('0.95')):
        check(defect(xx,zz)<0,'inside strict')
    for zz in (yy*mp.mpf('1.05'), 2*yy):
        check(defect(xx,zz)>0,'outside strict')
    check(abs(defect(xx,yy)-integral(xx,yy))<mp.mpf('1e-45'),
          'integral equals closed form')

for xx in ('0.000001','0.00001','0.0001','0.001'):
    xx=mp.mpf(xx)
    root=mp.findroot(lambda y:defect(xx,y),((12*xx)**mp.mpf('0.25')*mp.mpf('.9'),
                                            (12*xx)**mp.mpf('0.25')*mp.mpf('1.1')))
    check(abs(root/(12*xx)**mp.mpf('.25')-1)<mp.mpf('.1'),
          'fourth-root asymptotics scale')

limitcoefficient=mp.sqrt(3*(xcrit**2-2)*(1+xcrit)/(xcrit*(3+2*xcrit)))
check(abs(limitcoefficient-mp.mpf('2.1970824369929405')) < mp.mpf('1e-15'),
      'endpoint square-root coefficient')

print(f'PASS: {checks} checks')
print('real-axis cutoff =',mp.nstr(xcrit,40))
print('right-endpoint square-root coefficient =',mp.nstr(limitcoefficient,40))
print('fourth-root coefficient =',mp.nstr(12**mp.mpf('.25'),40))
print('explicit-vs-implicit near-origin gain =',mp.nstr(2**mp.mpf('.25'),40))
