import sys
import sympy as sp

print('python_version =', sys.version.split()[0])
print('sympy_version =', sp.__version__)

# Symbols for the Hopf--Langford-type system.
x, y, z = sp.symbols('x y z', real=True)
alpha, beta, gamma, mu = sp.symbols('alpha beta gamma mu', real=True, nonzero=True)
r = sp.symbols('r', positive=True)
a = alpha - mu
T = (2*gamma + 1)*mu - 2*gamma*alpha
b2 = sp.simplify(a*(mu - gamma*a)/gamma)

# Exact polar reduction, checked from x=r cos(theta), y=r sin(theta).
theta = sp.symbols('theta', real=True)
xx = r*sp.cos(theta)
yy = r*sp.sin(theta)
fx = xx*(mu-alpha) - beta*yy + xx*z
fy = beta*xx + yy*(mu-alpha) + yy*z
r_dot = sp.simplify((xx*fx + yy*fy)/r)
theta_dot = sp.simplify((xx*fy - yy*fx)/r**2)
print('r_dot_minus_expected =', sp.simplify(r_dot - r*(mu-alpha+z)))
print('theta_dot_minus_beta =', sp.simplify(theta_dot - beta))

# Off-axis equilibrium of the amplitude system.
zstar = a
z_rhs_at_star = sp.simplify(mu*zstar - gamma*(b2 + zstar**2))
print('z_rhs_at_star =', z_rhs_at_star)

# Quotient Jacobian trace and determinant at (r,z)=(b,a).
b = sp.symbols('b', positive=True)
J = sp.Matrix([[0, b], [-2*gamma*b, T]])
print('jacobian_trace_minus_T =', sp.simplify(sp.trace(J)-T))
print('jacobian_det_minus_2gamma_b2 =', sp.simplify(J.det()-2*gamma*b**2))
lam = sp.symbols('lam')
print('characteristic_polynomial =', sp.factor(J.charpoly(lam).as_expr()))

# Exact scalar equation after w=r**gamma.
w, wp = sp.symbols('w wp', positive=True)
wpp = T*wp + gamma**2*b**2*w - gamma**2*w**(1+2/gamma)
Vprime = -gamma**2*b**2*w + gamma**2*w**(1+2/gamma)
print('energy_derivative_minus_T_wp2 =', sp.simplify(wp*(wpp+Vprime)-T*wp**2))

# Curvature of the potential at the positive equilibrium w*=b**gamma.
wstar = b**gamma
Vpp = sp.diff(Vprime, w)
print('Vpp_at_wstar_minus_2gamma_b2 =', sp.simplify(Vpp.subs(w,wstar)-2*gamma*b**2))

# Expansion of the exact unit-modulus surface T=0 for the paper's perturbation.
eps = sp.symbols('eps')
a1, a2, g0, g1, mu2, nu0, nu1 = sp.symbols('a1 a2 g0 g1 mu2 nu0 nu1')
alpha_e = a1*eps + a2*eps**2
gamma_e = g0 + g1*eps
nu_e = nu0 + nu1*eps
mu_e = nu_e*eps + mu2*eps**2
T_e = sp.expand((2*gamma_e+1)*mu_e - 2*gamma_e*alpha_e)
c1 = sp.expand(T_e).coeff(eps,1)
c2 = sp.expand(T_e).coeff(eps,2)
nu0_exact = sp.simplify(2*g0*a1/(2*g0+1))
nu1_exact = sp.solve(sp.Eq(c2.subs(nu0,nu0_exact),0),nu1)[0]
print('exact_nu0 =', nu0_exact)
print('exact_nu1 =', sp.factor(nu1_exact))

# A concrete admissible family: alpha=eps, beta=1, gamma=1, mu=nu*eps.
# The source's Eq. (7) gives the displayed nonzero first correction.
pi = sp.pi
omega0 = sp.sqrt(2)/3
source_nu1 = sp.simplify((-4*omega0**2 + (-4*omega0**2 + 8*pi**2) - omega0**2)/27)
print('special_family_exact_nu1 =', sp.simplify(nu1_exact.subs({a1:1,a2:0,g0:1,g1:0,mu2:0})))
print('special_family_source_nu1 =', source_nu1)
print('special_family_source_nu1_numeric =', sp.N(source_nu1,15))

nucrit = sp.Rational(2,3)
hyp1 = sp.simplify((nucrit-1)*(1-2*nucrit))
hyp2 = sp.simplify(12 - 36*nucrit + 25*nucrit**2)
print('special_family_hypothesis_product =', hyp1)
print('special_family_hypothesis_discriminant =', hyp2)
