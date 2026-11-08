"""Reproduce the exact quadratic slaving and cubic infection coefficients."""
import sympy as sp

mu, alpha, delta, gamma, sigma, eps1, eps2 = sp.symbols(
    'mu alpha delta gamma sigma eps1 eps2', positive=True
)
I = sp.Symbol('I')
beta = mu + alpha
A, B = mu + delta, mu + gamma
a = alpha / A
c = delta * a / B
K = beta * (1 + a + (1 - sigma) * c)
b = (a * K + (1 - sigma) * beta * c - eps1 * delta * a) / A
d = (c * K + delta * b + eps1 * delta * a - beta * c - eps2 * gamma * c) / B
L = beta * (b + (1 - sigma) * d)

# These equations are the exact coefficient identities for the full model.
checks = [
    alpha - A*a,
    delta*a - B*c,
    A*b - a*K - (1 - sigma)*beta*c + eps1*delta*a,
    B*d - c*K - delta*b - eps1*delta*a + beta*c + eps2*gamma*c,
    K - beta*(1+a+(1-sigma)*c),
    L - beta*(b+(1-sigma)*d),
]
for expression in checks:
    assert sp.cancel(expression) == 0
# Both feedback functions have the same leading infection Taylor jet.
R = a*I + b*I**2
C = c*I + d*I**2
S = 1-I-R-C
assert sp.expand(S*I-I).coeff(I,1) == 0
assert sp.expand(S*I-I).coeff(I,0) == 0
sample = {mu:1,alpha:1,delta:1,gamma:1,sigma:1}
assert sp.cancel(K.subs(sample)-3) == 0
assert sp.cancel(L.subs(sample)-(3-eps1)/2) == 0
assert L.subs({**sample,eps1:0,eps2:2}) > 0
assert L.subs({**sample,eps1:3,eps2:2}) == 0
assert L.subs({**sample,eps1:6,eps2:2}) < 0
# Independently evaluate the original full differential equations on exact
# rational jets, for both nonlinear choices of infection-driven feedback.
from itertools import product
jet_checks = 0
for sig, er, ec, gam in product((sp.Rational(0), sp.Rational(1,2), sp.Rational(1)),
                                (sp.Rational(0), sp.Rational(1), sp.Rational(5)),
                                (sp.Rational(0), sp.Rational(2)),
                                (sp.Rational(1), sp.Rational(2))):
    par = {mu:sp.Rational(1),alpha:sp.Rational(2),delta:sp.Rational(3),
           gamma:gam,sigma:sig,eps1:er,eps2:ec}
    bb=beta.subs(par)
    aa=a.subs(par)
    cc=c.subs(par)
    b2=b.subs(par)
    d2=d.subs(par)
    k2=K.subs(par)
    l2=L.subs(par)
    rr=aa*I+b2*I**2
    cv=cc*I+d2*I**2
    sv=1-I-rr-cv
    ip=sp.expand(bb*I*(sv+sig*cv-1))
    for gg in (I,sv*I):
        rp=sp.expand(2*I+(1-sig)*bb*cv*I-(1+3)*rr-er*3*gg*rr)
        cp=sp.expand(3*rr-(1+gam)*cv-bb*cv*I+er*3*gg*rr-ec*gam*gg*cv)
        resr=sp.expand(rp-(aa+2*b2*I)*ip)
        resc=sp.expand(cp-(cc+2*d2*I)*ip)
        for residual in (resr,resc):
            for j in range(3):
                assert residual.coeff(I,j)==0
                jet_checks+=1
        assert ip.coeff(I,2)==-k2
        assert ip.coeff(I,3)==-l2
        jet_checks+=2
print(f'VERIFY_OK exact_coefficient_identities=6 feedback_linear_jet=2 critical_sample_checks=5 exact_jet_checks={jet_checks}')
