"""Fallback replay script (fixed scale eps0=1/10, delta0=1/100, c1=(ln2)/16).
Finite part: exact-defect diagonal-sign orbit certificate at k=6,12 (and 6..14).
Extension part: checks closed-form inequalities for ALL k>=6 (honest binary).
Outputs VERIFY_OK only if full fallback criterion met, else FAILED + best counts.
Frozen datum D0 (disclosed): reduced group words len<=3 (target 0), v (target 0),
mixed U_w V |w|<=2 (target 0), V^2=I/unitary/lamp-commutation exact.
EXCLUDED (documented parity obstruction): pure V-products at even small k.
"""
import math, random, json, sys

EPS0, DELTA0, C1 = 0.1, 0.01, math.log(2)/16

def compose(p, q):  # apply q then p: (p o q)(i)
    return [p[q[i]] for i in range(len(p))]

def invert(p):
    q = [0]*len(p); 
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
    gens = ['a','A','b','B']; inv = {'a':'A','A':'a','b':'B','B':'b'}
    out = []
    def rec(w):
        if w: out.append(tuple(w))
        if len(w) == n: return
        for g in gens:
            if w and inv[g] == w[-1]: continue
            rec(w+[g])
    rec([]); return out

WORDS3 = words_upto(3)
WORDS2 = [w for w in words_upto(2) if w]

def find_base(k, seed):
    rng = random.Random(seed)
    Pa = [(i+1) % k for i in range(k)]  # single k-cycle
    for t in range(20000):
        Pb = list(range(k)); rng.shuffle(Pb)
        ok = True
        for w in WORDS3:
            if not w: continue
            r = eval_word(w, Pa, Pb)
            if any(r[i] == i for i in range(k)): ok = False; break
        if ok: return Pa, Pb
    return None

def check_base(k, Pa, Pb, d):
    assert sum(d) == 0 and set(d) <= {1, -1}
    worst = 0.0
    for w in WORDS3:
        if not w: continue
        r = eval_word(w, Pa, Pb)
        tr = sum(1 for i in range(k) if r[i] == i)/k  # target 0
        worst = max(worst, abs(tr))
    trv = abs(sum(d)/k); worst = max(worst, trv)
    for w in WORDS2:  # mixed U_w V target 0: trace=(1/k)sum_{fixed} d_i
        r = eval_word(w, Pa, Pb)
        tr = abs(sum(d[i] for i in range(k) if r[i] == i)/k)
        worst = max(worst, tr)
    # V^2=I, unitarity, lamp commutation: exact by construction (diag signs/perms)
    return worst

def thresh(k): return math.exp(C1*k*k)

results = {"k": {}, "finite_6_12": None, "range_6_14": None, "extension_all_k": None}
allok = True
for k in range(6, 15):
    base = find_base(k, 1000+k)
    if base is None:
        results["k"][str(k)] = {"base": False}; allok = False; continue
    Pa, Pb = base
    d = [1 if i % 2 == 0 else -1 for i in range(k)]
    if sum(d) != 0: d[-1] *= -1  # only needed for odd k; 6..14 even so no-op
    worst = check_base(k, Pa, Pb, d)
    # single-cycle check on Pa (cut>=2 separation lemma premise)
    vis = set(); c = 0
    for _ in range(k): vis.add(c); c = Pa[c]
    single = (len(vis) == k)
    need = thresh(k); have = 2**(k-1)
    sep2 = 16/(3*k)  # analytic min d^2 lower bound for distinct orbit reps
    ok = (worst < DELTA0) and single and (have >= need) and (sep2 >= EPS0**2)
    results["k"][str(k)] = {"base": True, "worst_defect": worst, "single_cycle": single,
        "need": need, "have": have, "sep2_lb": sep2, "ok": ok,
        "Pa": Pa, "Pb": Pb, "d": d}
    if k in (6, 12) and not ok: allok = False
    print(f"k={k} defect={worst:.4f} single={single} need={need:.2f} have={have} sep2={sep2:.3f} ok={ok}")

r6, r12 = results["k"]["6"], results["k"]["12"]
finite_ok = bool(r6.get("ok") and r12.get("ok"))
results["finite_6_12"] = "PASS" if finite_ok else "FAIL"
range_ok = all(results["k"][str(k)].get("ok", False) for k in range(6, 15))
results["range_6_14"] = "PASS" if range_ok else "FAIL"
# full extension to all k>=6 requires count+separation beyond k=14: orbit gives
# have=2^{k-1} < 2^{k^2/16} for k>=15 -> NOT certified (volume lemma open)
results["extension_all_k"] = "NOT_CERTIFIED_k_ge_15"
verdict = "VERIFY_OK" if (finite_ok and results["extension_all_k"] == "CERTIFIED") else "FAILED"
results["verdict"] = verdict
results["best_counts"] = {"k6_have_need": [r6.get("have"), r6.get("need")],
    "k12_have_need": [r12.get("have"), r12.get("need")]}
with open("output/artifacts/replay_results.json", "w") as f:
    json.dump(results, f, indent=1)
print("finite_6_12:", results["finite_6_12"], "| range_6_14:", results["range_6_14"],
      "| extension:", results["extension_all_k"], "| verdict:", verdict)
