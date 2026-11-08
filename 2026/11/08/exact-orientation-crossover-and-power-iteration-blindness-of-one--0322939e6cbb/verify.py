"""Exact subspace-iteration risk checks for Gaussian and coordinate-sign sketches.

Python >=3.10, sympy >=1.11, numpy >=1.23, scipy >=1.9.
No external data. Finite checks supplement the analytic proof in RESULT.md.
"""
from itertools import product
import math
import numpy as np
import sympy as s
from scipy.integrate import quad

checks = 0

def check(cond, msg):
    global checks
    if not bool(cond):
        raise AssertionError(msg)
    checks += 1

p, a, u = s.symbols('p a u', real=True, positive=True)
k, t = s.symbols('k t', real=True, positive=True)
D, E = p*p+1, p*p-1
G = 1+(a-1)/(p+1)
S = 1+(a-1)*(D+E*u)/(D*D-E*E*u)
check(s.factor(S.subs(u,0)-(1+(a-1)/(p*p+1)))==0,'aligned signs')
check(s.factor(S.subs(u,1)-(a+1)/2)==0,'diagonal signs')
check(s.factor(S-G-(a-1)*p*(p-1)*((p+1)**2*u-(p*p+1))/((p+1)*(D*D-E*E*u)))==0,'comparison factor')
check(s.simplify(S.subs(u,(p*p+1)/(p+1)**2)-G)==0,'unique crossover')
check(s.factor(s.diff(S,u)-(a-1)*E*D*(D+E)/(D*D-E*E*u)**2)==0,'monotonicity in u')
check(s.factor(s.diff((p*p+1)/(p+1)**2,p)-2*(p-1)/(p+1)**3)==0,'crossover shifts with power')
check(s.simplify(s.limit(p**2*(S-1),p,s.oo)-(a-1)*(1+u)/(1-u))==0,'off-axis asymptotic')
# For an interior u<1 the leading coefficient is algebraically determined.
check(s.factor((S-1)/(a-1)-(D+E*u)/(D*D-E*E*u))==0,'off-axis exact representation')
# At q=0, comparison reduces to harmonic/geometric/arithmetic sequence.
S0=s.factor(S.subs({a:k*k,p:k,u:t*t}))
check(s.simplify(S0-2*k*k*(k*k+1)/((k*k+1)**2-(k*k-1)**2*t*t))==0,'q=0 original closed form')
check(s.factor(S0.subs(t,0)-2*k*k/(k*k+1))==0,'harmonic')
check(s.factor(S0.subs(t,1)-(k*k+1)/2)==0,'arithmetic')
check(s.simplify(G.subs({a:k*k,p:k})-k)==0,'geometric')
check(s.factor(S0.subs(t,0)*S0.subs(t,1)-k*k)==0,'HGA identity')

# Exact rational arithmetic across integer power counts and rational angle parameters.
for kap in [s.Rational(3,2),s.Rational(2),s.Rational(3),s.Rational(5),s.Rational(9)]:
    for q in [0,1,2,3,5]:
        pp=kap**(2*q+1)
        g=s.factor(G.subs({a:kap*kap,p:pp}))
        thresh=(pp*pp+1)/(pp+1)**2
        for tt in [s.Rational(0),s.Rational(3,5),s.Rational(4,5),s.Rational(24,25),s.Rational(1)]:
            sn=s.factor(S.subs({a:kap*kap,p:pp,u:tt*tt}))
            rp=s.factor(1+(kap*kap-1)*(1-tt)/(pp*pp*(1+tt)+(1-tt)))
            rm=s.factor(1+(kap*kap-1)*(1+tt)/(pp*pp*(1-tt)+(1+tt)))
            check(s.factor(sn-(rp+rm)/2)==0,'direct binary expectation')
            check(bool(sn>0),'positive risk')
            check((sn<g)==(tt*tt<thresh),'strict sign Gaussian comparison')
            check((sn>g)==(tt*tt>thresh),'reverse comparison')

# Independent angular quadrature of exact Gaussian transfer for arbitrary q.
for kap in [1.1,1.4,2.,3.,9.]:
    for q in [0,1,2]:
        if kap**(2*q+1)>120:
            continue
        pp=kap**(2*q+1)
        integral,err=quad(lambda phi: 1+(kap**2-1)*math.sin(phi)**2/(pp**2*math.cos(phi)**2+math.sin(phi)**2),
                          0,2*math.pi,epsabs=2e-9,epsrel=2e-12,limit=900)
        pred=1+(kap**2-1)/(pp+1)
        check(abs(integral/(2*math.pi)-pred)<2e-8,'Gaussian direct angular integral')

# Direct independent matrix experiment with m=3, n=2.
U=np.array([[3/5,0], [0,1], [4/5,0]],dtype=float)
check(np.allclose(U.T@U,np.eye(2)),'orthonormal tall left factor')
for kap in [1.1,2.,3.,9.]:
    for q in [0,1,2,3]:
        for theta in [0,0.17,math.atan2(3,4),math.pi/4,math.pi/2]:
            V=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
            A=U@np.diag([kap,1.])@V.T
            T=A@A.T
            m=0.
            for omega in product([-1.,1.],repeat=2):
                y=np.linalg.matrix_power(T,q)@(A@np.array(omega))
                Q=np.outer(y,y)/(y@y)
                m+=np.linalg.norm(A-Q@A,'fro')**2/4.
            pp=kap**(2*q+1)
            tt=abs(math.sin(2*theta))
            pred=1+(kap**2-1)*.5*((1-tt)/(pp*pp*(1+tt)+(1-tt)) + (1+tt)/(pp*pp*(1-tt)+(1+tt)))
            check(abs(m-pred)<1e-8,'direct tall-matrix range finder')

print(f'PASS: {checks} exact algebra, rational enumeration, integration and matrix assertions')
print('For kappa=3, q=0: sign best 9/5, Gaussian 3, sign worst 5.')
print('For kappa=3, q=1: sign best 1+8/730, Gaussian 1+8/28, sign worst 5.')
