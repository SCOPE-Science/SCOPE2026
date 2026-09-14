"""Independent verifier for the cyclic non-existence lemma (brute force, pure Python).
Reads nothing; enumerates all 2^20 complement-classes of cyclic colorings of K43,
checks the 111930 five-sets containing vertex 0 (translation symmetry), reports
number of K5-free colorings found. Cross-checks the C program cyc/cyc_verify.
"""
import itertools

N = 43
S0 = [s for s in itertools.combinations(range(1, N), 4)]  # 5-sets {0}+4, count C(42,4)
assert len(S0) == 111930, len(S0)

def dclass(a, b):
    d = abs(a - b)
    if d > N - d:
        d = N - d
    return d

free = 0
checked = 0
for mask in range(1 << 20):
    d = [0] * 22
    d[1] = 0
    for k in range(2, 22):
        d[k] = (mask >> (k - 1)) & 1
    ok = True
    for (a, b, e, f) in S0:
        s = (d[dclass(0,a)] + d[dclass(0,b)] + d[dclass(0,e)] + d[dclass(0,f)]
             + d[dclass(a,b)] + d[dclass(a,e)] + d[dclass(a,f)]
             + d[dclass(b,e)] + d[dclass(b,f)] + d[dclass(e,f)])
        if s == 0 or s == 10:
            ok = False
            break
    checked += 1
    if ok:
        free += 1
        print("FOUND", mask)
print(f"checked={checked} K5free_cyclic={free}")
