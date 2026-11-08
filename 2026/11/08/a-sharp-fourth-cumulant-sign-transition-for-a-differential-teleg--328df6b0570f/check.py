"""Reproduce exact stationary moment identities and the unique excess-kurtosis sign boundary.
Usage: python check.py
Requires Python 3 and SymPy. No randomness or external files are used.
"""
import sympy as sp
from functools import lru_cache

a,b,g = sp.symbols('a b g', positive=True)
@lru_cache(None)
def rec(i,j,k):
    if i == j == 0:
        return sp.Integer(1) if k == 0 else sp.Integer(0)
    n=i*a+j*b+2*g*k
    v=sp.Integer(0)
    if i:v+=i*a*rec(i-1,j,1-k)
    if j:v+=j*b*rec(i,j-1,1-k)
    return sp.factor(v/n)
def contrast(n):
    return sp.factor(sum(sp.binomial(n,j)*(-1)**j*rec(n-j,j,0) for j in range(n+1)))
S=a+b
eta=a*b/S**2
x=g/S
Q=(9*eta**2*(2+eta)-4*eta*(3+8*eta)*x
   -8*(3+5*eta+13*eta**2)*x**2
   -8*(9+4*eta)*x**3-48*(1+eta)*x**4)
den=(a+b)*(a+3*b)*(3*a+b)*(a+2*g)**2*(b+2*g)**2*(3*a+2*g)*(3*b+2*g)*(a+2*b+2*g)*(2*a+b+2*g)
variance=2*g*(a-b)**2/((a+b)*(a+2*g)*(b+2*g))
formula=12*g*(a-b)**4*S**6*Q/den
v=contrast(2)
k=sp.factor(contrast(4)-3*v**2)
assert sp.cancel(v-variance)==0
assert sp.cancel(k-formula)==0
assert sp.cancel(contrast(1))==0 and sp.cancel(contrast(3))==0
print('PASS: symbolic generator recurrence, variance, fourth cumulant factorization, odd moments')

# Independent linear stationary-generator solve rather than the recursive evaluation.
def direct(aa,bb,gg):
    indices=[(i,j,k) for i in range(5) for j in range(5-i) for k in (0,1)]
    n=len(indices); loc={t:h for h,t in enumerate(indices)}
    M=sp.zeros(n); rhs=sp.zeros(n,1)
    for h,(i,j,k) in enumerate(indices):
        if i==j==0:
            M[h,h]=1;rhs[h]=1 if k==0 else 0
            continue
        M[h,h]=i*aa+j*bb+2*gg*k
        if i:M[h,loc[(i-1,j,1-k)]]=-i*aa
        if j:M[h,loc[(i,j-1,1-k)]]=-j*bb
    values=M.inv()*rhs
    def moment(n):return sum(sp.binomial(n,j)*(-1)**j*values[loc[(n-j,j,0)]] for j in range(n+1))
    vv=moment(2)
    return sp.factor(vv),sp.factor(moment(4)-3*vv**2)

cases=[(1,2,sp.Rational(1,10)),(1,2,sp.Rational(1,3)),(1,2,1),(2,3,sp.Rational(1,7)),(3,5,2),(1,3,sp.Rational(2,9)),(1,1,2),(7,7,1)]
for aa,bb,gg in cases:
    vd,kd=direct(*map(sp.Rational,(aa,bb,gg)))
    subs={a:aa,b:bb,g:gg}
    assert vd==sp.factor(variance.subs(subs))
    assert kd==sp.factor(formula.subs(subs))
print('PASS:',len(cases),'independent exact-rational full stationary-generator solves')

# Quartic coefficients have one sign change (+ then all -) in descending powers,
# and Q is strictly decreasing on x>0 for all eta>0.
h=sp.symbols('h', positive=True)
t=sp.symbols('t',positive=True)
q=sp.Poly((9*h**2*(2+h)-4*h*(3+8*h)*t
   -8*(3+5*h+13*h**2)*t**2-8*(9+4*h)*t**3-48*(1+h)*t**4),t)
assert all(all(coef >= 0 for coef in sp.Poly(-c,h).all_coeffs())
           and any(coef > 0 for coef in sp.Poly(-c,h).all_coeffs())
           for c in q.all_coeffs()[:-1])
assert sp.simplify(q.all_coeffs()[-1]-9*h**2*(2+h))==0
print('PASS: quartic coefficient sign audit and unique positive-root argument')

r=sp.symbols('r',positive=True)
example=sp.factor(formula.subs({a:1,b:2,g:r}))
expected= -2*r*(66*r**4+267*r**3+385*r**2+129*r-90)/(35*(r+1)**2*(r+2)*(r+3)*(2*r+1)**2*(2*r+3)*(2*r+5))
assert sp.cancel(example-expected)==0
assert example.subs(r,sp.Rational(1,10))>0
assert example.subs(r,sp.Rational(1,3))<0
print('PASS: explicit crossover example; signed exact rational evaluations')
