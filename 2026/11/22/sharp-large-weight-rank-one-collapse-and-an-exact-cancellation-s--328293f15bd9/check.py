"""Standalone checks of the inverse-Gaussian CDF-discrepancy high-weight theorem.
Dependencies: Python 3.10+, sympy, mpmath. No network/data dependencies.
"""
from fractions import Fraction as Q
import sympy as sp
import mpmath as mp

checks = 0
def test(condition, msg):
    global checks
    assert bool(condition), msg
    checks += 1

p = sp.symbols('p', positive=True)
r = 1/p
mom={-4:1+10*r+45*r**2+105*r**3+105*r**4,
     -3:1+6*r+15*r**2+15*r**3,-2:1+3*r+3*r**2,
     -1:1+r,0:1,1:1,2:1+r}
coef={1:(p+3)/2,-1:(3*p+6)/2,-2:-p/2}
variance=sp.factor(sum(a*b*(mom[i+j]-mom[i]*mom[j])
                       for i,a in coef.items() for j,b in coef.items()))
test(sp.simplify(variance-3*(p+4)/(2*p**2))==0,'null influence variance')
for value in [sp.Rational(1,3),1,sp.Rational(3,2),5,20]:
    test(variance.subs(p,value)>0,'positive variance')

x,y=sp.symbols('x y', positive=True)
z=3-x-y
u=(1/x+1/y+1/z)/3
v=(1/x**2+1/y**2+1/z**2)/3
identity=sp.factor(3*u**2-3*u+1-v-(x-1)*(y-1)*(z-1)/(x*y*z))
test(identity==0,'exact three-point zero locus')
q=sp.symbols('q', real=True)
two=[1-q,1+q]; u2=sum(1/a for a in two)/2
v2=sum(1/a**2 for a in two)/2
B2=sp.factor(sp.Rational(1,2)*(3*u2+(1-v2)/(u2-1)))
test(sp.simplify(B2-q**2/(2*(1-q**2)))==0,'two-point nonzero formula')

def standardize(xs):
    xs=[mp.mpf(str(x)) for x in xs]
    mean=sum(xs)/len(xs)
    ys=[x/mean for x in xs]
    rec=sum(1/t for t in ys)/len(ys)
    phi=1/(rec-1)
    b=[(phi+3/t-phi/t**2)/2 for t in ys]
    B=sum(b)/len(b)
    return ys,b,B

def g(t,ys,bs):
    n=len(ys)
    return sum(b*min(y,t) for y,b in zip(ys,bs))/n-sum(y<=t for y in ys)/n

def statistic(xs,a,gaussian=False):
    ys,bs,B=standardize(xs)
    cuts=sorted(set(ys))
    endpoints=[mp.mpf(0)]+cuts+[mp.inf]
    out=mp.mpf('0')
    for left,right in zip(endpoints[:-1],endpoints[1:]):
        # integrate each analytic interval, discontinuity affects zero Lebesgue measure
        weight=lambda t:mp.exp(-a*t*t) if gaussian else mp.exp(-a*t)
        out+=mp.quad(lambda t:g(t,ys,bs)**2*weight(t),[left,right])
    return len(xs)*out

mp.mp.dps=55
samples=[[mp.mpf('0.6'),mp.mpf('0.8'),mp.mpf('1.6')],
         [mp.mpf('0.5'),mp.mpf('1.0'),mp.mpf('1.5')]]
for xs in samples:
    ys,bs,B=standardize(xs)
    m=min(ys); n=len(ys); count=sum(y==m for y in ys)
    for gaussian in [False, True]:
        a=mp.mpf('70') if gaussian else mp.mpf('45')
        T=statistic(xs,a,gaussian)
        if abs(B)>mp.mpf('1e-30'):
            lead=n*B**2*(mp.sqrt(mp.pi)/(4*a**mp.mpf('1.5')) if gaussian else 2/a**3)
            test(abs(T/lead-1)<mp.mpf('0.003'),'generic high weight')
        else:
            lead=count**2/(2*n*m*a)*mp.exp(-a*m*m) if gaussian else count**2/(n*a)*mp.exp(-a*m)
            test(abs(T/lead-1)<mp.mpf('0.18'),'exceptional high weight')

test(abs(standardize(samples[1])[2])<mp.mpf('1e-45'),'exceptional sample exact zero')
print('PASS:',checks,'assertions; sigma2 =',variance)
