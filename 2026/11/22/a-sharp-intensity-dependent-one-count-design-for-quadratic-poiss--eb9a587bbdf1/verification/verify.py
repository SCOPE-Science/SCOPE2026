#!/usr/bin/env python3
"""Exact polynomial and independent numerical checks for a Poisson count-quadrature design."""
import math
import random
import sympy as S
from sympy.functions.combinatorial.numbers import stirling

x, L, mu, k = S.symbols('x L mu k', real=True)
checks = 0

def check_equal(lhs, rhs, label):
    global checks
    assert S.simplify(lhs-rhs) == 0, label
    checks += 1

A = 1 - S.Rational(2,3)*x
B = x/6 + L*(1-x)**2
C = L*(1-x)**2/2 + L**2*(1-x)**3/3
G = A*k*k + B*k + C
V = S.factor(L*x*((A+B)**2 + L*x*(6*A*A+4*A*B) + 4*(L*x)**2*A*A))
V_poly = L*x*(L**2*(4*x**4-24*x**2+36) + L*(44*x**3-120*x**2+36*x+72) + 9*x**2-36*x+36)/36
check_equal(V,V_poly,'explained variance polynomial')
P0 = 27*x*x-72*x+36
P1 = 176*x**3-360*x*x+72*x+72
P2 = 20*x**4-72*x*x+36
P = P0 + L*P1 + L**2*P2
check_equal(S.diff(V,x),L*P/36,'derivative polynomial')
check_equal(P0,27*(x-S.Rational(2,3))*(x-2),'linear coefficient factor')
check_equal(P2,20*(x*x-S.Rational(3,5))*(x*x-3),'quadratic coefficient factor')
check_equal(P1.subs(x,S.Rational(2,3)),S.Rational(328,27),'P1 left endpoint')
check_equal(P2.subs(x,S.Rational(2,3)),S.Rational(644,81),'P2 left endpoint')
check_equal(P1.subs(x,S.sqrt(S.Rational(3,5))),-144+S.Rational(888,25)*S.sqrt(15),'P1 upper endpoint')
check_equal(-P1.subs(x,S.Rational(2,3))/S.diff(P0,x).subs(x,S.Rational(2,3)),S.Rational(82,243),'small-intensity slope')
check_equal(-P1.subs(x,S.sqrt(S.Rational(3,5)))/S.diff(P2,x).subs(x,S.sqrt(S.Rational(3,5))),S.Rational(37,20)-S.sqrt(15)/2,'large-intensity correction')

# Independent covariance derivation for Q = integral N_t^2 dt.
s,t=S.symbols('s t',real=True)
lam=S.symbols('lam',positive=True)
cs=4*lam**3*s*s*t+lam**2*(4*s*s+2*s*t)+lam*s
varQ=S.factor(2*S.integrate(S.integrate(cs,(t,s,1)),(s,0,1)))
check_equal(varQ,lam/3+S.Rational(7,6)*lam**2+S.Rational(8,15)*lam**3,'unconditional variance')

# Independent Touchard moments: Var(K^2) and Cov(K^2,K).
touch=[sum(stirling(n,j,kind=2)*mu**j for j in range(n+1)) for n in range(5)]
check_equal(touch[4]-touch[2]**2,4*mu**3+6*mu**2+mu,'fourth Poisson moment')
check_equal(touch[3]-touch[2]*touch[1],2*mu**2+mu,'third Poisson covariance')

# Optimal high-rate Bayes risk and gain from the classical linear-count choice.
v_inf=S.sqrt(S.Rational(3,5))
H=x*(x*x-3)**2/9
ropt=S.Rational(8,15)-H.subs(x,v_inf)
rlinear=S.Rational(8,15)-H.subs(x,S.Rational(2,3))
check_equal(ropt,S.Rational(8,15)-16*S.sqrt(15)/125,'high-rate optimum')
check_equal(rlinear,S.Rational(542,10935),'high-rate risk at 2/3')

# Root isolation, monotonicity in intensity, positive finite risk, direct Poisson-moment sums.
for lam_num in (S.Rational(1,100),S.Rational(1,10),S.Rational(1,2),S.Rational(1),S.Rational(2),S.Rational(10),S.Rational(100)):
    polynomial=S.Poly(P.subs(L,lam_num),x)
    roots=[float(S.re(z)) for z in S.nroots(polynomial,maxsteps=150) if abs(float(S.im(z)))<1e-12 and 0<float(S.re(z))<1]
    assert len(roots)==1 and 2/3<roots[0]<math.sqrt(3/5)
    checks+=1
    root=roots[0]
    dvdl=float((P1+2*L*P2).subs({x:root,L:lam_num}))
    dvdx=float(S.diff(P,x).subs({x:root,L:lam_num}))
    assert dvdl>0 and dvdx<0
    checks+=1
    qvar=float(varQ.subs(lam,lam_num))
    vopt=float(V.subs({x:root,L:lam_num}))
    vlin=float(V.subs({x:S.Rational(2,3),L:lam_num}))
    assert qvar>vopt>vlin>0
    checks+=1

# Conditional-expectation check via an independent finite binomial/Poisson construction.
# Given K=k at x, pre-x event times are k independent U[0,x].
# Poisson events after x are independent.  The formula can be checked
# through the exact first/second moments of the two contributions.
for xx in (S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),S.Rational(9,10)):
  for ll in (S.Rational(1,5),S.Rational(1),S.Rational(7,2)):
    for kk in range(8):
      # For pre-x, N_t = Binomial(k,t/x). For after x, N_t=k+Pois(ll(t-x)).
      z=S.symbols('z')
      pre=S.integrate(kk*z/xx*(1-z/xx)+kk**2*z*z/(xx*xx),(z,0,xx))
      post=S.integrate(kk**2+2*kk*ll*(z-xx)+(ll*(z-xx))**2+ll*(z-xx),(z,xx,1))
      check_equal(pre+post,G.subs({x:xx,L:ll,k:kk}),'conditional mean moment check')

# Independent seeded jump-time experiment for one sample, with event-time Q exact.
random.seed(20261119)
lam_num=3.0
xx=0.75568449803559
sum_g=sum_q=sum_gq=sum_g2=0.0
samples=300000
for _ in range(samples):
    # Knuth Poisson generator, independent path generated from sorted uniforms.
    threshold=math.exp(-lam_num)
    z=1.0; count=0
    while True:
        z*=random.random()
        if z<=threshold: break
        count+=1
    points=sorted(random.random() for i in range(count))
    K=sum(point<=xx for point in points)
    Q=sum((2*i+1)*(1-u) for i,u in enumerate(points))
    AA=1-2*xx/3
    BB=xx/6+lam_num*(1-xx)**2
    CC=lam_num*(1-xx)**2/2+lam_num**2*(1-xx)**3/3
    g=AA*K*K+BB*K+CC
    sum_g+=g;sum_q+=Q;sum_gq+=g*Q;sum_g2+=g*g
emp_cov=sum_gq/samples-(sum_g/samples)*(sum_q/samples)
emp_var=sum_g2/samples-(sum_g/samples)**2
theo=float(V.subs({L:lam_num,x:xx}))
assert abs(emp_cov-theo)<.17 and abs(emp_var-theo)<.17, (emp_cov,emp_var,theo)
checks+=2
print('PASS:',checks,'exact identities, direct moment comparisons, root checks, and simulated covariance checks')
print('lambda=3, optimal u=',xx,'theoretical explained variance=',theo,'empirical covariance=',emp_cov)
print('high-intensity Bayes-risk reduction vs u=2/3 =',float(1-ropt/rlinear))
