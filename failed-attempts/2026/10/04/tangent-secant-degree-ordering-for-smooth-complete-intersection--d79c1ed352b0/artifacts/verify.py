from itertools import combinations_with_replacement

def degrees(N, ds):
    D = 1
    for d in ds:
        D *= d
    S = sum(ds)
    tangent = D * (S - N + 1)
    secant_num = D * (D - S + N - 2)
    assert secant_num % 2 == 0
    secant = secant_num // 2
    return D, tangent, secant

expected = {
    (4, (2, 2, 2)): (8, 24, 16),
    (4, (2, 2, 3)): (12, 48, 42),
    (4, (2, 2, 4)): (16, 80, 80),
}

seen = {}
checks = 0
for N in range(4, 10):
    m = N - 1
    for ds in combinations_with_replacement(range(2, 13), m):
        D, tangent, secant = degrees(N, ds)
        checks += 1
        if secant <= tangent:
            seen[(N, ds)] = (D, tangent, secant)

assert seen == expected, (seen, expected)
assert [k for k, v in seen.items() if v[1] == v[2]] == [(4, (2, 2, 4))]
print("VERIFY_OK", checks, sorted(seen.items()))
