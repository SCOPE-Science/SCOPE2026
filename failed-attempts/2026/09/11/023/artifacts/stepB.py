"""Step B: find base perms (BOTH free) with all |w|<=3 words fixed-point-free.
Then valid patterns = ALL balanced sign vectors (mixed/group defects exactly 0).
Count vs need; separation automatic (min dist^2 = 8/k >> eps0^2). Bounded: ~60s."""
import math, random, json

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

def nfixed(w, Pa, Pb):
    r = eval_word(w, Pa, Pb)
    return sum(1 for i in range(len(Pa)) if r[i] == i)

def try_find(k, seed, iters=60000):
    rng = random.Random(seed)
    base = list(range(k))
    for t in range(iters):
        Pa = base[:]; rng.shuffle(Pa)
        Pb = base[:]; rng.shuffle(Pb)
        ok = True
        for w in WORDS3:
            if nfixed(w, Pa, Pb) > 0:
                ok = False; break
        if ok: return Pa, Pb, t
    return None

out = {}
for k in (6, 12):
    r = try_find(k, 777+k, iters=(40000 if k == 6 else 60000))
    if r is None:
        out[k] = {"found": False}
        print(f"k={k}: NO base found in budget")
    else:
        Pa, Pb, t = r
        need = math.exp((math.log(2)/16)*k*k)
        from math import comb
        have = comb(k, k//2)
        sep2 = 8.0/k
        out[k] = {"found": True, "iters": t, "need": need, "have": have,
                  "sep2": sep2, "Pa": Pa, "Pb": Pb,
                  "ok": have >= need and sep2 >= 0.01}
        print(f"k={k}: base found it={t} need={need:.2f} have={have} "
              f"min-sep^2={sep2:.3f} ok={out[k]['ok']}")
with open("output/artifacts/stepB.json", "w") as f:
    json.dump(out, f, indent=1)
