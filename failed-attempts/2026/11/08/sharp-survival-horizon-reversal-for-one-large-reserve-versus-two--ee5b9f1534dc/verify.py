"""Independent checks for the two-reserve occupancy comparison.

Run with: python verify.py
Requires sympy and mpmath. These finite checks supplement, but do not replace,
the analytic proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import math
import sympy as sp
import mpmath as mp

checks = 0

def check(statement, label):
    global checks
    checks += 1
    assert statement, label

z, c, d, e, delta = sp.symbols('z c d e delta', positive=True)
Q = sp.Matrix([[-2*d, 2*d], [c, -(c+d)]])
D = sp.factor((z*sp.eye(2)-Q).det())
check(sp.simplify(D - (z*z+(c+3*d)*z+2*d*d)) == 0, 'characteristic denominator')
res = (sp.Matrix([[1,0]])*(z*sp.eye(2)-Q).inv()*sp.ones(2,1))[0]
check(sp.simplify(res-(z+c+3*d)/D)==0,'survival Laplace transform')
mean = sp.simplify(res.subs(z,0))
check(sp.simplify(mean-(c+3*d)/(2*d*d))==0,'mean duration')
ctail=e*(delta-1)*(2*delta-1)
cmean=e*(2*delta*delta-3*delta)
check(sp.simplify(ctail-cmean-e)==0,'threshold gap exactly e')
check(sp.simplify((e*e-(ctail+3*delta*e)*e+2*delta*delta*e*e))==0,'tail characteristic threshold')
check(sp.simplify((cmean+3*delta*e)/(2*delta*delta*e*e)-1/e)==0,'mean threshold')

mp.mp.dps=60
for dval,cval in product([F(5,4), F(3,2), F(2), F(5,2), F(3)],
                         [F(0), F(1,5), F(1), F(5,2), F(6), F(13)]):
    dd=mp.mpf(dval.numerator)/dval.denominator
    cc=mp.mpf(cval.numerator)/cval.denominator
    discr=mp.sqrt((cc+3*dd)**2-8*dd**2)
    alpha=(cc+3*dd-discr)/2
    beta=(cc+3*dd+discr)/2
    check(0<alpha<beta,'distinct positive rates')
    check(mp.almosteq(alpha*beta,2*dd**2,rel_eps=mp.mpf('1e-50')),'eigenvalue product')
    for t in [mp.mpf('0.02'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('3'),mp.mpf('10')]:
        matrix=mp.matrix([[-2*dd, 2*dd],[cc,-(cc+dd)]])
        prob=(mp.expm(matrix*t)*mp.matrix([1,1]))[0]
        formula=(beta*mp.exp(-alpha*t)-alpha*mp.exp(-beta*t))/(beta-alpha)
        check(mp.almosteq(prob,formula,rel_eps=mp.mpf('1e-48')),'matrix exponential survival')
        h=alpha*beta*(1-mp.exp(-(beta-alpha)*t))/(beta-alpha*mp.exp(-(beta-alpha)*t))
        check(0<h<=alpha,'hazard between zero and tail rate (may round to tail)')
    threshold=ctail.subs({delta:dval,e:1})
    a_num=float(alpha)
    if cval >= threshold:
        check(a_num <= 1+1e-12,'tail regime strong colonization')
    else:
        check(a_num > 1-1e-12,'tail regime weak colonization')

# Explicit ecological counter-ranking: d=2,c=5/2,e=1.
dd=mp.mpf(2); cc=mp.mpf(5)/2
alpha=(cc+6-mp.sqrt((cc+6)**2-32))/2
beta=(cc+6+mp.sqrt((cc+6)**2-32))/2
S2=lambda t:(beta*mp.exp(-alpha*t)-alpha*mp.exp(-beta*t))/(beta-alpha)
S1=lambda t:mp.exp(-t)
check(mp.mpf(1)<alpha,'example long tail favors single reserve')
check((cc+3*dd)/(2*dd**2)==mp.mpf(17)/16,'exact two reserve mean')
check(S2(mp.mpf('0.5'))>S1(mp.mpf('0.5')),'example short horizon favors two')
check(S2(mp.mpf('3'))<S1(mp.mpf('3')),'example late horizon favors one')
root=mp.findroot(lambda t:S2(t)-S1(t),(mp.mpf('1'),mp.mpf('4')),solver='bisect',maxsteps=250)
check(mp.mpf('2')<root<mp.mpf('2.1'),'unique crossing sample')
print('PASS',checks,'exact symbolic/numerical assertions; crossing=',mp.nstr(root,20))
