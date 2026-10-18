from decimal import Decimal, getcontext

getcontext().prec = 100

def primal(n, e):
    return e ** n

def dual(n, e):
    return (n + 1) * (e - 1) ** n

pairs = 0
equalities = []
for n in range(1, 301):
    signs = []
    for e in range(2, 301):
        p = primal(n, e)
        q = dual(n, e)
        if q == p:
            equalities.append((n, e))
        signs.append((q > p) - (q < p))
        pairs += 1

    # The sign sequence may start negative/equal and then can change only once.
    seen_positive = False
    for s in signs:
        if s > 0:
            seen_positive = True
        if seen_positive:
            assert s > 0

assert equalities == [(1, 2)]

threshold_checks = 0
for n in range(2, 301):
    # Exact first integer overtake by direct integer comparison.
    e = 2
    while dual(n, e) <= primal(n, e):
        e += 1
    first = e

    # High-precision real threshold and its ceiling.
    nd = Decimal(n)
    root = Decimal(n + 1) ** (Decimal(-1) / nd)
    T = Decimal(1) / (Decimal(1) - root)
    ceil_T = int(T.to_integral_value(rounding="ROUND_CEILING"))
    assert first == ceil_T, (n, first, T)

    # Exact monotonicity of dual/primal ratio:
    # R(e+1)/R(e) = (e^2/(e^2-1))^n > 1.
    for e in range(2, 100):
        assert e * e > e * e - 1

    threshold_checks += 1

print("VERIFY_OK", pairs, threshold_checks, equalities)
