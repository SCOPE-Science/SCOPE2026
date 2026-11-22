"""Supplementary exact and numerical checks for one-observation Wiener integral design.

Run: python verify.py (requires SymPy).
Analytical uniqueness and global comparisons are proved in RESULT.md.
"""
from math import sqrt
import sympy as S

x, u, eta = S.symbols('x u eta', real=True)
C = x**2 * (x**2 - 4*x + 6) / 24
D = x * (x**2 - 3*x + 3) / 6
V = x**3 / 3
F = C**2 / (V + eta)
G = D**2 / (x + eta)

assert S.simplify(S.integrate((1-u)**2 * (x-u)/2, (u, 0, x)) - C) == 0
assert S.simplify(S.integrate((1-u)**2/2, (u, 0, x)) - D) == 0
assert S.integrate((1-u)**4/4, (u, 0, 1)) == S.Rational(1, 20)

q = 5*x**2-12*x+6
p = x**2-3*x+3
factor_F = x**3*(x**2-4*x+6)*(24*eta*p+x**3*q) / (192*(3*eta+x**3)**2)
assert S.cancel(S.diff(F,x)-factor_F) == 0

Lambda = x*(-5*x**2+9*x-3)/(6*(1-x)**2)
assert S.cancel(S.diff(Lambda,x)-(S.Rational(1,3)/(1-x)**3-S.Rational(5,6))) == 0
assert S.cancel((x+eta)*S.diff(G,x) - (2*D*S.diff(D,x)-G)) == 0

value_critical = S.Rational(1,24)
ylo, yhi = S.Rational(47,100), S.Rational(12,25)
assert Lambda.subs(x,ylo) < value_critical < Lambda.subs(x,yhi)
upper = D.subs(x,yhi)**2/(ylo+value_critical)
assert upper < S.Rational(1,24)

P6 = 80*x**6-416*x**5+880*x**4-896*x**3+432*x**2-96*x+9
G_st = S.factor((G.subs(eta,Lambda)))
F1_st = 1/(64*(S.Rational(1,3)+Lambda))
assert S.cancel((G_st-F1_st) - ((x-1)**2*P6)/(96*(5*x**3-11*x**2+7*x-2))) == 0

root = float(S.nsolve(P6, S.Rational(52,100), prec=45))
noise_cross = float(Lambda.subs(x, root))
assert 0.5212 < root < 0.5213
assert 0.1260 < noise_cross < 0.1262

# Independent numerical stress checks; not a substitute for global proof.
for noise in [0.0, 0.01, 1/24, 0.1, noise_cross, 0.2, 1.0, 100.0]:
    # Bisection on the strictly monotone function Lambda over (y0,1).
    left=(9-sqrt(21))/10
    right=1.0
    for _ in range(110):
        mid=(left+right)/2
        value=float(Lambda.subs(x,mid))
        if value < noise:
            left=mid
        else:
            right=mid
    ystar=(left+right)/2
    val_b=float(G.subs({x:ystar,eta:noise}))
    x0=(6-sqrt(6))/5
    if noise >= 1/24:
        xstar=1.0
    else:
        left=x0
        right=1.0
        for _ in range(110):
            mid=(left+right)/2
            v=-mid**3*(5*mid**2-12*mid+6)/(24*(mid*mid-3*mid+3))
            if v < noise:
                left=mid
            else:
                right=mid
        xstar=(left+right)/2
    val_x=float(F.subs({x:xstar,eta:noise}))
    funx=lambda z: (z*z*(z*z-4*z+6)/24)**2/(z**3/3+noise)
    funb=lambda z: (z*(z*z-3*z+3)/6)**2/(z+noise)
    for i in range(2001):
        p=i/2000
        if p==0 and noise==0: continue
        assert funx(p) < val_x+2e-12
        assert funb(p) < val_b+2e-12
    if noise<noise_cross-1e-8: assert val_x>val_b
    if noise>noise_cross+1e-8: assert val_b>val_x

print('PASS: exact covariance, curvature, endpoint and algebraic crossing identities;')
print('      rational crossing bracket and 32,014 finite design comparisons.')
print(f'Crossing site {root:.12f}; crossing noise variance {noise_cross:.12f}')
