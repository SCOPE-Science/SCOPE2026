"""Verification: critical loci of the cubic-del-Pezzo seed potential and three
Lagrangian-mutation descendants (Pascaleff-Tonkonog wall-crossing maps).

Seed (Table 1):  W0 = (1+x+y)^3/(x*y) - 6   (Bl_6 CP^2 = cubic surface).
Cluster map (Def 4.1): mu_v(x,y) = (x*(1+t)^(-v1), y*(1+t)^(-v2)),
  t = x^v2 * y^(-v1).  Mutated potential W' = W o mu_v.
Checks per potential W:
  * factored form of W+6 (expect S^3 / M),
  * factored gradient numerators,
  * Morse check at the tracked value-21 point,
  * degeneracy sample on the S=0 curve (grad 0, Hess det 0, value -6).
"""
import sympy as sp

x, y = sp.symbols('x y')
W0 = (1 + x + y) ** 3 / (x * y) - 6


def muW(W, v):
    v1, v2 = v
    t = 1 + x ** v2 * y ** (-v1)
    X = x * t ** (-v1)
    Y = y * t ** (-v2)
    return sp.together(W.subs({x: X, y: Y}))


def report(W, name):
    print("=" * 70)
    print(name)
    n, d = sp.together(W + 6).as_numer_denom()
    print("  W+6 num factored:", sp.factor(n))
    print("  W+6 den factored:", sp.factor(d))
    nx, dx = sp.together(sp.diff(W, x)).as_numer_denom()
    ny, dy = sp.together(sp.diff(W, y)).as_numer_denom()
    print("  dW/dx num:", sp.factor(nx))
    print("  dW/dy num:", sp.factor(ny))


def morse_check(W, name, pt):
    H = sp.hessian(W, (x, y)).subs(pt)
    print("  %s pt=%s value=%s Hdet=%s" % (
        name, pt, sp.simplify(W.subs(pt)), sp.simplify(H.det())))


def degeneracy_sample(W, name, x0):
    n, d = sp.together(W + 6).as_numer_denom()
    S = None
    for f, e in sp.factor_list(n)[1]:
        if e >= 2:
            S = f
            break
    print("  %s cubed factor S=%s (power in num)" % (name, S))
    for s in sp.solve(S.subs(x, x0), y):
        pt = {x: x0, y: s}
        if sp.simplify(d.subs(pt)) == 0:
            print("    y=%s pole, skip" % sp.simplify(s))
            continue
        g = [sp.simplify(sp.diff(W, x).subs(pt)),
             sp.simplify(sp.diff(W, y).subs(pt))]
        Hdet = sp.simplify(sp.hessian(W, (x, y)).subs(pt).det())
        print("    y=%s value=%s grad=%s Hdet=%s" % (
            sp.simplify(s), sp.simplify(W.subs(pt)), g, Hdet))


W1 = muW(W0, (1, 0))
W2 = muW(W1, (0, 1))
W3 = muW(W2, (0, -1))  # valid LG-seed direction of W2's seed; recovery test

for W, nm in [(W0, "W0 seed"), (W1, "W1=mu_(1,0)W0"),
              (W2, "W2=mu_(0,1)W1"), (W3, "W3=mu_(0,-1)W2")]:
    report(W, nm)

print("-" * 70 + "\nMorse (value-21) points:")
morse_check(W0, "W0", {x: 1, y: 1})
morse_check(W1, "W1", {x: 2, y: 1})
morse_check(W2, "W2", {x: 2, y: 3})
morse_check(W3, "W3", {x: 2, y: 2})

print("-" * 70 + "\nDegenerate (value -6) curve samples:")
degeneracy_sample(W0, "W0", 1)
degeneracy_sample(W1, "W1", 1)   # S1(1,y)=0 has roots; M1 nonzero there
degeneracy_sample(W2, "W2", 1)
degeneracy_sample(W3, "W3", 2)

print("-" * 70 + "\nPearl-dichotomy samples for W0:")
for pt in [{x: 1, y: 1}, {x: -1, y: -1}]:
    g = [sp.simplify(sp.diff(W0, x).subs(pt)),
         sp.simplify(sp.diff(W0, y).subs(pt))]
    print("  pt=%s value=%s grad=%s" % (pt, sp.simplify(W0.subs(pt)), g))
print(" bullets: (1,1) critical -> HF!=0; (-1,-1) noncritical -> HF=0")
