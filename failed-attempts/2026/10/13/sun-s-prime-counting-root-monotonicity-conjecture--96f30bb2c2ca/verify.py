#!/usr/bin/env python3
import math

N = 2000
MAX_X = max((N + 1) * N, 100000)

is_prime = bytearray(b"\x01") * (MAX_X + 1)
is_prime[0:2] = b"\x00\x00"
for p in range(2, int(MAX_X ** 0.5) + 1):
    if is_prime[p]:
        is_prime[p*p:MAX_X+1:p] = b"\x00" * (((MAX_X - p*p) // p) + 1)

pi = [0] * (MAX_X + 1)
c = 0
for x in range(MAX_X + 1):
    c += is_prime[x]
    pi[x] = c

small = []
for n in range(5, 17):
    for k in range(1, n + 1):
        if k * n >= 17:
            continue
        A = pi[k*n]
        B = pi[(k+1)*n]
        left = A ** (k + 1)
        right = B ** k
        assert left > right, (n, k, A, B, left, right)
        small.append((n, k, A, B, left, right))
assert len(small) == 17

pairs = 0
sufficient = 0
for n in range(5, N + 1):
    ceil_half = (n + 1) // 2
    for k in range(1, n + 1):
        A = pi[k*n]
        B = pi[(k+1)*n]
        assert (k + 1) * math.log(A) > k * math.log(B), (n, k, A, B)
        d = B - A
        assert d <= ceil_half, (n, k, d, ceil_half)
        if k*n >= 17:
            assert A * math.log(A) > k * ceil_half, (n, k, A)
            sufficient += 1
        pairs += 1

for x in range(17, 100001):
    assert pi[x] > x / math.log(x), x

print(
    "VERIFY_OK",
    f"small_cases={len(small)}",
    f"parameter_pairs={pairs}",
    f"sufficient_checks={sufficient}",
    "prime_bound_check=17..100000",
    f"max_n={N}",
)
