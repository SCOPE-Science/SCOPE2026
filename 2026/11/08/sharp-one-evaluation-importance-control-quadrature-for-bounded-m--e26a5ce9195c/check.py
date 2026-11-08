#!/usr/bin/env python3
"""Independent numerical checks for the one-node monotone quadrature law.
Only the Python standard library is required.
"""
import math

def integrate(fun, n=20000):
    return sum(fun((i+0.5)/n) for i in range(n))/n

c=1/(4*math.sinh(1)**2)
star=(1/math.tanh(1)-1)/4
p=lambda x: 1/(2*math.sqrt((x-.5)**2+c))
h=lambda x: 1-x-.5/p(x)
F=lambda x: .5+(x-.5)*p(x)
checks=[]
def check(name,value,target,tol=2e-7):
    error=abs(value-target)
    assert error<tol, f'{name}: {value}, target {target}, error {error}'
    checks.append((name,value,target,error))

check('normalization',integrate(p),1)
check('zero_mean_control',integrate(lambda x:p(x)*h(x)),0)
check('symmetric_mean',integrate(lambda x:p(x)*x),.5)
check('exact_analytic_risk',integrate(lambda x:p(x)*h(x)**2),star)
check('least_favorable_CDF_mean',integrate(F),.5)
check('least_favorable_product',integrate(lambda x: F(x)*(1-F(x))/p(x)**2),c)
check('saddle_Cauchy_schwarz',integrate(lambda x:math.sqrt(F(x)*(1-F(x)))),math.sqrt(c))
for j in range(61):
    theta=j/60
    second=(theta*integrate(lambda u:p(theta*u)*h(theta*u)**2,n=4000) + (1-theta)*integrate(lambda u:p(theta+(1-theta)*u)*(h(theta+(1-theta)*u)+1/p(theta+(1-theta)*u))**2,n=4000))
    check('step_risk_'+str(j), second-(1-theta)**2,star,3e-6)
# A nonuniform family of monotone test functions, with exact I.
for power in [1,2,3,5,10,25]:
    I=1/(power+1)
    second=integrate(lambda x:p(x)*(h(x)+x**power/p(x))**2)
    risk=second-I**2
    assert risk<=star+3e-7 and risk>=-1e-7
    checks.append(('monotone_power_'+str(power),risk,star,star-risk))
# Explicit separated density/control designs to test the strict saddle lower bound.
for a in [-.8,-.4,.2,.5,1]:
    pp=lambda x: 1+a*(6*(x-.5)**2-.5)
    assert min(pp(x) for x in [0,.5,1])>0
    # Same equalizer design but not saddle optimal.
    hh=lambda x:1-x-1/(2*pp(x))
    var=integrate(lambda x:pp(x)*hh(x)**2)
    assert var >= star-3e-7
    checks.append(('perturbed_density_'+str(a),var,star,var-star))
print('PASS',len(checks),'checks')
print('c=',repr(c))
print('sharp risk=',repr(star))
print('uniform risk=',repr(1/12))
print('relative improvement=',repr(1-12*star))
for z in checks[-11:]: print(z)
