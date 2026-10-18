import math
import sympy as sp

theta, z = sp.symbols("theta z", positive=True)
g_pxl = (
    theta**2 *
    (theta**2 + 3*theta + 3 - (theta + 2)*z) /
    ((1 + theta)**2 * (1 + theta - z)**2)
)
g_pts = (
    theta**4 *
    (theta**2 + 3*theta + 3 - (theta + 2)*z)**2 /
    ((1 + theta)**4 * (1 + theta - z)**4)
)
assert sp.simplify(g_pxl**2 - g_pts) == 0

DI = (
    theta**5 + 5*theta**4 + 11*theta**3 + 14*theta**2 + 10*theta + 2
) / (
    theta*(1+theta)**2*(theta**2 + 2*theta + 2)
)
gap = sp.factor(DI - 1)
target_gap = (
    theta**4 + 4*theta**3 + 8*theta**2 + 8*theta + 2
) / (
    theta*(1+theta)**2*(theta**2 + 2*theta + 2)
)
assert sp.simplify(gap - target_gap) == 0

mean = 2*(theta**2 + 2*theta + 2)/(theta*(1+theta)**2)
assert sp.limit(theta*(DI-1), theta, sp.oo) == 1
assert sp.limit(theta*mean, theta, sp.oo) == 2

def pxl_pmf(x, th):
    return th**2 * (x + th**2 + 3*th + 3) / (1+th)**(x+4)

def pts_pmf(x, th):
    return (
        th**4 * (x+1) /
        (6*(1+th)**(x+8)) *
        (
            x*x
            + x*(17 + 6*th*(th+3))
            + 6*(3 + th*(th+3))**2
        )
    )

for th in (0.15, 0.7, 1.0, 2.5, 8.0):
    for x in range(0, 31):
        conv = sum(pxl_pmf(k, th)*pxl_pmf(x-k, th) for k in range(x+1))
        ref = pts_pmf(x, th)
        assert abs(conv-ref) <= 2e-12*max(1.0, abs(ref))
    di = float(DI.subs(theta, th))
    assert di > 1.0

# A source-table boundary illustration.
th = 100.0
mean100 = float(mean.subs(theta, th))
di100 = float(DI.subs(theta, th))
assert abs(mean100 - 0.0200) < 6e-5
assert abs(di100 - 1.0100) < 6e-5

print("VERIFY_OK")
print("DI_minus_1_factor", sp.factor(DI-1))
print("mean_theta_100", format(mean100, ".12f"))
print("DI_theta_100", format(di100, ".12f"))
