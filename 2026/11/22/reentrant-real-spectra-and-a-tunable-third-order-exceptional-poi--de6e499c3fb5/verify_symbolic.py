"""Exact algebra checks for the closed-triangle PT star model.
Run with: python verify_symbolic.py (requires SymPy).
"""
import sympy as s
x, u, k = s.symbols('x u k', positive=True)
t = u*((u*u-k)**2+2*k)/(u*u+k)
G = s.factor(t*t + k+2 - 2*u*u-t/u)
P = lambda T, Gammasq: s.expand(x**4+(Gammasq-T**2-(k+2))*x*x-2*T*x+k*(T*T-Gammasq))
assert s.simplify(P(t,G).subs(x,-u)) == 0
assert s.simplify(s.diff(P(t,G),x).subs(x,-u)) == 0
assert s.simplify(G-u*u*(u*u-k-1)**2*((u*u-k)**2+2*k+2*u*u)/(u*u+k)**2)==0
assert s.simplify(s.diff(t,u) - (u*u-k)*(3*u**4+6*k*u*u-k*(k+2))/(u*u+k)**2)==0
assert s.simplify((u*u+G-t*t) + 2*u*u*(u*u-k-1)/(u*u+k))==0
assert s.simplify(P(u,1).subs(k,u*u)-(x+u)**2*((x-u)**2-1))==0
Tstar = 4*u**3
Gstar = 16*u**6+k+2-6*u**2
triple_difference = s.expand(P(Tstar,Gstar) - (x+u)**3*(x-3*u))
assert s.simplify(triple_difference - (3*u**4+6*k*u*u-k*(k+2))) == 0
# Full H, including peripheral dark modes, has the claimed factorization.
for m in range(3,8):
    a,b,h=0,1,2
    leaves=list(range(3,m+1))
    H=s.zeros(m+1)
    H[a,a]=s.I*s.Rational(2,3); H[b,b]=-s.I*s.Rational(2,3)
    H[a,b]=H[b,a]=s.Rational(3,2)
    for j in [a,b]+leaves: H[h,j]=H[j,h]=1
    charpoly=H.charpoly()
    p_direct=s.expand(charpoly.as_expr().subs(charpoly.gen,x))
    expected=s.expand(x**(m-3)*P(s.Rational(3,2),s.Rational(4,9)).subs(k,m-2))
    assert s.simplify(p_direct-expected)==0,(m,p_direct,expected)
print('PASS: double-root elimination, two folds, exact triple-root factorization and full-matrix polynomials for m=3..7')
