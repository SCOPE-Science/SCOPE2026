import sympy as sp

th, z = sp.symbols("th z", positive=True)
x = sp.symbols("x", integer=True, nonnegative=True)

a = th*(th+2)/(1+th)**2
b = 1/(1+th)**2

assert sp.simplify(a+b-1) == 0

# XLindley density coefficient identity after removing exp(-th*t).
t = sp.symbols("t", positive=True)
lhs_density = a*th + b*th**2*t
rhs_density = th**2*(th+2+t)/(1+th)**2
assert sp.simplify(lhs_density-rhs_density) == 0

def nb_pmf(k):
    return sp.binomial(x+k-1, x)*(th/(1+th))**k*(1/(1+th))**x

mix_pmf = sp.simplify(a**2*nb_pmf(2) + 2*a*b*nb_pmf(3) + b**2*nb_pmf(4))

target_pmf = (
    th**4*(x+1) /
    (6*(1+th)**(x+8)) *
    (
        x**2
        + x*(17 + 6*th*(th+3))
        + 6*(3 + th*(th+3))**2
    )
)
assert sp.simplify(sp.factor(mix_pmf-target_pmf)) == 0

D = 1 + th - z
g_pxl = sp.simplify(a*th/D + b*(th/D)**2)
g_pxl_target = (
    th**2*(th**2+3*th+3-(th+2)*z) /
    ((1+th)**2*D**2)
)
assert sp.simplify(g_pxl-g_pxl_target) == 0

g_pts = sp.expand(g_pxl_target**2)
g_source = (
    th**4*(th**2+3*th+3-(th+2)*z)**2 /
    ((1+th)**4*D**4)
)
assert sp.simplify(g_pts-g_source) == 0

# Numerical PMF cross-checks.
for theta_value in (sp.Rational(1,2), sp.Integer(1), sp.Rational(5,2)):
    for x_value in (0,1,2,5,10):
        v1 = sp.N(mix_pmf.subs({th:theta_value, x:x_value}), 40)
        v2 = sp.N(target_pmf.subs({th:theta_value, x:x_value}), 40)
        assert abs(v1-v2) < sp.Float("1e-35")

print("VERIFY_OK")
