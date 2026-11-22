"""Exact identities and finite cross-checks for two-noisy-sensor Brownian-bridge IMSE.
Run with Python 3 and SymPy. This checker supplements the complete sign proof in RESULT.md.
"""
from fractions import Fraction
from math import comb
import sympy as s

b, d, eta, u, t, x, y = s.symbols('b d eta u t x y', real=True)
count = 0

def check(condition, label):
    global count
    if condition is not True and condition != s.true:
        raise AssertionError(label)
    count += 1

def equal(a, c, label):
    check(s.cancel(a-c)==0, label)

# Direct posterior calculation for x<=y, with distinct noisy observations.
M = s.Matrix([[x*x*(1-x)**2/3, x*(1-y)*(2*y-x*x-y*y)/6],
              [x*(1-y)*(2*y-x*x-y*y)/6, y*y*(1-y)**2/3]])
K = s.Matrix([[x*(1-x)+eta, x*(1-y)], [x*(1-y), y*(1-y)+eta]])
Jxy = s.cancel(s.Rational(1,6)-s.trace(K.inv()*M))
Jdirect = s.cancel(Jxy.subs({x:(1-b+d)/2, y:(1+b+d)/2}))

# Markov-bridge precision and integrated piecewise interpolation basis.
a=(1-b+d)/2
c=(1-b-d)/2
Q = s.Matrix([[1/a+1/b+1/eta, -1/b],[-1/b,1/b+1/c+1/eta]])
H = s.Matrix([[(a+b)/3,b/6],[b/6,(b+c)/3]])
J = s.cancel((a*a+b*b+c*c)/6+s.trace(H*Q.inv()))
equal(J,Jdirect,'conditional covariance two ways')
Ju = s.factor(J.subs(d*d,u))
G = b*((1-b)**2-u)+2*eta*(1-b*b-u)+4*eta**2
D1 = 12*(b-2*eta-1)*(b*b-b-2*eta)*G
A=(b*b*(b-1)**4-4*b*(b-1)**3*(b+1)*eta+
   4*(b-1)*(b+1)*(5*b*b-2*b-1)*eta**2-16*(3*b*b-1)*eta**3)
B=(-b*b*(b-1)**2+4*b*(b-1)*eta+
   4*(b*b-b-1)*eta**2-8*eta**3)
equal(D1*(Ju-Ju.subs(u,0)),u*(A+u*B),'fixed-gap centering certificate')
AtEnd=s.factor((A+u*B).subs(u,(1-b)**2))
positive_end=(4*b*b*(1-b)**3*eta+
              4*b*(1-b)*(3-b-6*b*b)*eta**2+
              8*(1+2*b-7*b*b)*eta**3)
equal(AtEnd,positive_end,'centering endpoint positive certificate')

D2 = 48*(4*eta+1)*(8*eta+1)*G
N=s.cancel(D2*(Ju-Ju.subs({b:s.Rational(1,2),u:0})))
N2=s.Poly(N,u).nth(2)
equal(N2,-4*(b+2*eta)*(4*eta+1)*(8*eta+1),'large gap concavity')
N0=s.factor(N.subs(u,0))
polyQ=48*b**4-116*b**3+38*b*b+34*b+1
N0_expected=(b*(1-b)**2*(2*b-1)*(6*b-1)+
  2*(b-1)*(2*b-1)*(36*b**3-44*b*b-3*b+1)*eta+
  4*(2*b-1)*polyQ*eta**2+
  16*(2*b-1)*(2*b+1)*(7-4*b*b)*eta**3)
equal(N0,N0_expected,'large gap centered endpoint')
zend=b*(1-b)
Nend_expected=(4*b*(1-b)*(16*b*b-16*b+5)*eta+
 4*(5+36*zend-192*zend**2)*eta**2+
 16*(9-128*zend**2)*eta**3)
equal(s.factor(N.subs(u,(1-b)**2)),Nend_expected,'large gap boundary endpoint')

