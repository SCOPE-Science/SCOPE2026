import sympy as sp

theta = sp.symbols('theta', positive=True)
rho = 1 / (2 - theta)
R = sp.Rational(1, 2) + 6 * theta

C_raw = sp.factor(R + theta - 4 * theta / (1 - rho))
C_long = sp.factor((1 - rho) - 4 * theta * rho / (1 - rho))
E0 = sp.factor(R + 2 * theta)
L1 = sp.factor((1 - rho) + 5 * theta)
margin = sp.factor(E0 - L1)

print('rho =', rho)
print('raw_root_exponent R =', R)
print('raw_path_monotonicity_coefficient =', C_raw)
print('long_path_monotonicity_coefficient =', C_long)
print('raw_path_maximum E0 =', E0)
print('long_path_maximum L1 =', L1)
print('E0-L1 =', margin)

assert sp.simplify(E0 - (sp.Rational(1, 2) + 8 * theta)) == 0
assert sp.simplify(C_raw - (6*theta**2 + 3*theta - 1)/(2*(theta-1))) == 0
assert sp.simplify(C_long - (5*theta**2 - 10*theta + 1)/((theta-2)*(theta-1))) == 0
assert sp.simplify(margin - theta*(6*theta-13)/(2*(theta-2))) == 0

for q in [sp.Rational(1,24), sp.Rational(1,20), sp.Rational(1,16)]:
    vals = [sp.simplify(x.subs(theta,q)) for x in [C_raw,C_long,E0,L1,margin]]
    print(f'theta={q}: C_raw={vals[0]}, C_long={vals[1]}, E0={vals[2]}, L1={vals[3]}, margin={vals[4]}')
    assert vals[0] > 0
    assert vals[1] > 0
    assert vals[4] > 0

print('At theta=1/24, E0 =', sp.simplify(E0.subs(theta, sp.Rational(1,24))))
