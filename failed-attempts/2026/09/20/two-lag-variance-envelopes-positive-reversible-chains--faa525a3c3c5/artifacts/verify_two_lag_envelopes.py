from fractions import Fraction as F


def H(N, x):
    total = F(N, 1)
    for k in range(1, N):
        total += 2 * (N-k) * (x ** k)
    return total / (N*N)


def canonical(rho, q):
    b = q / rho
    wlo = rho*rho / q
    d = 1 - 2*rho + q
    a = (rho-q) / (1-rho)
    whi = (q-rho*rho) / d
    return a, b, wlo, whi


def moments(nodes, weights):
    return tuple(sum(w * (x ** k) for x, w in zip(nodes, weights)) for k in range(3))


def tau(nodes, weights):
    return sum(w * (1+x)/(1-x) for x, w in zip(nodes, weights))


def fmt(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


cases = [
    (F(2,5), F(1,5), 10),
    (F(1,3), F(1,6), 7),
    (F(3,5), F(2,5), 12),
]

checks = 0
for rho, q, N in cases:
    assert 0 < rho < 1 and rho*rho <= q < rho
    a, b, wlo, whi = canonical(rho, q)
    lo_nodes = (F(0), b)
    lo_weights = (1-wlo, wlo)
    hi_nodes = (a, F(1))
    hi_weights = (1-whi, whi)
    assert moments(lo_nodes, lo_weights) == (1, rho, q)
    assert moments(hi_nodes, hi_weights) == (1, rho, q)
    checks += 2
    for k in range(3, 9):
        rlo = q**(k-1) / rho**(k-2)
        rhi = (1-whi)*(a**k) + whi
        assert sum(w*x**k for x,w in zip(lo_nodes,lo_weights)) == rlo
        assert sum(w*x**k for x,w in zip(hi_nodes,hi_weights)) == rhi
        checks += 2
    vlo = (1-wlo)*H(N,F(0)) + wlo*H(N,b)
    vhi = (1-whi)*H(N,a) + whi
    assert vlo <= vhi
    checks += 1

rho, q = F(2,5), F(1,5)
a, b, wlo, whi = canonical(rho, q)
r3_lo = q*q/rho
r3_hi = (1-whi)*a**3 + whi
V10_lo = (1-wlo)*H(10,F(0)) + wlo*H(10,b)
V10_hi = (1-whi)*H(10,a) + whi
assert r3_lo == F(1,10)
assert r3_hi == F(2,15)
assert V10_lo == F(7297,32000)
assert V10_hi == F(145709,546750)
assert tau((F(0), b), (1-wlo,wlo)) == F(13,5)
checks += 5

# Exact two-point ergodic approximants at fixed first two moments.
v = q-rho*rho
for c in (F(9,10), F(99,100), F(999,1000)):
    u = rho - v/(c-rho)
    wc = v/((c-rho)*(c-rho)+v)
    assert 0 <= u < rho < c < 1
    assert moments((u,c),(1-wc,wc)) == (1,rho,q)
    checks += 2

print(f"exact_checks={checks}")
print(f"example_rho={fmt(rho)} q={fmt(q)}")
print(f"r3_interval=[{fmt(r3_lo)},{fmt(r3_hi)}]")
print(f"V10_interval=[{fmt(V10_lo)},{fmt(V10_hi)}]")
print(f"V10_decimal=[{float(V10_lo):.12f},{float(V10_hi):.12f}]")
print(f"finite_ESS_interval=[{1/float(V10_hi):.12f},{1/float(V10_lo):.12f}]")
print(f"tau_lower={fmt(F(13,5))}")
for c in (F(9,10), F(99,100), F(999,1000)):
    u = rho - v/(c-rho)
    wc = v/((c-rho)*(c-rho)+v)
    t = tau((u,c),(1-wc,wc))
    print(f"fixed_moments_c={fmt(c)} u={fmt(u)} weight_c={fmt(wc)} tau={float(t):.12f}")
