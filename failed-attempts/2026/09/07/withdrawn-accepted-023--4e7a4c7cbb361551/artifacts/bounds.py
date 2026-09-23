"""Recompute absolute (Gerzon), relative (trace), and degree-4 Delsarte LP bounds
for equiangular lines with alpha=1/3 in d=6,7,8. Stdlib + numpy/sympy only.
"""
from fractions import Fraction
import sympy as sp
from sympy import gegenbauer, Rational

ALPHA = Fraction(1,3)
A2 = ALPHA*ALPHA  # 1/9

def absolute(d): return d*(d+1)//2
def relative(d):
    # d*(1-a2)/(1-d*a2) if denom>0 else inf
    num = Fraction(d)*(1-A2)
    den = 1-Fraction(d)*A2
    if den <= 0: return None
    return num/den

print("=== Absolute (Gerzon) and relative (trace) bounds, alpha=1/3 ===")
for d in [6,7,8]:
    ab = absolute(d)
    re = relative(d)
    print(f"d={d}: absolute={ab}, relative={re} = {float(re):.4f}, combined_min={min(ab, int(re)) if re==int(re) else min(ab, float(re))}")

# Exact LP polynomials:
# d=6: f(t)=18 t^2-2 = 1+15*P2, P2=(6t^2-1)/5
# d=7: f(t)=(63t^2-7)/2 = 1+27*P2, P2=(7t^2-1)/6
# d=8: f(t)=(3240t^4-1620t^2+140)/59 = 1+(1701/59)*P4, P4=(40t^4-20t^2+1)/21
t=sp.symbols('t')
def check_poly(d, fexpr, expansion, alpha=sp.Rational(1,3)):
    f1 = sp.expand(fexpr.subs(t,1))
    fa = sp.expand(fexpr.subs(t,alpha))
    fma = sp.expand(fexpr.subs(t,-alpha))
    print(f"d={d}: f(1)={f1} ~{float(f1):.6f}, f(1/3)={fa}, f(-1/3)={fma}")
    print(f"  expansion: {expansion}")
    # verify Gegenbauer formulas
    lam = sp.Rational(d-2,2)
    for k, coeff in expansion.items():
        if k==0: continue
        C=gegenbauer(k, lam, t); C1=C.subs(t,1); P=sp.simplify(C/C1)
        print(f"   P{k}={sp.expand(P)}")
    # verify f == sum coeff*P
    s=0
    for k, coeff in expansion.items():
        if k==0:
            s+=coeff
        else:
            C=gegenbauer(k, lam, t); C1=C.subs(t,1); P=C/C1
            s+=sp.Rational(coeff)*P if isinstance(coeff,int) else coeff*P
    diff=sp.expand(s-fexpr)
    print(f"  expansion check diff={diff} (must be 0)")
    assert diff==0
    assert fa<=0 and fma<=0
    for k,c in expansion.items():
        if k>=1: assert c>=0, f"c{k}={c} negative!"
    print(f"  => Delsarte bound n <= f(1)/f0 = {f1} => n <= {int(sp.floor(f1))} (integer)")

print()
print("=== Delsarte LP certificates ===")
# d=6
f6=18*t**2-2
check_poly(6, f6, {0:1, 2:sp.Rational(15)})
print()
# d=7
f7=(63*t**2-7)/2
check_poly(7, f7, {0:1, 2:sp.Rational(27)})
print()
# d=8
f8=(3240*t**4-1620*t**2+140)/59
check_poly(8, f8, {0:1, 4:sp.Rational(1701,59)})
print()
print("=== Final tightened table ===")
print("d=6: lower 16 (Clebsch), upper min(21,16)=16 => N=16 exact")
print("d=7: lower 28 (T8), upper min(28,28)=28 => N=28 exact")
print("d=8: lower 28 (T8 embedded), upper min(36,64,1760/59=29.83)=29 => N in {28,29}")
