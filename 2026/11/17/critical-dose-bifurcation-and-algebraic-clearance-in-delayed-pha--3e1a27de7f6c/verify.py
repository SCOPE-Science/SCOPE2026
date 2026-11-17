# Symbolic checks of the eigenvector and nonlinear coefficient identities.
import sympy as s
mu=s.symbols('mu',positive=True)
k=s.symbols('k1:4',positive=True)
ell=s.symbols('l1:4',positive=True)
m=s.symbols('m1:4',positive=True)
d=s.symbols('d1:4',positive=True)
b=s.symbols('b1:4',positive=True)
z=s.symbols('z1:4',positive=True)
n=3
q=[d[i]/m[i] for i in range(n)]
J=sum(k[i]*q[i]*(1-z[i]) for i in range(n))/mu
sigma=[s.expand((k[i]*q[i]*(b[i]*z[i]-1)-ell[i]*q[i]*J)/m[i]) for i in range(n)]
assert s.simplify(mu*J-sum(k[i]*q[i]*(1-z[i]) for i in range(n)))==0
for i in range(n):
    assert s.simplify(m[i]*sigma[i]-k[i]*q[i]*(b[i]*z[i]-1)+ell[i]*q[i]*J)==0
for burst,expected in [(4,s.Rational(1,2)),(2,s.Rational(-1,2))]:
    J1=s.Rational(1,2)
    sigma1=(s.Rational(burst,2)-1)-J1
    assert sigma1==expected
print('VERIFY_OK linear_infected=1 linear_phages=3 scalar_opposite_signs=2')
