from fractions import Fraction
from math import prod

N = 60
K = 8
PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89]


def pow2(m):
    return Fraction(2**m, 1) if m >= 0 else Fraction(1, 2**(-m))


def atanh_bounds(z, terms=N):
    z = Fraction(z)
    assert 0 <= z <= Fraction(1,3)
    s = Fraction(0)
    term = z
    z2 = z*z
    for j in range(terms + 1):
        s += term / (2*j + 1)
        term *= z2
    # Positive tail bounded by replacing all later denominators by the first omitted one.
    rem = term / (2*terms + 3) / (1-z2)
    return 2*s, 2*(s + rem)


def log_bounds(x, terms=N):
    x = Fraction(x)
    assert x > 0
    m = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(m):
        m -= 1
    while x >= pow2(m+1):
        m += 1
    y = x / pow2(m)
    assert 1 <= y < 2
    l2, u2 = atanh_bounds(Fraction(1,3), terms)
    z = (y-1)/(y+1)
    ly, uy = atanh_bounds(z, terms)
    if m >= 0:
        return m*l2 + ly, m*u2 + uy
    return m*u2 + ly, m*l2 + uy


def a_coeff(k, p):
    # (1+1/p)^k - 1
    return Fraction((p+1)**k - p**k, p**k)


def b_coeff(k, q):
    # 1-(1+1/q)^(-k)
    return Fraction((q+1)**k - q**k, (q+1)**k)


def bootstrap_sign(k, q, p):
    # Sign of L_k(p,0)-U_k(q,1), after multiplying by the positive factor k log p log q:
    # A(k,p) log q - B(k,q) log p.
    lq, uq = log_bounds(q)
    lp, up = log_bounds(p)
    A = a_coeff(k,p)
    B = b_coeff(k,q)
    return A*lq - B*up, A*uq - B*lp


def direct_order_ratio_bounds(p):
    # Cor. 3.10 exponent-one threshold ratio
    # log(1 + log(p)/log(2)) / log(1+1/p).
    lp_l, lp_u = log_bounds(p)
    l2_l, l2_u = log_bounds(2)
    t_l = 1 + lp_l/l2_u
    t_u = 1 + lp_u/l2_l
    num_l, _ = log_bounds(t_l)
    _, num_u = log_bounds(t_u)
    den_l, den_u = log_bounds(Fraction(p+1,p))
    return num_l/den_u, num_u/den_l

positive = []
for q,p in zip(PRIMES, PRIMES[1:]):
    lo, hi = bootstrap_sign(K,q,p)
    assert lo > 0, (q,p,float(lo),float(hi))
    positive.append((q,p,float(lo)))

lo_fail, hi_fail = bootstrap_sign(K,89,97)
assert hi_fail < 0

primorial = prod(PRIMES)
assert primorial == 23768741896345550770650537601358310

rlo, rhi = direct_order_ratio_bounds(89)
assert rlo > 180 and rhi < 181

# Cor. 3.10 directly guarantees all exponent-one primes through 5 at k=8 but not 7.
def direct_ratio(p):
    lo, hi = direct_order_ratio_bounds(p)
    return lo, hi
for p in [2,3,5]:
    lo, hi = direct_ratio(p)
    assert hi <= 8
lo7, hi7 = direct_ratio(7)
assert lo7 > 8

print('VERIFY_OK')
print(f'k={K} adjacent_bootstrap_edges={len(positive)} endpoint={PRIMES[-1]} next_prime=97')
print(f'primorial_89={primorial}')
print(f'min_certified_positive_cross_margin={min(x[2] for x in positive):.15g}')
print(f'89_to_97_certified_negative_cross_margin_upper={float(hi_fail):.15g}')
print(f'corollary_3_10_89primorial_order_ratio_in=({float(rlo):.15g},{float(rhi):.15g}) ceiling=181')
print('corollary_3_10_direct_at_k8_primes_through=5; prime_7_not_directly_certified')
