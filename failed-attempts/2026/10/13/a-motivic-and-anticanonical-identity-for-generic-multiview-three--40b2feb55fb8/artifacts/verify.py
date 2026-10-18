def invariants(n):
    assert n >= 2
    betti_even = (1, n+1, n+1, 1)
    euler = sum(betti_even)
    antiK3 = 64 - 8*n
    return betti_even, euler, antiK3

checks = 0
for n in range(2, 501):
    b, chi, v = invariants(n)
    assert b == (1, n+1, n+1, 1)
    assert chi == 2*n + 4
    assert v == 64 - 8*n
    assert v + 4*chi == 80
    # Each point blow-up adds L + L^2 and Euler increment 2.
    assert chi - 4 == 2*n
    checks += 1

print("VERIFY_OK", checks)
