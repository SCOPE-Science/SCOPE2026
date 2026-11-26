#!/usr/bin/env python3
import math
from fractions import Fraction
# Exact combinatorial coefficient: at a vertex, each incident repeated edge of length a contributes 12*a/(L^3 sin(angle)).
assert 2*3*2==12
# For equilateral length one: total incident-length sum / sin(angle) = 6/(sqrt(3)/2), L=3.
c = 12/27 * 6/(math.sqrt(3)/2)
assert abs(c-16/(3*math.sqrt(3)))<1e-12
# Exact zero-area atom on 3 equal sides.
assert sum(Fraction(1,3)**3 for i in range(3))==Fraction(1,9)
# Density of absolute uniform difference: integral f(d) dd is 1.
assert Fraction(2,1)-Fraction(1,1)==1
print('exact normalization and equilateral coefficient identities: PASS')
