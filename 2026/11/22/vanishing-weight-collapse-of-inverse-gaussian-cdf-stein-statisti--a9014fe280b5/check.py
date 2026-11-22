#!/usr/bin/env python3
"""Reproduce exact identities and numerical checks for inverse-Gaussian CDF-Stein vanishing-weight limits.
Requires numpy, scipy, sympy; no external data or network.
"""
from fractions import Fraction as F
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import invgauss, norm
import sympy as sp

checks=0
def check(cond, msg):
    global checks
    assert bool(cond), msg
    checks+=1

# IG(1,phi) raw moments, with r=1/phi.
r=sp.symbols('r', positive=True)
M={0:sp.Integer(1),1:sp.Integer(1),2:1+r,3:1+3*r+3*r*r,
   4:1+6*r+15*r*r+15*r**3,-1:1+r,-2:1+3*r+3*r*r}
A=1+r
# H = X^2 - X^-1 - 3 A(X-1).
EH2=(M[4]+M[-2]-2*M[1]) - 6*A*(M[3]-M[2]-M[0]+M[-1]) +9*A*A*(M[2]-2*M[1]+M[0])
check(sp.simplify(EH2-6*r**3)==0, 'influence variance 6/phi^3')
check(sp.simplify(M[2]-M[-1])==0,'matching IG second and reciprocal moments')

# Exact normalized sample, one-to-one with unnormalized (1,2,3).
y=[F(1,2),F(1),F(3,2)]
v=sum(x*x for x in y)/3
u=sum(1/x for x in y)/3
thmo=1/(v-1)
thml=1/(u-1)
cmo=(1-thmo*(u-1))/2
cml=(1-thml*(u-1))/2
check(v==F(7,6),'second moment')
check(u==F(11,9),'reciprocal moment')
check(thmo==6,'moment shape')
check(thml==F(9,2),'likelihood shape')
check(cmo==F(-1,6),'moment plateau')
check(cml==0,'likelihood plateau')
check(sum((x-1)**3/x for x in y)/3==v-u,'cubic moment identity')

def profile(t, theta):
    return sum(0.5*(theta+3/float(z)-theta/float(z)**2)*min(float(z),t)-float(z<=t) for z in y)/3
for theta, c in [(float(thmo),float(cmo)),(float(thml),0.0)]:
    for t in [1.51,2.,10.,100.]:
        check(abs(profile(t,theta)-c)<2e-12,'profile plateau')

def statistic(a,theta,mode):
    M=1.5
    weight=(lambda t:math.exp(-a*t)) if mode=='exp' else (lambda t:math.exp(-a*t*t))
    core=sum(quad(lambda t:profile(t,theta)**2*weight(t),float(lo),float(hi),epsabs=1e-11)[0]
             for lo,hi in [(0,.5),(.5,1.0),(1.,1.5)])
    c=profile(M+1,theta)
    if mode=='exp':
        tail=c*c*math.exp(-a*M)/a
    else:
        tail=c*c*math.sqrt(math.pi)*math.erfc(math.sqrt(a)*M)/(2*math.sqrt(a))
    return len(y)*(core+tail)

for a in [1e-2,1e-3,1e-5,1e-7]:
    expmo=statistic(a,float(thmo),'exp')
    normmo=statistic(a,float(thmo),'normal')
    check(abs(a*expmo-3*float(cmo*cmo))<2*a,'exp MO scaled finite sample')
    check(abs(math.sqrt(a)*normmo-3*float(cmo*cmo)*math.sqrt(math.pi)/2)<3*math.sqrt(a),'Gaussian MO scaled finite sample')
    expml=statistic(a,float(thml),'exp')
    normml=statistic(a,float(thml),'normal')
    check(abs(expml-normml)<20*a,'ML finite same unweighted limit')
    if a<1e-4:
        check(a*expml<1e-3 and math.sqrt(a)*normml<1e-2,'ML scaled goes to zero')

# Independent reconstruction in raw coordinates of the Hilbert-valued four-function decomposition.
def Hbasis(t, theta):
    mu=F(2)
    ss=mu*t
    xs=[F(1),F(2),F(3)]
    return sum((F(1)-(theta/(2*mu))*(x-ss)-F(3,2)*(1-ss/x)
                +(theta*mu/F(2))*(1/x-ss/x**2)) for x in xs if x>ss)/3
for theta in (thmo,thml):
    c=(1-theta*(u-1))/2
    for t in (F(0), F(1,10),F(2,5),F(3,5),F(7,10),F(1),F(2),F(3)):
        expected=sum((theta+3/z-theta/z**2)*min(z,t)/2-F(z<=t) for z in y)/3-c
        check(expected==Hbasis(t,theta),'four-function tail decomposition')

# Monte Carlo independent check of the chi-square limiting null law, using inverse-Gaussian direct sampling.
rng=np.random.default_rng(20261117)
phi=2.0
N=1200
rep=7000
x=invgauss.rvs(mu=1/phi, scale=phi,size=(rep,N),random_state=rng)
m=x.mean(axis=1)
ysq=(x*x).mean(axis=1)/(m*m)
yinv=m*(1/x).mean(axis=1)
c=(ysq-yinv)/(2*(ysq-1))
z=np.sqrt(N)*c/math.sqrt(3/(2*phi))
check(abs(float(np.mean(z)))<0.065,'CLT centered')
check(abs(float(np.std(z))-1)<0.075,'CLT unit scale')
q=np.mean(z*z > 3.841458820694124)
check(abs(q-0.05)<0.024,'chi-square 95 percent tail')
print({'checks_passed':checks,'c_MO_exact':str(cmo),'c_ML_exact':str(cml),
       'variance_H':str(sp.factor(EH2)),'MonteCarlo_n':N,'MonteCarlo_replicates':rep,
       'CLT_mean':float(np.mean(z)),'CLT_std':float(np.std(z)),
       'Chi2_95_tail':float(q),
       'finite_exp_mo_a1e-5':1e-5*statistic(1e-5,float(thmo),'exp'),
       'finite_gauss_mo_sqrta1e-5':math.sqrt(1e-5)*statistic(1e-5,float(thmo),'normal')})
