"""Independent finite checks for the three-descent Eulerian dyadic fiber law.

Run: python3 verify.py. Standard library only. Finite checks corroborate,
not replace, the unrestricted mathematical proof in RESULT.md.
"""
from collections import Counter
from math import comb


def e_formula(n):
    if n < 4:
        return 0
    return 4**n - (n + 1)*3**n + comb(n + 1, 2)*2**n - comb(n + 1, 3)


def g(n):
    return -(n + 1)*3**n - comb(n + 1, 3)


def val2(z):
    if z == 0:
        raise ValueError("valuation of zero")
    z = abs(z)
    return (z & -z).bit_length() - 1


# Independent classical Eulerian recurrence, with 0-based descent index.
prev = [1]
recurrence_checks = 0
for n in range(2, 105):
    curr = [0]*n
    for j in range(n):
        x = (j + 1)*prev[j] if j < len(prev) else 0
        y = (n-j)*prev[j-1] if j > 0 else 0
        curr[j] = x + y
    if n >= 4:
        assert curr[3] == e_formula(n), (n, curr[3], e_formula(n))
        recurrence_checks += 1
    prev = curr

# Exact finite-period histograms from direct expression at separate cutoffs.
histogram_checks = 0
period_checks = 0
for k in range(1, 13):
    m = 1 << k
    period = 2*m
    for start in [max(4,k), max(4,k)+1, max(4,k)+7]:
        actual = Counter(e_formula(n) % m for n in range(start, start+period))
        for y in range(m):
            if k >= 4:
                want = 9 if y % 16 in (0,10) else 1
            elif k == 3:
                want = 5 if y in (0,2) else 1
            else:
                want = 3 if (y % 2 == 0) else 1
            assert actual.get(y,0) == want,(k,start,y,actual.get(y,0),want)
            histogram_checks += 1
        for n in range(start,start+period):
            assert (e_formula(n+period)-e_formula(n))%m==0
            period_checks += 1

# Exact 2-adic difference behavior for all four odd-branch charts and even branch.
isometry_checks = 0
for t in range(0,52):
    for s in range(t+1,54):
        assert val2(g(2*t)-g(2*s))==val2(t-s)
        isometry_checks += 1
for r in range(4):
    for u in range(0,34):
        for v in range(u+1,35):
            t,s = r+4*u,r+4*v
            assert val2(g(2*t+1)-g(2*s+1))==4+val2(u-v),(r,u,v)
            isometry_checks += 1

# Verify 16-adic class centers and finite odd-branch image.
assert [g(2*t+1)%16 for t in range(4)]==[10,0,10,0]
print("VERIFY_OK")
print("independent_eulerian_recurrence_terms",recurrence_checks)
print("residue_fiber_comparisons",histogram_checks)
print("modular_period_comparisons",period_checks)
print("sharp_isometry_pairs",isometry_checks)
print("all_levels_finite_checks=PASS")
