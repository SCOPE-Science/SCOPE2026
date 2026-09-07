import itertools, hashlib, time, csv, os

# Normalized DCLS(10): a_0=0, (a_1..a_9) permutation of 1..9
# Column-Latin condition: b_k = (a_k - k) mod 10 must be permutation of Z10
t0 = time.time()
total = 0
passes = []
for perm in itertools.permutations(range(1, 10)):
    total += 1
    seen = 1  # bit 0 set (b_0 = 0)
    ok = True
    for k in range(1, 10):
        b = (perm[k - 1] - k) % 10
        bit = 1 << b
        if seen & bit:
            ok = False
            break
        seen |= bit
    if ok and seen == 1023:
        passes.append((0,) + perm)
elapsed = time.time() - t0
print(f"total scanned={total} passes={len(passes)} time={elapsed:.2f}s")
h = hashlib.sha256(repr(passes).encode()).hexdigest()
print("sha256(passes)=", h)
print("sum Z10 =", sum(range(10)), "=45 =", sum(range(10)) % 10, "mod10")
print("sum of b for any a = 0 mod10, contradiction")

os.makedirs("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-10/output/artifacts", exist_ok=True)
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-10/output/artifacts/dcls10_squares.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "col_latin", "sha256_row"])
    for a in passes:
        w.writerow(list(a) + [1, hashlib.sha256(repr(a).encode()).hexdigest()[:16]])
print("csv written")
