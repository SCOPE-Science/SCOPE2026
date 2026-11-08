"""Exact checks for a Bernoulli stale-gradient recurrence.

Run with Python >=3.9 and SymPy >=1.10. All symbolic assertions are exact.
Finite enumerations are independent checks, not proofs of the real-parameter theorem.
"""
from fractions import Fraction as F
from itertools import product
import sympy as s

checks = 0

def check(test, message):
    global checks
    if not test:
        raise AssertionError(message)
    checks += 1

p, h, z = s.symbols('p h z', real=True)
lam = s.symbols('lam')
A0 = s.Matrix([[1-h,0],[1,0]])
A1 = s.Matrix([[1,-h],[1,0]])
# The symmetric covariance coordinate order is (E[x_n^2], E[x_n x_{n-1}], E[x_{n-1}^2]).
T = s.Matrix([[1-2*(1-p)*h+(1-p)*h**2, -2*p*h, p*h**2],
              [1-(1-p)*h, -p*h, 0], [1,0,0]])
check(s.expand((s.eye(3)-T).det()-h*(2-h-p*h*h))==0, 'sharp determinant')
check(s.simplify(s.diff(T,h).subs({h:0})[0,0] + s.diff(T,h).subs({h:0})[0,1]+2)==0,
      'derivative of Perron root at origin')
check(s.expand(T.subs(p,0).charpoly(lam).as_expr()-lam**2*(lam-(1-h)**2))==0, 'zero-delay endpoint')
# Direct one-step covariance identity for arbitrary symbolic a,b,c.
a,b,c=s.symbols('a b c')
V=s.Matrix([[a,b],[b,c]])
M=s.expand((1-p)*(A0*V*A0.T)+p*(A1*V*A1.T))
vec=s.Matrix([M[0,0],M[0,1],M[1,1]])
check(all(s.expand(x)==0 for x in vec-T*s.Matrix([a,b,c])), 'covariance propagation')

hp=s.Rational(3,2)
pp=s.Rational(1,4)
Tw=T.subs({h:hp,p:pp})
check(Tw==s.Matrix([[s.Rational(7,16),-s.Rational(3,4),s.Rational(9,16)],
                      [-s.Rational(1,8),-s.Rational(3,8),0],[1,0,0]]),'witness matrix')
chi=s.expand(128*Tw.charpoly(lam).as_expr())
P=128*lam**3-8*lam**2-105*lam-27
check(s.expand(chi-P)==0, 'witness characteristic polynomial')
for val,sign in [(s.Rational(-1),-1),(s.Rational(-1,2),1),(s.Rational(0),-1),
                 (s.Rational(1),-1),(s.Rational(9,8),1)]:
    check(s.sign(P.subs(lam,val))==sign, 'root sign at '+str(val))
G=s.factor((s.eye(3)-z*Tw).inv()[0,0])
expected=(1+s.Rational(3,8)*z)/(1-z/s.Integer(16)-s.Rational(105,128)*z*z-s.Rational(27,128)*z**3)
check(s.cancel(G-expected)==0,'moment generating function')
# Exact finite path enumeration, weighted probabilities, for the initial state (1,0).
vec0=s.Matrix([1,0,0])
for n in range(0,11):
    exact=(Tw**n*vec0)[0]
    enum=s.Rational(0)
    for choices in product((0,1),repeat=n):
        x0=s.Rational(1)
        xm1=s.Rational(0)
        prob=s.Rational(1)
        for delayed in choices:
            xn=x0-hp*(xm1 if delayed else x0)
            xm1,x0=x0,xn
            prob*=pp if delayed else 1-pp
        enum+=prob*x0*x0
    check(enum==exact,'enumerated second moment n='+str(n))

# A0 and A1 norms for weighted infinity norm max(|x_n|, |x_{n-1}|/2).
D=s.diag(1,2)
for A, norm in [(A0.subs(h,hp),s.Rational(1,2)),(A1.subs(h,hp),s.Integer(4))]:
    W=D.inv()*A*D
    check(max(sum(abs(W[i,j]) for j in range(2)) for i in range(2))==norm,'weighted norm')
check((s.Rational(3,4)*s.log(s.Rational(1,2))+s.Rational(1,4)*s.log(4)).simplify()==-s.log(2)/4,'negative log exponent')
check(hp+pp*hp**2>s.Integer(2),'unstable witness point')

print('PASS: '+str(checks)+' independent exact assertions')
print('det(I-T) = h(2-h-p h^2)')
print('witness char polynomial: '+str(P))
print('witness generating function: '+str(G))
for n in (0,4,10):
    print('E[x_'+str(n)+'^2] = '+str((Tw**n*vec0)[0]))
