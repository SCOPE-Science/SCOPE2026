"""Independent stdlib-only verifier for witness_36_11_12.json.
Recomputes rank, full support, and the exact weight enumerator from the
stored generator matrix; asserts [36,11,12]. Usage: python3 verify_witness.py
"""
import json

with open("witness_36_11_12.json") as f:
    W = json.load(f)

n, k = W["n"], W["k"]
rows = W["generator_rows"]
assert len(rows) == k and all(0 <= r < (1 << n) for r in rows)

# rank
R = list(rows)
r = 0
for b in range(n - 1, -1, -1):
    piv = next((i for i in range(r, len(R)) if (R[i] >> b) & 1), None)
    if piv is None:
        continue
    R[r], R[piv] = R[piv], R[r]
    for i in range(len(R)):
        if i != r and ((R[i] >> b) & 1):
            R[i] ^= R[r]
    r += 1
assert r == k, f"rank {r} != {k}"

dist = {}
supp = 0
for mask in range(1 << k):
    w = 0
    for i in range(k):
        if (mask >> i) & 1:
            w ^= rows[i]
    supp |= w
    wt = bin(w).count("1")
    dist[str(wt)] = dist.get(str(wt), 0) + 1

assert dist == W["weight_enumerator"], "enumerator mismatch"
dmin = min(int(x) for x in dist if int(x) > 0)
assert dmin == W["d"] == 12, f"min distance {dmin}"
assert sum(dist.values()) == (1 << k)
assert supp == (1 << n) - 1, "not full support"
print(f"VERIFY OK: binary [{n},{k},{dmin}] full-support code; "
      f"{dist.get('12',0)} words of weight 12; enumerator matches.")
