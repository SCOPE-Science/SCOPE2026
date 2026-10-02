"""Chanillo-normalization verification: P0^t(f)=0 for f=z^2 (exact).

Uses Chanillo-Chiu-Yang conventions (arXiv:1007.5020):
  Frame: E = Z(t)/sqrt(1-t^2), Eb = Zbar(t)/sqrt(1-t^2), s2=1-t^2.
  Kohn: BoxC = 2*dbar* dbar with BoxC f = -2 E(Eb f) + 2*omega-term;
        omega-term vanishes here because omega(Z(t))=0 (Takeuchi Lemma proof).
        So BoxC_num = -2*Zt(Zbt f), BoxbarC_num = -2*Zbt(Zt f), over s2.
  Torsion: A_C = 4 t i/(1-t^2) (Prop 2.5), f1 = E f = Zt(f)/sqrt(s2),
        (A f1)_1 = E(A f1) = A*Zt(Zt f)/s2.
  P0 = 1/4 (BoxC BoxbarC f - 4i (A f1)_1).
Exact polynomial identities in (z,w,zb,wb,t).
"""
import sympy as sp

z, w, zb, wb, t = sp.symbols('z w zb wb t')
s2 = 1 - t**2


def Z1(f):
    return sp.expand(wb * sp.diff(f, z) - zb * sp.diff(f, w))


def Zb(f):
    return sp.expand(w * sp.diff(f, zb) - z * sp.diff(f, wb))


Zt = lambda fx: sp.expand(Z1(fx) + t * Zb(fx))
Zbt = lambda fx: sp.expand(Zb(fx) + t * Z1(fx))

f = z**2
g = zb**2

ok = True
for name, fx in [('f=z^2', f), ('g=zb^2', g)]:
    Boxb_num = sp.expand(-2 * Zbt(Zt(fx)))   # s2 * BoxbarC fx
    # apply BoxC: BoxC(BoxbarC fx) = -2*Zt(Zbt(BoxbarC fx))/s2
    # numerator over s2^2:
    BoxBoxb_num = sp.expand(-2 * Zt(Zbt(Boxb_num)))
    A = 4 * t * sp.I / s2
    # Full Q-part: -4i (A f1)_1 = -4i*A*Zt(Zt f)/s2. Common denominator s2^2:
    # num_Q = -4i*(A*s2)*Zt(Zt f) = -4i*(4ti)*Zt(Zt f) = 16t*Zt(Zt f).
    Q_num = sp.expand(16 * t * Zt(Zt(fx)))  # over s2^2, same denom as BoxBoxb_num
    P0_num = sp.expand(BoxBoxb_num + Q_num)
    zero = (P0_num == 0)
    ok &= zero
    print(f"{name}: BoxbarC_num={Boxb_num}")
    print(f"{name}: BoxCBoxbarC_num={BoxBoxb_num}")
    print(f"{name}: Q_num={Q_num}")
    print(f"{name}: P0_num==0 ? {'PASS' if zero else 'FAIL'}")
    print()
u = f + g
print("u* P0^t == 0 by linearity:", "PASS" if ok else "FAIL")
print('ALL_CHANILLO_OK' if ok else 'CHANILLO_FAIL')
