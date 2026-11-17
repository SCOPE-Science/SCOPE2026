"""Reproduce the quintic-oscillator crossover checks.

Requires Python 3, scipy, sympy. The all-parameter proof is in RESULT.md;
numerical integrations below supplement, rather than replace, that proof.
"""
from math import exp, pi, sqrt
from scipy.integrate import quad
from scipy.special import beta as Beta
from sympy import symbols, exp as Sexp, diff, simplify

x, v, alpha, beta = symbols('x v alpha beta', real=True)
p2 = Sexp(alpha*x**4/2)
Vprime = p2*(x+beta*x**5)
dH = (diff(p2,x)*v*v/2+Vprime)*v+p2*v*(-x-alpha*x**3*v*v-beta*x**5)
assert simplify(dH)==0


def integral(q, u, p):
    return quad(lambda r: r**p*exp(q*r**4/2), u, 1, epsabs=1e-12)[0]


def scaled(q, epsilon=0):
    # u=1-w*w removes the square-root singularity at u=1.
    def f(w):
        u=1-w*w
        if w==0:
            return 2*exp(q/4)/sqrt(exp(q/2)*(1+epsilon))
        return 2*w*exp(q*u**4/4)/sqrt(integral(q,u,5)+epsilon*integral(q,u,1))
    return 2*sqrt(2)*quad(f,0,1,epsabs=1e-10,limit=100)[0]


endpoint=(2*sqrt(3)/3)*Beta(1/6,1/2)
assert abs(scaled(0)-endpoint)<1e-9
vals=[scaled(q) for q in [0,1,3,10,30,100]]
assert all(u>v for u,v in zip(vals,vals[1:]))
assert abs(sqrt(100)*vals[-1]/(2*pi)-1)<.05
count=0
for A in (1.2,3,8):
    for beta_value in (.7,2):
        for q in (0,1,7):
            eps=1/(beta_value*A**4)
            true=scaled(q,eps)
            asymp=scaled(q)
            lower=asymp/sqrt(1+3*eps)
            assert lower-1e-8<true<asymp+1e-8,(A,beta_value,q,true,lower,asymp)
            count+=1

# Two-point exact inequality underlying the uniform all-scale bracket.
# For each u and q>=0, I(q,u)/J(q,u) is a tilted mean of r^4,
# whose q-derivative is half of a nonnegative variance.
for u in (0,.2,.6,.92):
    for q in (0,.1,2,8):
        I=integral(q,u,5); J=integral(q,u,1)
        assert J/I < 3+1e-9
print('CHECK_OK energy, beta endpoint, monotonicity, large-q limit,')
print(f'{count} finite-amplitude universal brackets, 16 kernel ratios')
