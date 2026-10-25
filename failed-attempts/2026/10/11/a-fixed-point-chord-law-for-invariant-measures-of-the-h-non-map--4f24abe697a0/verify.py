from fractions import Fraction as F

# Generic root algebra: roots satisfy sum=-(1-b)/a and product=-1/a.
a = F(7, 5)
b = F(3, 10)
root_sum = -(1-b)/a
root_product = -1/a

assert root_sum == F(-1, 2)
assert root_product == F(-5, 7)

# For any symbolic mean m, compare polynomial coefficients in
# Var = [1-(1-b)m]/a - m^2
# with -(m-x_-)(m-x_+) = -m^2 + (x_-+x_+)m - x_-x_+.
coef_m2_lhs = F(-1)
coef_m_lhs = -(1-b)/a
coef_0_lhs = 1/a

coef_m2_rhs = F(-1)
coef_m_rhs = root_sum
coef_0_rhs = -root_product

assert (coef_m2_lhs, coef_m_lhs, coef_0_lhs) == (
    coef_m2_rhs, coef_m_rhs, coef_0_rhs
)

# Classical discriminant and sharp x-variance bound.
disc = (1-b)**2 + 4*a
assert disc == F(609, 100)

# (x_+-x_-)^2 = disc/a^2.
x_gap_sq = disc/(a*a)
x_var_max = x_gap_sq/4
assert x_var_max == F(609, 784)

# Total coordinate variance multiplies by 1+b^2.
total_var_max = (1+b*b)*x_var_max
assert total_var_max == F(66381, 78400)

# Marginal scaling example.
vx = F(17, 23)
vy = b*b*vx
assert vy == F(9, 100)*vx
assert vx + vy == (1+b*b)*vx

print("VERIFY_OK")
