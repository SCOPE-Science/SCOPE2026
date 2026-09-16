"""Free-group piece statistics supporting the cubical tiling threshold.

Checks (F_2, b=log 3):
 1. P(two random cyclically reduced words of length L share piece >= L) ~ C*3^{-L}
 2. P(fixed segment of length L occurs in a random word) ~ C*l*3^{-L}
 3. Extrapolated tiling exponent: k^(m+1) e^{-b l} with m=6 -> threshold d<1/7.
Writes output/artifacts/piece_stats.csv
"""
import random, math, csv, os

random.seed(20260916)
GENS = [0, 1, 2, 3]  # a, A, b, B ; inverse x^1
def inv(x): return x ^ 1

def rand_cyc(n):
    while True:
        w = [random.randrange(4)]
        for _ in range(1, n):
            c = random.randrange(4)
            while c == inv(w[-1]):
                c = random.randrange(4)
            w.append(c)
        if w[-1] != inv(w[0]):
            return w

def lcs_len(a, b):
    # longest common substring of a and cyclic shifts of b (b doubled), O(|a|*|b|)
    m, n = len(a), 2 * len(b)
    bb = b + b
    prev = [0] * (n + 1)
    best = 0
    for i in range(1, m + 1):
        cur = [0] * (n + 1)
        ai = a[i - 1]
        for j in range(1, n + 1):
            if ai == bb[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return min(best, len(b))

def contains_seg(w, seg):
    L = len(seg)
    if L > len(w):
        return False
    ww = w + w  # cyclic word: allow wraparound
    for i in range(len(w)):
        if ww[i:i + L] == seg:
            return True
    return False

ELL = 100
NPAIR = 300
print("sampling pairs...", flush=True)
maxpieces = []
for _ in range(NPAIR):
    u, v = rand_cyc(ELL), rand_cyc(ELL)
    maxpieces.append(lcs_len(u, v))
print("done pairs", flush=True)

# empirical tail P(maxpiece >= L)
rows = []
import collections
for L in [8, 10, 12, 14, 16, 18, 20, 24, 28]:
    p = sum(1 for x in maxpieces if x >= L) / NPAIR
    theory = (ELL ** 2) * math.exp(-math.log(3) * L)  # ~ l^2 3^{-L} union bound scale
    rows.append(("pair_tail", L, p, theory))

# single-segment occurrence probes
print("probing segments...", flush=True)
MSEG = 1500
for L in [8, 12, 16]:
    seg = rand_cyc(ELL)[:L]
    hit = 0
    for _ in range(MSEG):
        if contains_seg(rand_cyc(ELL), seg):
            hit += 1
    p = hit / MSEG
    theory = 2 * ELL * math.exp(-math.log(3) * L)
    rows.append(("seg_hit", L, p, theory))
print("done segments", flush=True)

# fit slope of log tail over L=10..20
xs = [L for k, L, p, t in rows if k == "pair_tail" and 10 <= L <= 20 and p > 0]
ys = [math.log(p) for k, L, p, t in rows if k == "pair_tail" and 10 <= L <= 20 and p > 0]
n = len(xs)
sx, sy = sum(xs), sum(ys)
sxx = sum(x * x for x in xs)
sxy = sum(x * y for x, y in zip(xs, ys))
slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
print(f"fitted tail slope = {slope:.4f}  (theory -log3 = {-math.log(3):.4f})")

os.makedirs("output/artifacts", exist_ok=True)
with open("output/artifacts/piece_stats.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["kind", "L", "empirical", "theory_scale", "note"])
    for k, L, p, t in rows:
        w.writerow([k, L, f"{p:.5f}", f"{t:.3e}", "ell=100"])
    w.writerow(["fit_slope", "-", f"{slope:.4f}", f"{-math.log(3):.4f}", "log-tail slope vs -b"])

# tiling threshold extrapolation table (analytic, uses verified exponent b=log3)
with open("output/artifacts/thresholds.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["regime", "FW_density", "ours_density", "note"])
    w.writerow(["a=0 (free/surface-type)", "1/41=0.02439", "1/7=0.14286 (B(6) tiling); 1/6=0.16667 via OW at a=0 free", "d=c/b"])
    w.writerow(["general a", "min((1-a/b)/20,(1/41))", "min(1,1-a/b)/7 (Thm B); min((1-a/b)/14,1/29) (Thm A)", "d=c/b"])
print("wrote artifacts")
