"""Check Dirichlet abundance-threshold versus power-concentration identities.
Requires Python 3 and scipy for floating-point quadrature checks.
This code does not prove the all-parameter uniqueness theorem; that proof is analytic.
"""
from fractions import Fraction as F
from math import comb, isclose
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import beta, betaincc, poch

checks=0

def upper_int(a,b,t):
    # P[Beta(a,b)>t] = P[Binomial(a+b-1,t) <= a-1]
    return sum(F(comb(a+b-1,j))*t**j*(1-t)**(a+b-1-j)
               for j in range(a))

for m in range(2,8):
  for a in range(1,6):
    b=(m-1)*a; s=m*a
    moment=F(m*a*(a+1),s*(s+1))
    for j in range(1,23):
      t=F(j,23)
      exact=moment*(upper_int(a+2,b,t)+(m-1)*upper_int(a,b+2,t)-m*upper_int(a,b,t))
      B=F(1,1)
      # beta(a,b)=(a-1)!(b-1)!/(a+b-1)!
      from math import factorial
      B=F(factorial(a-1)*factorial(b-1),factorial(s-1))
      closed=F(m*(s+2),(b+1)*(s+1))/B*t**a*(1-t)**b*(t-F(a+1,s+2))
      assert exact==closed,(m,a,t,exact,closed)
      checks+=1
    tstar=F(a+1,s+2)
    assert upper_int(a+2,b,tstar)+(m-1)*upper_int(a,b+2,tstar)-m*upper_int(a,b,tstar)==0
    checks+=1

# Independently integrate the Beta conditional moment for noninteger power orders.
for m,a in [(2,.6),(3,.75),(3,1),(4,2),(5,.5)]:
  b=(m-1)*a; s=m*a
  for q in [1.1,1.6,2.4,3.5,6.]:
    c=(m-1)*poch(a,q)/poch(b,q)
    moment=m*poch(a,q)/poch(s,q)
    density=lambda x:x**(a-1)*(1-x)**(b-1)/beta(a,b)
    f=lambda x:x**q+c*(1-x)**q
    g=lambda t:betaincc(a+q,b,t)+(m-1)*betaincc(a,b+q,t)-m*betaincc(a,b,t)
    for t in [.08,.23,.44,.7,.89]:
      integral=m*quad(lambda x:(f(x)-moment)*density(x),t,1,epsabs=1e-10)[0]
      closed=moment*g(t)
      assert isclose(integral,closed,rel_tol=1e-6,abs_tol=2e-9),(m,a,q,t,integral,closed)
      checks+=1
    r=brentq(g,0.00001,0.99999)
    assert g(r-.000001)<0 and g(r+.000001)>0
    checks+=1

# Check high-order limiting zero of the normalized covariance.
for m,a in [(2,1.),(3,1.),(4,3.),(5,.5)]:
  b=(m-1)*a
  root=brentq(lambda t:m*betaincc(a,b,t)-1,1e-8,1-1e-8)
  for t in [.1,.3,.6,.8]:
    actual=betaincc(a+300,b,t)+(m-1)*betaincc(a,b+300,t)-m*betaincc(a,b,t)
    limit=1-m*betaincc(a,b,t)
    assert abs(actual-limit)<1e-7,(m,a,t,actual,limit)
    checks+=1
  q300=brentq(lambda t:betaincc(a+300,b,t)+(m-1)*betaincc(a,b+300,t)-m*betaincc(a,b,t),max(.05,root-.1),min(.95,root+.1))
  assert abs(root-q300)<1e-7,(m,a,root,q300)
  checks+=1
print('PASS',checks,'checks')
