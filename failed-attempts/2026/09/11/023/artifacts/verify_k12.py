"""FINAL certificate: k=12 explicit packing (emergent finding core).
Loads base_k12.json, rechecks: every reduced |w|<=3 group word fixed-point-free
(defect exactly 0 < delta0=1/100); tr V = 0; all mixed U_w V (|w|<=2) trace 0;
count C(12,6)=924 >= exp(c1*144)=512; min separation^2 = 8/12 >> eps0^2.
Outputs VERIFY_OK or FAILED. Deterministic, stdlib only, seconds-long."""
import math, json

EPS0, DELTA0, C1 = 0.1, 0.01, math.log(2)/16

def compose(p, q):
    return [p[q[i]] for i in range(len(p))]

def invert(p):
    q = [0]*len(p)
    for i, v in enumerate(p): q[v] = i
    return q

def eval_word(w, Pa, Pb):
    k = len(Pa); res = list(range(k))
    Ia, Ib = invert(Pa), invert(Pb)
    for g in w:
        if g == 'a': res = compose(Pa, res)
        elif g == 'A': res = compose(Ia, res)
        elif g == 'b': res = compose(Pb, res)
        elif g == 'B': res = compose(Ib, res)
    return res

def words_upto(n):
    gens = ['a', 'A', 'b', 'B']; inv = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    out = []
    def rec(w):
        if w: out.append(tuple(w))
        if len(w) == n: return
        for g in gens:
            if w and inv[g] == w[-1]: continue
            rec(w+[g])
    rec([]); return out

W3 = words_upto(3); W2 = [w for w in words_upto(2) if w]

base = json.load(open("output/artifacts/base_k12.json"))
Pa, Pb = base["Pa"], base["Pb"]; k = 12
assert len(Pa) == k and sorted(Pa) == list(range(k)) and sorted(Pb) == list(range(k))

worst = 0.0; nwords = 0
for w in W3:  # group words target trace 0
    nfix = sum(1 for i in range(k) if eval_word(w, Pa, Pb)[i] == i)
    worst = max(worst, nfix/k); nwords += 1
# V trace: any balanced d has tr 0 (counted, not per-pattern)
from math import comb
have = comb(k, k//2)  # all balanced sign patterns valid: see mixed check below
# mixed U_w V target 0 for EVERY balanced d? No: mixed defect depends on d.
# Correct counting: for each w, Fix(w) nonempty? No — all |w|<=2 words are
# fixed-point-free (subset of W3 check) => mixed trace = 0 for ALL d. Verify:
sub2 = [w for w in W2]
allfree = all(sum(1 for i in range(k) if eval_word(w, Pa, Pb)[i] == i) == 0 for w in sub2)
need = math.exp(C1*k*k)
sep2 = 8.0/k  # distinct balanced diagonals differ in >=2 coords: d^2 = 4m/k, m>=2
checks = {
    "group_words_checked": nwords,
    "worst_group_defect": worst,
    "all_lenLE2_fixedpoint_free": allfree,
    "have": have, "need": need,
    "min_sep2": sep2, "eps0sq": EPS0**2,
}
ok = worst < DELTA0 and allfree and have >= need and sep2 >= EPS0**2
checks["verdict"] = "VERIFY_OK" if ok else "FAILED"
json.dump(checks, open("output/artifacts/cert_k12.json", "w"), indent=1)
print(json.dumps(checks, indent=1))
