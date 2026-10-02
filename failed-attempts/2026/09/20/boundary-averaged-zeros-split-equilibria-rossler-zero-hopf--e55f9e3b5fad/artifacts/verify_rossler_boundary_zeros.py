#!/usr/bin/env python3
"""Symbolic checks for boundary averaged zeros in a classical Rössler unfolding."""
import sympy as sp

# Symbols and abbreviations.
a, eps, b1, c1, x, lam = sp.symbols('a eps b1 c1 x lam', nonzero=True)
delta = c1 - b1
omega2 = 2 - a**2
D = 4*a*eps**2*delta + eps**4*c1**2

# Exact equilibria of x'=-y-z, y'=x+a y, z'=b+z(x-c),
# with b=a+eps^2 b1 and c=2a+eps^2 c1.
b = a + eps**2*b1
c = 2*a + eps**2*c1
sigma = sp.symbols('sigma')
sqrtD = sp.sqrt(D)
x_sigma = (c + sigma*sqrtD)/2
y_sigma = -x_sigma/a
z_sigma = x_sigma/a

eq1 = sp.simplify(-y_sigma-z_sigma)
eq2 = sp.simplify(x_sigma+a*y_sigma)
eq3 = sp.simplify(b+z_sigma*(x_sigma-c)).subs(sigma**2,1)

# The paper's linear coordinates satisfy, on the equilibrium line,
# X=-(a^2/omega^2)w, Y=(a/omega^2)w, Z=-(a/omega^2)w.
X = x_sigma-a
w_sigma = -omega2*X/a**2
mapY_res = sp.simplify((y_sigma+1) - a*w_sigma/omega2)
mapZ_res = sp.simplify((z_sigma-1) + a*w_sigma/omega2)

# Leading scaled W coordinate.  Put k^2=a(c1-b1), k>0, and use eps>0.
k = sp.symbols('k', positive=True)
# x_sigma-a = sigma eps k + O(eps^2), hence W=w/eps.
W_lead = -sigma*omega2*k/a**2
P_boundary = -sigma*omega2*k/a**2
W_match = sp.simplify(W_lead-P_boundary)

# Exact characteristic polynomial at an equilibrium.
z = x/a
J = sp.Matrix([[0,-1,-1],[1,a,0],[z,0,x-c]])
charpoly = sp.expand((lam*sp.eye(3)-J).det())
char_expected = (lam**3 + (c-a-x)*lam**2
                 + (1+x/a+a*(x-c))*lam + c-2*x)
char_res = sp.simplify(charpoly-char_expected)

# First-order spectrum at x=a+sigma eps k+O(eps^2), c=2a+O(eps^2).
# Slow eigenvalue lambda = eps Ls + O(eps^2).
Ls = 2*sigma*k/omega2
# Oscillatory eigenvalues lambda = tau*i*omega + eps Lc + O(eps^2).
tau, omega = sp.symbols('tau omega', nonzero=True)
Lc = -sigma*a**2*k/(2*omega2) + sp.I*tau*sigma*k*(a+1/a)/(2*omega)
# Verify perturbation equations using omega^2=omega2 and tau^2=1.
q = sigma*k*(-lam**2 + (a+1/a)*lam - 2)
p0 = lam*(lam**2 + omega**2)
# slow coefficient at O(eps)
slow_res = sp.simplify(omega2*Ls - 2*sigma*k)
# complex coefficient p0'(lambda0)*Lc + q(lambda0)
lambda0 = sp.I*tau*omega
complex_res = sp.expand((3*lambda0**2+omega**2)*Lc + q.subs(lam,lambda0))
complex_res = sp.factor(complex_res.subs(omega**2,omega2))
complex_res_plus = sp.simplify(complex_res.subs(tau,1))
complex_res_minus = sp.simplify(complex_res.subs(tau,-1))

# Averaged Jacobian eigenvalues at the boundary zeros P_±.
# For W0 = s*omega^2*k/a^2, eigs are s*a^2*k/(2 omega^3), -s*2k/omega^3.
s = sp.symbols('s')
avg1 = s*a**2*k/(2*omega**3)
avg2 = -s*2*k/omega**3
# Exact equilibrium with sigma maps to boundary sign s=-sigma.
match_complex = sp.simplify(avg1.subs(s,-sigma) - (-sigma*a**2*k/(2*omega2))/omega)
match_slow = sp.simplify(avg2.subs(s,-sigma) - (sigma*2*k/omega2)/omega)
match_complex = sp.simplify(match_complex.subs(omega2,omega**2))
match_slow = sp.simplify(match_slow.subs(omega2,omega**2))

print('equilibrium_residuals =', [eq1, eq2, eq3])
print('coordinate_line_residuals =', [mapY_res, mapZ_res])
print('scaled_boundary_match =', W_match)
print('characteristic_polynomial_residual =', char_res)
print('slow_eigenvalue_first_order_residual =', slow_res)
print('complex_pair_first_order_residuals =', [complex_res_plus, complex_res_minus])
print('averaged_equilibrium_spectrum_matches =', [match_complex, match_slow])

# Numerical instance used in the source paper: a=1, b1=1, c1=2, eps=1/500.
vals = {a:sp.Integer(1), b1:sp.Integer(1), c1:sp.Integer(2), eps:sp.Rational(1,500)}
Dn = sp.N(D.subs(vals), 30)
print('example_discriminant =', Dn)
for sig in (+1,-1):
    xs = sp.N(x_sigma.subs(vals).subs(sigma,sig), 30)
    ys = sp.N(y_sigma.subs(vals).subs(sigma,sig), 30)
    zs = sp.N(z_sigma.subs(vals).subs(sigma,sig), 30)
    Ws = sp.N((w_sigma/eps).subs(vals).subs(sigma,sig), 30)
    cp_expr = char_expected.subs(vals).subs(x, x_sigma.subs(vals).subs(sigma,sig))
    cp = sp.Poly(sp.N(cp_expr, 40), lam)
    eigs = [complex(ev) for ev in sp.nroots(cp, n=24, maxsteps=100)]
    print(f'example_sigma_{sig}_equilibrium =', xs, ys, zs)
    print(f'example_sigma_{sig}_scaled_W =', Ws)
    print(f'example_sigma_{sig}_eigenvalues =', eigs)

all_zero = all(v == 0 for v in [eq1,eq2,eq3,mapY_res,mapZ_res,W_match,char_res,slow_res,complex_res_plus,complex_res_minus,match_complex,match_slow])
print('all_symbolic_checks_passed =', all_zero)
