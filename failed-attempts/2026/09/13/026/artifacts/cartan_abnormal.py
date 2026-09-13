"""Symbolic verification: Cartan group law, left-invariant fields, abnormal containment."""
import sympy as sp

# Lie algebra coords x=(x1..x5), basis e1..e5, brackets [e1,e2]=e3,[e1,e3]=e4,[e2,e3]=e5
def bracket(a, b):
    # a,b length-5 vectors (sympy); return [a,b]
    a = list(a); b = list(b)
    c = [sp.Integer(0)]*5
    # [e1,e2]=e3
    c[2] += a[0]*b[1] - a[1]*b[0]
    # [e1,e3]=e4
    c[3] += a[0]*b[2] - a[2]*b[0]
    # [e2,e3]=e5
    c[4] += a[1]*b[2] - a[2]*b[1]
    return c

def add(*vs):
    return [sum(v[i] for v in vs) for i in range(5)]

def scale(s, v):
    return [s*v[i] for i in range(5)]

def bch(x, y):
    xy = bracket(x, y)
    x_xy = bracket(x, xy)
    y_yx = bracket(y, scale(-1, xy))  # [y,[y,x]]
    return add(x, y, scale(sp.Rational(1,2), xy),
               scale(sp.Rational(1,12), x_xy), scale(sp.Rational(1,12), y_yx))

xs = sp.symbols('x1:6')
ys = sp.symbols('y1:6')
x = list(xs); y = list(ys)
z = bch(x, y)
print("=== Group law z = x*y (first-kind coords) ===")
for i, zi in enumerate(z):
    print(f"z{i+1} =", sp.expand(zi))

# Left-invariant fields: Xi(x) = d/ds|0 x*(s ei)
s = sp.symbols('s')
print("\n=== Left-invariant frame ===")
X = []
for k in range(5):
    ek = [sp.Integer(0)]*5; ek[k] = s
    prod = bch(x, ek)
    col = [sp.diff(prod[i], s).subs(s, 0) for i in range(5)]
    X.append(col)
    print(f"X{k+1} =", [sp.expand(c) for c in col])

x1,x2,x3,x4,x5 = xs
X1, X2 = X[0], X[1]
print("\nX1(x) =", [sp.expand(c) for c in X1])
print("X2(x) =", [sp.expand(c) for c in X2])
assert X1[0] == 1 and X1[1] == 0 and X2[0] == 0 and X2[1] == 1

u1, u2 = sp.symbols('u1 u2')
xdot = [sp.expand(u1*X1[i] + u2*X2[i]) for i in range(5)]
print("\n=== Horizontal ODEs xdot = u1 X1 + u2 X2 ===")
for i, d in enumerate(xdot):
    print(f"x{i+1}' =", d)

# Plane P = {x3=x4=x5=0}: check tangency: x3',x4',x5' vanish on P for all u
print("\n=== Tangency check on P ===")
subsP = {x3: 0, x4: 0, x5: 0}
for i in [2,3,4]:
    print(f"x{i+1}'|_P =", sp.expand(xdot[i].subs(subsP)))

# Collinear controls: u = alpha*(-b,a); verify x1*u2-x2*u1 structure in x3'
print("\n=== x3' numerator ===")
print("x3' =", xdot[2])
a, b, al = sp.symbols('a b alpha')
# substitute u1=-alpha*b, u2=alpha*a
print("x3' with u=alpha*(-b,a):", sp.expand(xdot[2].subs({u1: -al*b, u2: al*a})))
print("x4' with u=alpha*(-b,a):", sp.expand(xdot[3].subs({u1: -al*b, u2: al*a})))
print("x5' with u=alpha*(-b,a):", sp.expand(xdot[4].subs({u1: -al*b, u2: al*a})))
print("\nAll checks done.")
