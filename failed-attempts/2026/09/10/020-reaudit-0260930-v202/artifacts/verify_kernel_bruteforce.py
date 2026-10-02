"""Independent brute-force route: P(t)u* = 0 pointwise as polynomials.

No eigenvalue table used. Operators built directly from vector fields:
  Z(t) = Z1 + t*Zbar1,  Zbar(t) = Zbar1 + t*Z1   (real t)
  (1-t^2) Box(t)     = -Z(t) Zbar(t)   [Takeuchi Lemma proof: omega(Z)=0]
  (1-t^2) Boxbar(t)  = -Zbar(t) Z(t)
  (1-t^2)^2 Q(t)     = +4t Zbar(t)^2   [via A^{bar bar}=conj(A^{11})]
  (1-t^2)^2 P(t)     = Boxbar-num Box-num + Q-num composition.
All steps are exact polynomial identities in (z,w,zb,wb,t).
"""
import sympy as sp

z, w, zb, wb, t = sp.symbols('z w zb wb t')
s = sp.symbols('s')  # formal conj(t) for complex-t robustness


def Z1(f):
    return sp.expand(wb * sp.diff(f, z) - zb * sp.diff(f, w))


def Zb(f):
    return sp.expand(w * sp.diff(f, zb) - z * sp.diff(f, wb))


f = z**2
g = zb**2
u = f + g

# real-t route
Zt = lambda fx: sp.expand(Z1(fx) + t * Zb(fx))
Zbt = lambda fx: sp.expand(Zb(fx) + t * Z1(fx))
Boxn = lambda fx: sp.expand(-Zt(Zbt(fx)))
Bbn = lambda fx: sp.expand(-Zbt(Zt(fx)))
Qn = lambda fx: sp.expand(4 * t * Zbt(Zbt(fx)))

print("== real-t route ==")
ok = True
for name, fx in [('f=z^2', f), ('g=zb^2', g), ('u*', u)]:
    b = Boxn(fx)
    bb = Bbn(b)
    q = Qn(fx)
    p = sp.expand(bb + q)
    zero = (p == 0)
    ok &= zero
    print(f"{name}: Pnum==0 ? {'PASS' if zero else 'FAIL: ' + str(p)}")
# nonzero witness check: u*(1,0)=2
print('u*(1,0) =', complex(u.subs({z: 1, w: 0, zb: 1, wb: 0})), '(nonzero => fixed trial fn nontrivial)')

# formal complex-t route: Z(t)=Z1+t Zbar, Zbar_s=Zbar+s Z1
Ztc = lambda fx: sp.expand(Z1(fx) + t * Zb(fx))
Zbc = lambda fx: sp.expand(Zb(fx) + s * Z1(fx))
Qnc = lambda fx: sp.expand(4 * t * Zbc(Zbc(fx)))
print("== formal complex-t route (s=conj t) ==")
for name, fx in [('f', f), ('g', g), ('u*', u)]:
    b = sp.expand(-Ztc(Zbc(fx)))
    bb = sp.expand(-Zbc(Ztc(b)))
    q = Qnc(fx)
    p = sp.expand(bb + q)
    zero = (p == 0)
    ok &= zero
    print(f"{name}: Pnum==0 ? {'PASS' if zero else 'FAIL: ' + str(p)}")

print('ALL_VERIFY_OK' if ok else 'VERIFY_FAIL')
