from fractions import Fraction


def admissible_interval(m, n):
    a = 2**m - 1
    b = 2**n - 1
    return Fraction(-1, a*b), Fraction(1, max(a, b))


def density(m, n, theta, u, v):
    return 1 + theta * (1 - 2**m * u) * (1 - 2**n * v)


def second_moment_factor(m):
    # If U is the product of m independent Uniform(0,1) variables,
    # E[(1-2^m U)^2] = (4/3)^m - 1.
    return Fraction(4, 3)**m - 1


x = y = Fraction(7, 8)
z = Fraction(1, 8)
g = density(2, 1, Fraction(1, 1), x*y, z)
assert g == Fraction(-35, 64)
assert admissible_interval(2, 1) == (Fraction(-1, 3), Fraction(1, 3))
assert admissible_interval(2, 2) == (Fraction(-1, 9), Fraction(1, 3))

# For H(theta) = -int (1+theta h) log(1+theta h), H''(0) = -E[h^2].
Hpp_outer = -second_moment_factor(1) * second_moment_factor(1)
Hpp_m2_n1 = -second_moment_factor(2) * second_moment_factor(1)
# Difference of quadratic coefficients is (Hpp_composite-Hpp_outer)/2.
defect_quadratic = (Hpp_m2_n1 - Hpp_outer) / 2
assert Hpp_outer == Fraction(-1, 9)
assert Hpp_m2_n1 == Fraction(-7, 27)
assert defect_quadratic == Fraction(-2, 27)

print(f"counterexample_density={g}")
print(f"admissible_interval_m2_n1={admissible_interval(2, 1)}")
print(f"admissible_interval_m2_n2={admissible_interval(2, 2)}")
print(f"Hpp_outer={Hpp_outer}")
print(f"Hpp_m2_n1={Hpp_m2_n1}")
print(f"entropy_defect_theta2_coefficient={defect_quadratic}")
