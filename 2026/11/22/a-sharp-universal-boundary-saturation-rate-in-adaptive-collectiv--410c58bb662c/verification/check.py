"""Exact algebraic reproduction of the risk-cost feedback saturation example.

Requires Python 3.10+ and SymPy. The infinite-time statements are proved
analytically in RESULT.md, not certified by finite computation.
"""
from sympy import symbols, Integer, Rational, Matrix, binomial, simplify, factor

x, r, c = symbols('x r c', real=True)
b, m1, m2, t1, t2, t3, t4, a, z = symbols(
    'b mu1 mu2 theta1 theta2 theta3 theta4 alpha beta', positive=True)
# Formal normalized log-cost and log-risk derivatives (without logarithm branches).
m = m1 + m2
s = t3 + t4
k = (a-z)*(t1+t2)/m
rho = ((t1+t2)*m1/m - t1+t4)/s
risk_logit_prime = m1-m*x
cost_logit_prime = (a-z)*(t1-t4-(t1+t2)*x+s*r)
assert simplify(cost_logit_prime-k*risk_logit_prime-(a-z)*s*(r-rho)) == 0

p = dict(b=Integer(1),mu1=Integer(4),mu2=Integer(1),theta1=Integer(1),
         theta2=Integer(4),theta3=Integer(1),theta4=Integer(1),
         alpha=Rational(3,4),beta=Rational(1,5))
K = 2*x*(1-x)
F = Matrix([
    x*(1-x)*(p['b']*K*r-c),
    r*(1-r)*(p['mu1']-(p['mu1']+p['mu2'])*x),
    (p['alpha']-c)*(c-p['beta'])*(p['theta1']-p['theta4']
           -(p['theta1']+p['theta2'])*x+(p['theta3']+p['theta4'])*r)
])
J=F.jacobian((x,r,c))
lam=symbols('lam')
examples = [
    ((Integer(0),Integer(1),p['alpha']), (lam+4)*(lam+Rational(3,4))*(lam+Rational(11,10))),
    ((Rational(4,5),Rational(5,8),p['beta']),
     (lam+Rational(121,80))*(lam**2+Rational(3,25)*lam+Rational(3,50))),
]
for equilibrium, characteristic in examples:
    substitution = dict(zip((x,r,c),equilibrium))
    assert all(simplify(z.subs(substitution))==0 for z in F)
    assert simplify(J.subs(substitution).charpoly(lam).as_expr()-characteristic)==0
# An independent exact sharp-rate equilibrium with both environmental faces decaying equally.
xs = Rational(102,155)
bs = Rational(4805,10812)
sharp_F = F.subs({})
sharp_F = Matrix([
    x*(1-x)*(bs*2*x*(1-x)*r-c),
    r*(1-r)*(4-5*x),
    (Rational(3,4)-c)*(c-Rational(1,5))*(-5*x+2*r)
])
sharp_sub = {x: xs, r: Integer(1), c: Rational(1,5)}
assert all(simplify(v.subs(sharp_sub)) == 0 for v in sharp_F)
sharp_J = sharp_F.jacobian((x,r,c)).subs(sharp_sub)
assert sharp_J.eigenvals() == { -Rational(49,775): 1, -Rational(22,31): 2 }
# Stable by negative real corner roots, and quadratic with positive coefficients.
assert simplify(rho.subs({m1:4,m2:1,t1:1,t2:4,t3:1,t4:1})) == 2
assert k.subs({a:Rational(3,4),z:Rational(1,5),t1:1,t2:4,m1:4,m2:1}) == Rational(11,20)
assert (p['alpha']-p['beta'])*(p['theta3']+p['theta4']) == Rational(11,10)
assert Rational(11,10)/(1+Rational(11,20)) == Rational(22,31)
print('Exact symbolic cancellation, equilibrium identities, stability polynomials and rate: PASS')
