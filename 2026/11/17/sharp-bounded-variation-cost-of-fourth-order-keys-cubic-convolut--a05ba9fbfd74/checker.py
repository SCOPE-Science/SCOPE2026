"""Exact symbolic and independent numerical checks for Keys cubic-convolution BV norm.
Requires Python 3 and sympy. Only evidence of local algebra; the BV theorem has a separate proof.
"""
import random
import sympy as S

t = S.symbols('t',real=True)
r = S.symbols('r',real=True)
p0 = S.Rational(4,3)*r**3-S.Rational(7,3)*r**2+1
p1 = -S.Rational(7,12)*r**3+3*r**2-S.Rational(59,12)*r+S.Rational(5,2)
p2 = S.Rational(1,12)*r**3-S.Rational(2,3)*r**2+S.Rational(7,4)*r-S.Rational(3,2)

def phi_at(q):
    a=S.Abs(q)
    if a.is_number:
        if a>=3:return S.Integer(0)
        if a<=1:return S.expand(p0.subs(r,a))
        if a<=2:return S.expand(p1.subs(r,a))
        return S.expand(p2.subs(r,a))
    raise ValueError('need definite interval')

def phi_cell(j,i):
    # x=j+t, 0<t<1, index i
    a=j-i
    if a>=0:
        dist=t+a
        zone=a
    else:
        dist=-t-a
        zone=-a-1
    if zone>=3:return S.Integer(0)
    return S.expand([p0,p1,p2][zone].subs(r,dist))

# All local kernels as expressions in 0<t<1.
F = {}
for j in range(-2,3):
    F[j]=S.factor(sum(phi_cell(j,i) for i in range(1,8)))
assert S.simplify(F[-2]-t**2*(1-t)/12)==0
assert S.simplify(F[-1]-t*(t-1)*(6*t+1)/12)==0
assert S.simplify(F[0]-t*(7+15*t-10*t**2)/12)==0
assert S.simplify(F[1]-(1-F[-1].subs(t,1-t)))==0
assert S.simplify(F[2]-(1-F[-2].subs(t,1-t)))==0
# Integer partitions: cardinality and unity on each unit cell.
assert S.simplify(sum(phi_cell(0,i) for i in range(-3,4))-1)==0
assert S.simplify(sum(phi_cell(1,i) for i in range(-3,5))-1)==0

rstar=(S.Integer(5)+S.sqrt(43))/18
A=(S.Integer(260)+43*S.sqrt(43))/5832
assert S.simplify(S.diff(F[-1],t).subs(t,rstar))==0
assert S.simplify(F[-1].subs(t,rstar)+A)==0
assert S.simplify(F[-2].subs(t,S.Rational(2,3))-S.Rational(1,81))==0
assert S.simplify(S.diff(F[0],t)-(7+30*t-30*t**2)/12)==0
constant=1+S.Rational(4,81)+4*A
assert S.simplify(constant-(1790+43*S.sqrt(43))/1458)==0
# Four-tap, order-3 response: two cubic Hermite side bumps and monotone center.
L3=1+S.Rational(8,27)
assert S.simplify(L3-S.Rational(35,27))==0
assert S.simplify(constant-L3-(43*S.sqrt(43)-100)/1458)==0
assert (constant-L3).evalf()>0
print('EXACT_KEYS_SIX_TAP_STEP_POLYNOMIALS_AND_CRITICAL_POINTS_PASS')
print('EXACT_KEYS_FOUR_VS_SIX_TAP_VARIATION_GAP_PASS', str(S.simplify(constant-L3)))

# Independent numerical test: evaluate kernel via explicit piecewise polynomial and
# numerical integration of interpolated |derivative| on all integer cells.
import math

def phi(x):
    u=abs(x)
    if u>=3:return 0.0
    if u<=1:return (4*u**3-7*u**2)/3+1
    if u<=2:return (-7*u**3+36*u**2-59*u+30)/12
    return (u**3-8*u**2+21*u-18)/12

def phip(x):
    u=abs(x)
    if u>=3 or u==0:return 0.0
    sign=1 if x>0 else -1
    if u<=1:return sign*(4*u*u-14*u/3)
    if u<=2:return sign*(-21*u*u+72*u-59)/12
    return sign*(3*u*u-16*u+21)/12

rng=random.Random(314159)
for case in range(125):
    size=5+rng.randrange(9)
    d=[rng.uniform(-1,1) for _ in range(size)]
    y=[0.0]
    for v in d:y.append(y[-1]+v)
    # extend constantly beyond data: y is indexed 0..size
    def Y(i):return y[max(0,min(size,i))]
    # for all piecewise intervals where derivative might be nonzero
    var=0.0
    for j in range(-3,size+3):
        # evaluate derivative with small-step Simpson after splitting at derivative roots approximately
        # not an exhaustive proof: dense stress independent of exact algebra
        N=1200
        vals=[]
        for k in range(N+1):
            xx=j+k/N
            vals.append(sum(Y(i)*phip(xx-i) for i in range(j-3,j+5)))
        var+=(abs(vals[0])+abs(vals[-1])+4*sum(abs(vals[k]) for k in range(1,N,2))+2*sum(abs(vals[k]) for k in range(2,N,2)))/(3*N)
    input_var=sum(abs(q) for q in d)
    assert var<=(float(constant)+0.004)*input_var,(case,var,input_var)
print('INDEPENDENT_RANDOM_BV_NUMERICAL_STRESS_PASS 125')
print('SHARP_SIX_TAP_BV_NORM',S.N(constant,16))
print('ALL_CHECKS_PASS')
