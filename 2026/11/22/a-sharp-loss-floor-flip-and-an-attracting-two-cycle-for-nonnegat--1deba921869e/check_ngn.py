"""Exact rational consistency tests for the scalar positive-floor NGN map.

The universal conclusions rely on the algebraic proof in RESULT.md;
finite evaluations are independent regression checks, not exhaustive proof.
"""
from fractions import Fraction as F

def multiplier(y, a):
    return (y + 1 - a) / (1 + (1 + a) * y)

def derivative(y, a):
    return multiplier(y, a) + 2 * y * a*a / (1 + (1 + a)*y)**2

def next_y(y, a):
    return y * multiplier(y, a)**2

checks = 0
for a in [F(201,100), F(9,4), F(3), F(11,2), F(10), F(77)]:
    y = (a-2)/(a+2)
    assert y > 0
    assert multiplier(y,a) == -1
    assert next_y(y,a) == y
    assert derivative(y,a) == 1 - F(8)/a**2
    assert -1 < derivative(y,a) < 1
    assert 0 < derivative(y,a)**2 < 1 or derivative(y,a) == 0
    assert a*(1+y)/(1+(1+a)*y)==2 # effective curvature-normalized step
    checks += 7

for a in [F(1,10), F(1), F(3,2), F(199,100), F(2)]:
    for y in [F(1,1000),F(1,7),F(1,3),F(3,2),F(123)]:
        assert abs(multiplier(y,a)) < 1
        checks += 1

for y in [F(1,100),F(1,3),F(2,3),F(3,2),F(7)]:
    yp=next_y(y,F(2))
    if yp:
        assert 1/yp-1/y == 8*(1+y)/(1-y)**2
        checks += 1

# At curvature 1, offset 1, normalized base step 3, the exact
# antipodal cycle is ±sqrt(2/5): ratios and all quantities are rational.
a=F(3); c=F(1); y=F(1,5)
assert multiplier(y,a)==-1
assert derivative(y,a)==F(1,9)
assert derivative(y,a)**2==F(1,81)
assert y*c==F(1,5)  # excess objective value
assert a*(1+y)/(1+(1+a)*y)==2
assert (a-2)/(a+2)==y
checks+=6

# The origin has derivative 1-a and changes from attracting to repelling at a=2.
for a in [F(1,2),F(1),F(3,2),F(2),F(3),F(100)]:
    assert multiplier(F(0),a)==1-a
    checks+=1

print(f'EXACT_RATIONAL_CHECKS_PASS {checks}')
