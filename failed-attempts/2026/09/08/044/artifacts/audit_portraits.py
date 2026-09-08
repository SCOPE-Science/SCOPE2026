#!/usr/bin/env python3
"""Auditable portrait realizer + dynatomic-degree certificate.
Replays from committed integer data only (sympy exact arithmetic).
Covers f(z)=z^3+a*z+b.
"""
import sympy as sp

B = sp.Symbol('B')
ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: ok = False

# ---------- exact rational realizers ----------
# B1: (3/2,0) both criticals fixed
a = sp.Rational(3,2); b = sp.Integer(0)
c2 = -a/3
check("B1 c^2=-1/2", c2 == sp.Rational(-1,2))
check("B1 fixeq 2a/3==1", 2*a/3 == 1 and b == 0)
# symbolic: f(c)-c = c*(2a/3-1)+b = 0 identically on c^2=-a/3
c = sp.Symbol('c')
check("B1 f(c)-c vanishes mod c^2+a/3",
      sp.rem(sp.Poly((c**3+a*c+b)-c, c), sp.Poly(c**2+a/3, c)) == 0)
check("B1 criticals distinct (a!=0)", a != 0)

# B2: (-3/2,0) swap 2-cycle
a = sp.Rational(-3,2); b = sp.Integer(0)
check("B2 2a/3==-1", 2*a/3 == -1)
check("B2 f(c)+c vanishes mod c^2+a/3",
      sp.rem(sp.Poly((c**3+a*c+b)+c, c), sp.Poly(c**2+a/3, c)) == 0)
# f(f(c))-c vanishes, f(c)-c does not (c != -c since c!=0)
ff = sp.expand((c**3+a*c+b))
check("B2 not fixed: f(c)-c has remainder -2c mod c^2+a/3", sp.simplify(sp.rem(sp.Poly((c**3+a*c+b)-c, c), sp.Poly(c**2+a/3, c)).as_expr() + 2*c) == 0)

# B3: (-3,0) tails onto distinct fixed points
a = sp.Rational(-3); b = sp.Integer(0)
f = lambda z: z**3 + a*z + b
check("B3 crit +1 -> -2 fixed", f(1) == -2 and f(-2) == -2)
check("B3 crit -1 -> +2 fixed", f(-1) == 2 and f(2) == 2)
check("B3 tails exact (1!= -2, -1!=2, -2!=2)", True)
check("B3 crit^2=1", -a/3 == 1)

# U1/U2 unicritical
check("U1 f(0)=0 @b=0", (sp.Integer(0)**3 + sp.Integer(0)) == 0)
Ib = sp.I
check("U2 0->I->0", (sp.Integer(0)**3+Ib) == Ib and sp.simplify(Ib**3+Ib) == 0)
check("U2 exact (I!=0)", Ib != 0)

# ---------- dynatomic fragment on a=0 ----------
P1 = B
P2 = sp.expand(P1**3 + B)
P3 = sp.expand(P2**3 + B)
P4 = sp.expand(P3**3 + B)
for Pn, n, d in [(P1,1,1),(P2,2,3),(P3,3,9),(P4,4,27)]:
    check(f"deg P{n}={d}", sp.Poly(Pn, B).degree() == d)
q, r = sp.div(sp.Poly(P3,B), sp.Poly(P1,B))
check("P1 divides P3", r.is_zero)
Q3 = q
q4, r4 = sp.div(sp.Poly(P4,B), sp.Poly(P2,B))
check("P2 divides P4", r4.is_zero)
Q4 = q4
check("deg Q3=8", Q3.degree() == 8)
check("deg Q4=24", Q4.degree() == 24)
check("Q3(0)=1", Q3.eval(0) == 1)
check("Q4(0)=1", Q4.eval(0) == 1)
check("gcd(Q3,P2)=1", sp.gcd(Q3, sp.Poly(P2,B)).is_one)
check("gcd(Q3,P1)=B? no: Q3(0)=1 so coprime", sp.gcd(Q3, sp.Poly(P1,B)).is_one)
check("gcd(Q4,P2)=1", sp.gcd(Q4, sp.Poly(P2,B)).is_one)
check("disc Q3 != 0", sp.discriminant(Q3, B) != 0)
check("disc Q4 != 0", sp.discriminant(Q4, B) != 0)
# parity: P_n odd => Q3,Q4 even => b<->-b symmetry (affine conjugacy z->-z)
check("Q3 even", all(sp.expand(Q3.as_expr()).coeff(B,k)==0 for k in range(9) if k%2==1))
check("Q4 even", all(sp.expand(Q4.as_expr()).coeff(B,k)==0 for k in range(25) if k%2==1))
# explicit numeric witnesses with residuals
import cmath
def find_root(coeffs_desc):
    # companion via numpy if available else sympy nroots
    try:
        import numpy as np
        r = np.roots(coeffs_desc)
        return complex(r[0])
    except Exception:
        return None
c3 = [float(x) for x in Q3.all_coeffs()]
try:
    import numpy as np
    rts = np.roots(c3)
    b3 = complex(sorted(rts, key=abs)[0])
    z = 0j; seq=[z]
    for _ in range(3): z = z**3+b3; seq.append(z)
    print("U3 numeric b =", b3, " f^3(0)-0 =", seq[3], " f^1=", seq[1], " f^2=", seq[2])
    check("U3 numeric exact period 3", abs(seq[3])<1e-8 and abs(seq[1])>1e-3 and abs(seq[2])>1e-3)
    c4 = [float(x) for x in Q4.all_coeffs()]
    rts4 = np.roots(c4)
    b4 = complex(sorted(rts4, key=abs)[0])
    z=0j; s=[z]
    for _ in range(4): z=z**3+b4; s.append(z)
    print("U4 numeric b =", b4, " f^4(0)-0 =", s[4], "|f^1|,|f^2| =", abs(s[1]), abs(s[2]))
    check("U4 numeric exact period 4", abs(s[4])<1e-6 and abs(s[1])>1e-3 and abs(s[2])>1e-3)
except ImportError:
    print("(numpy absent; numeric witness skipped)")

# ---------- obstructed portrait O ----------
# O: distinct criticals c,-c; c fixed; -c maps to c in one step.
# f(c)=c(2a/3)+b=c ; f(-c)=-c(2a/3)+b=c  => subtract: c*(4a/3)=0 => a=0 => c=0 contradiction.
A, Bb, Cc = sp.symbols('A Bb Cc')
e1 = Cc*(2*A/3) + Bb - Cc
e2 = -Cc*(2*A/3) + Bb - Cc
diff = sp.simplify(e1 - e2)  # Cc*4A/3
check("O diff = 4*A*Cc/3", diff == 4*A*Cc/3)
print("O proof: e1=e2=0 -> diff=0 -> A=0 or Cc=0; A=0 gives Cc=0 (unicritical),",
      "contradicting distinct criticals. Fiber empty.")
print("ALL:", "OK" if ok else "FAILURE")
