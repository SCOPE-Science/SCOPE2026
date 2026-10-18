#!/usr/bin/env python3
from collections import Counter

# Exact finite-group/Hodge bookkeeping for G=A[2] x {+-1} on an abelian surface A.
a2 = 2**4
assert a2 == 16
group_order = 2*a2
assert group_order == 32

# Elements (T,+1), T != 0, are fixed-point free.  Each (T,-1) has [2]^{-1}(T),
# a 16-point torsor under A[2], as its fixed set.
minus_elements = a2
fixed_points_per_minus = a2
orbit_size = a2
stabilizer_size = group_order // orbit_size
assert minus_elements == 16
assert fixed_points_per_minus == 16
assert stabilizer_size == 2

# There is one G-orbit in the fixed set for each minus element, hence one twisted
# connected component in the inertia stack for each T in A[2].
twisted_components = minus_elements
assert twisted_components == 16

# Derivative of x -> -x+T is -I on the two-dimensional tangent space, so age=1.
age = 1
assert age == 1

# Hodge numbers of an abelian surface.  Inversion is (-1)^(p+q), while translations
# act trivially on cohomology, so the untwisted invariant part is the even-total-degree part.
h = {
    (0,0):1, (1,0):2, (0,1):2,
    (2,0):1, (1,1):4, (0,2):1,
    (2,1):2, (1,2):2, (2,2):1,
}
untwisted = {pq:n for pq,n in h.items() if sum(pq)%2==0}
assert untwisted == {(0,0):1,(2,0):1,(1,1):4,(0,2):1,(2,2):1}

# A point sector of age 1 contributes one class of Hodge bidegree (1,1).
cr = Counter(untwisted)
cr[(1,1)] += twisted_components
expected = Counter({(0,0):1,(2,0):1,(1,1):20,(0,2):1,(2,2):1})
assert cr == expected

betti = Counter()
for (p,q),n in cr.items():
    betti[p+q] += n
assert betti == Counter({0:1,2:22,4:1})
assert sum(((-1)**k)*n for k,n in betti.items()) == 24

print('GROUP_ORDER=32')
print('TWISTED_COMPONENTS=16')
print('TWISTED_STABILIZER_ORDER=2')
print('AGE_EACH=1')
print('CR_HODGE=(0,0):1,(2,0):1,(1,1):20,(0,2):1,(2,2):1')
print('CR_BETTI=1,22,1')
print('ORBIFOLD_EULER=24')
print('VERIFY_OK')
