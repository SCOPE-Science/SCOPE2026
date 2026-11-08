"""Independent exact enumeration for the lunar divisor-count inequality.
Run: python3 verify_lunar.py. Only finite corroboration; unrestricted proof is separate.
"""
from collections import defaultdict

def digits(n, base):
    d = []
    while n:
        d.append(n % base)
        n //= base
    return d

def lunar_mul(u, v, b):
    a, c = digits(u, b), digits(v, b)
    z = [0] * (len(a) + len(c) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(c):
            z[i + j] = max(z[i + j], min(x, y))
    return sum(d * b ** i for i, d in enumerate(z))

def lunar_sum(nums, b):
    ans = []
    for n in nums:
        d = digits(n, b)
        while len(ans) < len(d):
            ans.append(0)
        for i, x in enumerate(d):
            ans[i] = max(ans[i], x)
    return sum(x*b**i for i, x in enumerate(ans))

def length(n, b):
    return len(digits(n, b))

n_checked, products, missing_checked = 0, 0, 0
for b in range(2, 11):
    maximum = b**3 - 1 if b <= 7 else b**2 - 1
    divs = defaultdict(set)
    for u in range(1, maximum + 1):
        lu = length(u, b)
        for v in range(1, b ** (3-lu+1)):
            x = lunar_mul(u, v, b)
            products += 1
            if x <= maximum:
                divs[x].add(u)
                divs[x].add(v)
    for n in range(1, maximum + 1):
        dset = divs[n]
        assert dset, (b, n, 'no divisors')
        sigma = lunar_sum(dset, b)
        d = len(dset)
        assert (d == sigma) == (n == 1), (b, n, d, sigma)
        assert d <= sigma, (b, n, d, sigma)
        if n >= b:
            r = n % b
            w = n-r if r else n+1
            assert 1 <= w <= sigma and w not in dset, (b,n,w,sigma)
            missing_checked += 1
        n_checked += 1
print(f'VERIFY_OK bases=2..10 inputs={n_checked} products={products} '
      f'missing_witnesses={missing_checked} all_strict_for_n_gt_one=PASS '
      f'equality_only_n_one=PASS unit_divisor_sum=PASS')
