import sympy as sp

th1, th2, th3, rho = sp.symbols('th1 th2 th3 rho', real=True)
a, R = sp.symbols('a R', positive=True, real=True)
w12, w13, w21, w23, w31, w32 = sp.symbols(
    'w12 w13 w21 w23 w31 w32', real=True
)
I = sp.I

f2 = (
    w12*w21*(sp.sin(2*rho) + sp.sin(2*(th2-th1)))
    + w12*w23*(sp.sin(th3-th1+2*rho) + sp.sin(2*th2-th3-th1))
    + w13*w31*(sp.sin(2*rho) + sp.sin(2*(th3-th1)))
    + w13*w32*(sp.sin(th2-th1+2*rho) + sp.sin(2*th3-th2-th1))
    - w12**2*sp.sin(2*(th2-th1)+2*rho)
    - 2*w12*w13*sp.sin(th2+th3-2*th1+2*rho)
    - w13**2*sp.sin(2*(th3-th1)+2*rho)
) / (4*a)

# Each tuple is (complex coefficient before 1/(4 a R^2), monomial phase p+q-r-j).
terms = [
    (-sp.exp(2*I*rho)*w12*w21, 0),
    (-sp.exp(2*I*rho)*w13*w31, 0),
    (-sp.exp(2*I*rho)*w12*w23, th3-th1),
    (-sp.exp(2*I*rho)*w13*w32, th2-th1),
    (-w12*w23, 2*th2-th3-th1),
    (-w13*w32, 2*th3-th2-th1),
    (2*sp.exp(2*I*rho)*w12*w13, th2+th3-2*th1),
    (sp.exp(2*I*rho)*w12**2-w12*w21, 2*(th2-th1)),
    (sp.exp(2*I*rho)*w13**2-w13*w31, 2*(th3-th1)),
]

# On z_j = R exp(i theta_j), straight-isochrone phase projection is
# R^{-1} Im(exp(-i theta_j) H_j), so every cubic monomial contributes R^2 Im(...).
controller_projection = sum(
    sp.expand_complex(coeff * sp.exp(I*phase)).as_real_imag()[1]
    for coeff, phase in terms
) / (4*a)

residual = sp.trigsimp(sp.expand_trig(controller_projection + f2))
assert residual == 0

# Exhaust the symmetric cubic monomials z_p z_q conjugate(z_r) for oscillator j=1.
classes = {}
for p in range(3):
    for q in range(p, 3):
        for r in range(3):
            exponent = [0, 0, 0]
            exponent[p] += 1
            exponent[q] += 1
            exponent[r] -= 1
            exponent[0] -= 1
            classes.setdefault(tuple(exponent), []).append((p+1, q+1, r+1))

assert (2, 2, 1) in classes[(-2, 2, 0)]
assert (3, 3, 1) in classes[(-2, 0, 2)]

print('phase_cancellation_residual =', residual)
print('z2^2*conj(z1) phase_vector =', (-2, 2, 0))
print('z3^2*conj(z1) phase_vector =', (-2, 0, 2))
print('distinct_cubic_phase_vectors =', len(classes))
print('all_checks_passed = True')
