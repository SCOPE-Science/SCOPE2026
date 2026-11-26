import math

def l1_series(q, tol=1e-15):
    s = 0.0
    term = 1.0
    for k in range(1, 500):
        term *= q / k
        add = ((-1.0) ** (k + 1)) * term / k
        s += add
        if abs(add) <= tol * max(1.0, abs(s)):
            return s
    raise RuntimeError("series did not converge")

def l2_series(q, tol=1e-15):
    s = 0.0
    term = 1.0
    for k in range(1, 500):
        term *= q / k
        add = term / k
        s += add
        if abs(add) <= tol * max(1.0, abs(s)):
            return s
    raise RuntimeError("series did not converge")

def finite_sums(q, m):
    n = int(round(m*q)) - 1
    a = 1.0 - 1.0/m
    l1 = 0.0
    l2 = 0.0
    p = 1.0
    pinv = 1.0
    for i in range(1, n+1):
        p *= a
        pinv /= a
        l1 += (1.0-p)/i
        l2 += (pinv-1.0)/i
    return l1, l2

expected = {
    1.0: (0.7965995992970534, 1.3179021514544038),
    2.0: (1.3192633561695393, 3.6838715105404117),
    3.0: (1.6888763346638398, 8.258004617055773),
    20.0: (3.572947938777151, 25615649.09110865),
}
for q, (e1, e2) in expected.items():
    a, b = l1_series(q), l2_series(q)
    assert abs(a-e1) <= 2e-11*max(1.0, abs(e1))
    assert abs(b-e2) <= 2e-11*max(1.0, abs(e2))
for q in (1.0, 2.0, 3.0):
    a, b = finite_sums(q, 20000)
    assert abs(a-l1_series(q)) < 2e-4
    assert abs(b-l2_series(q)) < 2e-3
print("VERIFY_OK")
