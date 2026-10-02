import sympy as sp

print(f"SymPy {sp.__version__}")

x, y, z, R, T = sp.symbols("x y z R T")
f = T - R + R*x**2
vx, vy, vz = y, z, -z - f*y - T*x


def L(q):
    return sp.expand(sp.diff(q, x)*vx + sp.diff(q, y)*vy + sp.diff(q, z)*vz)


H = (T - R)*x**2/2 + R*x**4/4
W = -y*z - T*x*y + T*x*z + T*H - T*x**2/2 - (T + 1)*y**2/2

checks = {
    "L(x^2/2)-xy": L(x**2/2) - x*y,
    "L(y^2/2)-yz": L(y**2/2) - y*z,
    "L(xy)-(y^2+xz)": L(x*y) - (y**2 + x*z),
    "L(xz+H)-(yz-xz-Tx^2)": L(x*z + H) - (y*z - x*z - T*x**2),
    "L(yz)-balance": L(y*z) - (z**2 - y*z - f*y**2 - T*x*y),
    "L(W)-defect": L(W) - (R*(x**2 - 1)*y**2 - (z + T*x)**2),
}

for name, expr in checks.items():
    residual = sp.factor(expr)
    print(f"{name}: {residual}")
    assert residual == 0

print("all symbolic residuals are zero")
