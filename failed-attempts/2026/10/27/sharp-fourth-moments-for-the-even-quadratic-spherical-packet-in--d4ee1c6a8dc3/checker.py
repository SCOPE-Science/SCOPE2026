"""Independent symbolic checks for sharp even-quadratic spherical fourth moments.
Requires sympy; finite checks supplement the analytic proof.
"""
import sympy as s
n,r=s.symbols('n r',positive=True)
gamma=2*s.sqrt(2)*(n-2)*s.sqrt(n+2)/((n+4)*s.sqrt(n-1))
delta=3*(n+2)*(5*n*n-13*n+12)/((n-1)*(n+4)*(n+6))
N=r**4+6*r**2+4*gamma*r+delta
F=N/(1+r**2)**2
poly=2*r**3+3*gamma*r**2+(delta-3)*r-gamma
assert s.simplify(s.diff(F,r)+4*poly/(1+r**2)**3)==0
assert s.simplify(delta-3*n*(n+2)/( (n+4)*(n+6))*(1+4*(n*n-3*n+3)/(n*(n-1))))==0
assert s.simplify(gamma-2*s.sqrt(2)*(n-2)*s.sqrt(n+2)/((n+4)*s.sqrt(n-1)))==0
# Direct Gegenbauer/zonal moments from the beta law of x_1^2.
t=s.symbols('t')
checks=0
for dim in range(2,26):
    a=s.Rational(dim,1)
    # E[x_1^(2j)]=(1/2)_j/(n/2)_j.
    Ex=lambda j:s.rf(s.Rational(1,2),j)/s.rf(a/2,j)
    q=t-1/a
    E=lambda p:s.factor(sum(s.expand(p).coeff(t,j)*Ex(j) for j in range(5)))
    var=E(q**2)
    mu3=E(q**3)
    mu4=E(q**4)
    assert s.simplify(var-2*(a-1)/(a*a*(a+2)))==0
    assert s.simplify(mu4/var**2-delta.subs(n,dim))==0
    if dim>2: assert abs(float(mu3/var**s.Rational(3,2))-float(gamma.subs(n,dim)))<1e-11
    else: assert mu3==0
    if dim==2:
        assert s.simplify(F.subs({n:2,r:s.sqrt(3)/2})-s.Rational(15,7))==0
    if dim==4:
        assert s.simplify(F.subs({n:4,r:s.Rational(1,2)})-s.Rational(21,5))==0
    checks+=6
print(f'PASS: {checks} normalized-moment, derivative, and special-value symbolic assertions')
