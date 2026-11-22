"""Reproduce the phase-polarization and optimal-reset theorem from stationary resolvents.
Requires numpy, scipy, and sympy; does not require any external data.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad
import sympy as sp

count=0

def test(ok, context=''):
    global count
    assert ok, context
    count+=1

def roots(r, delta, beta, diff, speed):
    t=r+beta
    # Characteristic polynomial of the stationary spatial resolvent in u=lambda².
    c2=diff*speed*speed
    c1=diff*t*t+speed*speed*(r+delta)
    c0=r*t*(t+delta)
    disc=c1*c1-4*c2*c0
    assert disc>0
    lm2=2*c0/(c1+math.sqrt(disc))
    lP2=(c1+math.sqrt(disc))/(2*c2)
    return math.sqrt(lm2),math.sqrt(lP2)

def vals(r,delta,beta,diff,speed):
    lo,hi=roots(r,delta,beta,diff,speed)
    t=r+beta
    alpha=t/speed
    q=speed*lo/t
    # Residues for stationary diffusive-mode density; two reset preparations.
    def amplitudes(reset):
        # numerator N(-l²) = r(t²-v²*l²) for D; r beta t for B.
        nlo=r*(t*t-speed*speed*lo*lo) if reset=='D' else r*beta*t
        nhi=r*(t*t-speed*speed*hi*hi) if reset=='D' else r*beta*t
        a=nlo/(2*diff*speed*speed*lo*(hi*hi-lo*lo))
        b=-nhi/(2*diff*speed*speed*hi*(hi*hi-lo*lo))
        return a,b
    return lo,hi,q,alpha,amplitudes

def densities(x,r,delta,beta,diff,speed,reset):
    l,h,q,alpha,A=vals(r,delta,beta,diff,speed)
    a,b=A(reset)
    assert x>0
    p0=a+b*math.exp(-(h-l)*x)
    # Values here are rescaled by exp(lambda_minus*x) for far-tail stability.
    plus=0.0
    minus=0.0
    for lam,c in [(l,a),(h,b)]:
        plus+=delta/(2*speed)*c*(math.exp(-(lam-l)*x)/(alpha-lam)-2*lam/(alpha*alpha-lam*lam)*math.exp(-(alpha-l)*x))
        minus+=delta/(2*speed)*c*math.exp(-(lam-l)*x)/(alpha+lam)
    if reset=='B': plus+=r/(2*speed)*math.exp(-(alpha-l)*x)
    return p0,plus,minus

# Exact polynomial check: physical root and optimizer cubic critical derivative.
R,z,a,b=sp.symbols('R z a b',positive=True)
F=(R+1)*(1-z)*(R+b-a*(R+1)**2*z)-b
z1=(2*R+b+1)/(3*a*(R+1)**2)
num=sp.factor(F.subs(z,z1)*9*a*(R+1))
expected=sp.factor((3*a*(R+1)**2-(2*R+b+1))*(R+2*b-1)-9*a*b*(R+1))
test(sp.simplify(num-expected)==0,'optimality cubic algebra')
test(sp.simplify(sp.diff(F,R)/(1-z)-(2*R+b+1-3*a*(R+1)**2*z))==0,'partial derivative')
test(sp.simplify(sp.diff(z1,R)+2*(R+b)/(3*a*(R+1)**3))==0,'z1 decreasing')

# Physical root parameter survey and optimization/phase-resolvent checks.
for (delta,beta,diff,speed) in [(1.,1.,1.,1.),(.23,1.8,.08,2.3),(8.,.3,2.,.9),(1.3,.7,.37,5.),(.01,4.,7.,.21),(3.,.04,.15,.8),(3.,1.2,.05,1.),(.2,10.,15.,1.)]:
  aa=diff*beta/(speed*speed); bb=delta/beta
  def q_of_R(rr): return vals(rr*beta,delta,beta,diff,speed)[2]
  opt=minimize_scalar(lambda x:-q_of_R(x),bounds=(1e-6,1e5),method='bounded',options={'xatol':1e-10})
  test(opt.success and opt.x>0)
  minR=max(0.,1-2*bb)
  def z2(RR): return 1-3*bb/((RR+1)*(RR+2*bb-1))
  def z_1(RR): return (2*RR+bb+1)/(3*aa*(RR+1)**2)
  rstar=brentq(lambda RR:z2(RR)-z_1(RR),minR+1e-9,1e8,xtol=1e-12)
  test(abs(math.log(opt.x/rstar))<5e-5,(opt.x,rstar,aa,bb))
  test(abs(q_of_R(rstar)**2-z_1(rstar))<1e-9)
  for scale in [1e-4,.1,1.,100.]:
    rr=beta*scale
    lo,hi,q,alpha,amps=vals(rr,delta,beta,diff,speed)
    test(0<lo<alpha<hi)
    test(abs((rr+delta-diff*lo*lo)*((rr+beta)**2-(speed*lo)**2)-beta*delta*(rr+beta))<1e-6*(1+rr+delta+speed)**4)
    for reset in ['D','B']:
      c,d=amps(reset)
      test(c>0)
      # independently numerical inversion of p0 characteristic function at x=0,
      # using Fourier inversion via scalar integration rather than partial fractions
      def P(k):
        top=rr*((rr+beta)**2+(speed*k)**2) if reset=='D' else rr*beta*(rr+beta)
        bot=(rr+delta+diff*k*k)*((rr+beta)**2+(speed*k)**2)-beta*delta*(rr+beta)
        return top/bot
      inverse=quad(lambda k:P(k),0,np.inf,epsabs=2e-9,epsrel=2e-9,limit=150)[0]/math.pi
      test(abs((c+d)-inverse)<2e-7*max(1,abs(inverse)))
      x=50/min(alpha-lo,hi-lo)
      p0,pp,pm=densities(x,rr,delta,beta,diff,speed,reset)
      test(min(p0,pp,pm)>0)
      pol=(pp-pm)/(pp+pm)
      test(abs(pol-q)<1e-6,(pol,q,rr,reset))
  small=1e-7
  asymptotic=(1+bb)/(aa+bb)*small
  test(abs(q_of_R(small)**2/asymptotic-1)<2e-5)
  huge=1e6
  test(abs(q_of_R(huge)**2*aa*huge-1)<2e-4)

print('PASS',count,'independent symbolic/numerical assertions')
print('benchmark', 'D=v=beta=delta=1', 'r*=',brentq(lambda RR:1-3/((RR+1)*(RR+1)) - (2*RR+2)/(3*(RR+1)**2),0,100))
