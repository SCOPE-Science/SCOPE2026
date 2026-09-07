"""Enumerate S = {k in (1e7,1e7+200] : sixth-power-free} deterministically."""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
KMIN, KMAX = 10_000_000, 10_000_200
PRIMES = [2, 3, 5, 7, 11, 13]
P6 = {p: p**6 for p in PRIMES}
S, excluded = [], []
for k in range(KMIN + 1, KMAX + 1):
    bad = [p for p in PRIMES if k % P6[p] == 0]
    if bad:
        excluded.append((k, bad))
    else:
        S.append(k)
print(f"|S| = {len(S)}, excluded = {len(excluded)}")
for k, bad in excluded:
    print(f"excluded {k}: divisible by {[f'{p}^6={P6[p]}' for p in bad]}")
with open(os.path.join(HERE, "S.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["k"])
    for k in S:
        w.writerow([k])
print("wrote S.csv")