# The quartic for N0 has a strictly positive Bernstein basis on b in [1/2,1].
q=s.Poly(s.expand(polyQ.subs(b,(1+t)/2)),t)
bernstein=[s.factor(sum(q.nth(j)*s.Rational(comb(i,j),comb(4,j))
                        for j in range(i+1))) for i in range(5)]
check(bernstein==[16,s.Rational(137,8),s.Rational(187,12),s.Rational(43,4),5],
      'Bernstein certificate')

T=s.cancel(Ju.subs(u,0))
D= s.factor(s.diff(T,b))
Hpoly = (b*b*(b-1)**3*(3*b-1)
         -2*eta*b*(b-1)**2*(5*b*b+5*b-2)
         +2*eta**2*(b-1)*(2*b**3+19*b*b-1)
         -16*eta**3*b*(b+1))
equal(D, (b-1)*Hpoly/(6*(b-2*eta-1)**2*(b*b-b-2*eta)**2),
      'symmetric gap derivative')

# Exact Descartes variation argument: H((t)/(3(1+t))) has one sign
# change in ascending powers for every eta>0. The 5 positive
# coefficient zeros are in mutually ordered disjoint rational intervals.
trans=s.Poly(s.cancel((1+t)**6*Hpoly.subs(b,t/(3*(1+t)))),t)
check(trans.degree()==6,'degree transformed')
equal(trans.nth(0),2*eta**2,'transformed constant')
equal(trans.nth(6),-16*eta*(6*eta+1)*(18*eta+1)/243,
      'transformed leading')
intervals={1:(s.Rational(223,100),s.Rational(224,100)),
           2:(s.Rational(96,100),s.Rational(97,100)),
           3:(s.Rational(50,100),s.Rational(51,100)),
           4:(s.Rational(25,100),s.Rational(26,100)),
           5:(s.Rational(9,100),s.Rational(10,100))}
for j,(lo,hi) in intervals.items():
    C=s.factor(trans.nth(j))
    positive_part=s.factor(C/eta) if j==1 else C
    cp=s.Poly(positive_part,eta)
    # Coefficient starts positive and ends negative; Descartes gives one root.
    vals=[cp.nth(k) for k in range(cp.degree()+1)]
    check(vals[0]>0 and vals[-1]<0, f'coefficient #{j} endpoint signs')
    check(sum((v>0)!=(w>0) for v,w in zip(vals,vals[1:]))==1,
          f'coefficient #{j} Descartes signs')
    check(C.subs(eta,lo)>0 and C.subs(eta,hi)<0,
          f'coefficient #{j} root bracket')

# H<0 for every b in [1/3,1] and eta>0, certified by
# nonpositive monomial coefficients after mapping b=(1+3t)/(3(1+t)).
transhi=s.Poly(s.cancel((1+t)**6*Hpoly.subs(b,(1+3*t)/(3*(1+t)))),t)
for j in range(7):
    C=s.Poly(transhi.nth(j),eta)
    for k in range(C.degree()+1):
        check(C.nth(k)<=0,f'high-gap H sign #{j},{k}')

# Root asymptotics follow from simple roots of H after rescaling.
k,z=s.symbols('k z')
equal(s.diff(Hpoly.subs(b,s.Rational(1,3)+k*eta),eta).subs(eta,0),
      -8*(3*k+2)/243,'small noise expansion')
equal(s.limit(Hpoly.subs(b,z/eta)/eta**2,eta,s.oo),
      -2*(8*z-1),'large noise expansion')

# Independent direct covariance calculations with exact rational parameters.
for xx,yy,ee in [(s.Rational(1,3),s.Rational(2,3),s.Rational(1,10)),
                 (s.Rational(1,4),s.Rational(3,4),1),
                 (s.Rational(2,5),s.Rational(3,5),4),
                 (s.Rational(1,2),s.Rational(1,2),s.Rational(1,3))]:
    direct=s.factor(Jxy.subs({x:xx,y:yy,eta:ee}))
    small=s.factor(Ju.subs({b:yy-xx,u:(xx+yy-1)**2,eta:ee}))
    equal(direct,small,'rational posterior instance')
print('PASS',count,'symbolic and exact checks')
