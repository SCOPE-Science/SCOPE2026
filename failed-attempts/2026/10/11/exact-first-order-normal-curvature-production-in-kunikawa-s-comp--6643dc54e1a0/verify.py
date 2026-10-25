import sympy as sp

theta = sp.symbols("theta", real=True)
kp = sp.symbols("kp", real=True)
x = sp.symbols("x", real=True)
r = sp.sqrt(13)

rho = 2 + sp.cos(theta)
rate = -4*kp*sp.sin(theta)/rho**4

# Source witness theta=pi/2.
assert sp.simplify(rate.subs(theta, sp.pi/2) + kp/sp.Integer(4)) == 0

# Maximize h on (0,pi).
h = sp.sin(theta)/rho**4
dh = sp.factor(sp.diff(h, theta))
target_dh = (4 + 2*sp.cos(theta) - 3*sp.cos(theta)**2)/rho**5
assert sp.simplify(dh-target_dh) == 0

roots = sp.solve(3*x**2-2*x-4, x)
assert roots == [(sp.Integer(1)-r)/3, (sp.Integer(1)+r)/3]
xstar = (1-r)/3
assert -1 < float(sp.N(xstar)) < 1
assert float(sp.N((1+r)/3)) > 1

sinstar = sp.sqrt(sp.simplify(1-xstar**2))
hmax = sp.simplify(sinstar/(2+xstar)**4)
target_hmax = 27*sp.sqrt(2*r-5)/(7-r)**4
assert sp.simplify(hmax-target_hmax) == 0
max_rate_coeff = sp.simplify(4*hmax)
target_rate_coeff = 108*sp.sqrt(2*r-5)/(7-r)**4
assert sp.simplify(max_rate_coeff-target_rate_coeff) == 0

# Exact profile integral through the J_n recurrence.
a = sp.symbols("a", positive=True)
J = 2*sp.pi/sp.sqrt(a**2-1)
vals = {}
for n in range(1, 8):
    vals[n] = sp.simplify(J.subs(a, 2))
    J = sp.simplify(-sp.diff(J, a)/n)

assert vals[5] == 227*sp.sqrt(3)*sp.pi/972
assert vals[6] == 101*sp.sqrt(3)*sp.pi/486
assert vals[7] == 1103*sp.sqrt(3)*sp.pi/5832

I = sp.simplify(-vals[5] + 4*vals[6] - 3*vals[7])
target_I = 59*sp.sqrt(3)*sp.pi/1944
assert sp.simplify(I-target_I) == 0

energy_coeff = sp.simplify(16*I)
target_energy_coeff = 118*sp.sqrt(3)*sp.pi/243
assert sp.simplify(energy_coeff-target_energy_coeff) == 0

energy_second = sp.simplify(2*energy_coeff)
assert sp.simplify(energy_second - 236*sp.sqrt(3)*sp.pi/243) == 0

ratio_to_source_witness = sp.N(max_rate_coeff/(sp.Rational(1,4)), 18)

print("VERIFY_OK")
print("pointwise_rate=true")
print("unique_profile_cosine=(1-sqrt(13))/3")
print("energy_coefficient=118*sqrt(3)*pi/243")
print("ratio_to_source_witness=" + str(ratio_to_source_witness))
