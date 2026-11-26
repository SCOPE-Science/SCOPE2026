"""Fixed-flag census for the two versions of the fourth identity."""

from itertools import product


def check(p):
    # The first basis vector is 0, the second is 1, and the annihilator is 2.
    triples = tuple(product(range(2), repeat=3))
    equal_count = unequal_count = 0
    for a, b, u, v, c, ell, d, f, h, j in product(range(p), repeat=10):
        if not (a or b) or not (c or ell or d or f or h or j):
            continue
        left = ((0, a, u), (0, 0, c), (0, 0, d), (0, 0, h))
        right = ((0, b, v), (0, 0, ell), (0, 0, f), (0, 0, j))

        def r(M, x, y):
            ans = M[2*x:2*x+2]
            return tuple(sum(y[i]*ans[i][k] for i in range(2)) % p for k in range(3))

        def l(M, x, y):
            return tuple((x[0]*M[y][k] + x[1]*M[y+2][k]) % p for k in range(3))

        def sub(x, y):
            return tuple((v-w) % p for v, w in zip(x, y))

        first_three = True
        fourth = altered_fourth = True
        for x, y, z in triples:
            xy = 2*x+y
            yx = 2*y+x
            yz = 2*y+z
            xz = 2*x+z
            if (r(left, x, left[yz]) != r(left, x, right[yz]) or
                    l(right, left[xy], z) != l(right, right[xy], z) or
                    sub(r(left, x, left[yz]), l(left, left[xy], z)) !=
                    sub(r(right, y, left[xz]), l(left, right[yx], z))):
                first_three = False
                break
            rhs = sub(r(right, y, right[xz]), l(right, right[yx], z))
            fourth &= sub(r(right, x, right[yz]), l(right, right[xy], z)) == rhs
            altered_fourth &= sub(r(right, x, left[yz]), l(right, left[xy], z)) == rhs

        eq = bool(not (h or j) and a == b and a and c == ell and (c or d or f))
        neq = bool(not (h or j or c or f) and a != b and ell and ((b-a)*d-a*ell) % p == 0)
        assert (first_three and fourth) == (eq or neq)
        assert (first_three and altered_fourth) == eq
        equal_count += eq
        unequal_count += neq

    assert equal_count == (p-1)*p*p*(p**3-1)
    assert unequal_count == p**3*(p-1)**2
    lines = p*p+p+1
    flag_count = lines*(p+1)
    two_step = 1+lines*(p**8-1)+lines*(p*p-1)*(p*p-p)
    narrow = two_step + flag_count*equal_count
    wide = narrow + flag_count*unequal_count
    print(p, equal_count, unequal_count, narrow, wide)
    return narrow, wide


assert check(2) == (2416, 2584)
assert check(3) == (110241, 115857)
print('FIXED_FLAG_CENSUS_PASS')
