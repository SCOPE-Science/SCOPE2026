import itertools

def count(n, cap=None):
    total = 0
    passes = 0
    first = None
    for perm in itertools.permutations(range(1, n)):
        total += 1
        seen = 1
        ok = True
        for k in range(1, n):
            b = (perm[k-1] - k) % n
            bit = 1 << b
            if seen & bit:
                ok = False
                break
            seen |= bit
        if ok and seen == (1 << n) - 1:
            passes += 1
            if first is None:
                first = (0,) + perm
            if cap and passes >= cap:
                break
    return total, passes, first

for n in [3, 5, 7, 9]:
    if n <= 7:
        t, p, f = count(n)
        print(f"n={n} scanned={t} passes={p} first={f}")
    else:
        # n=9: 8! =40320, full scan fine
        t, p, f = count(9)
        print(f"n={n} scanned={t} passes={p} first={f}")

# Verify first n=5 example builds a Latin square
a = count(5)[2]
print("a5 =", a)
n = 5
L = [[(i + a[(j-i) % n]) % n for j in range(n)] for i in range(n)]
for row in L:
    print(row)
# check Latin
assert all(sorted(r) == list(range(n)) for r in L), "rows"
assert all(sorted(L[i][j] for i in range(n)) == list(range(n)) for j in range(n)), "cols"
print("n=5 Latin check OK; diag-cyclic check:",
      all(L[(i+1) % n][(j+1) % n] == (L[i][j]+1) % n for i in range(n) for j in range(n)))
