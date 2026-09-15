"""Micro-test: S-pair reduction for case B only."""
P = 32003

def sub_scaled(D, G, q, scale):
    for t, c in G.items():
        u = tuple(t[k] + q[k] for k in range(5))
        D[u] = (D.get(u, 0) - scale * c) % P
        if D[u] == 0:
            del D[u]

def divmod_term(t, lt):
    if all(t[k] >= lt[k] for k in range(5)):
        return tuple(t[k] - lt[k] for k in range(5))
    return None

def lt_lex(D):
    return max(D, key=lambda t: tuple(t[v] for v in range(5)))

def reduce_full(D, GB, LTs, cap=2000):
    D = {t: c % P for t, c in D.items() if c % P != 0}
    steps = 0
    while True:
        hit = None
        for t in D:
            for gi, lt in enumerate(LTs):
                q = divmod_term(t, lt)
                if q is not None:
                    hit = (t, gi, q); break
            if hit is not None:
                break
        if hit is None:
            return D, steps
        t, gi, q = hit
        lc = D.pop(t)
        sub_scaled(D, GB[gi], q, lc)
        steps += 1
        if steps > cap:
            return None, steps

def E(*v):
    return tuple(v)

f1 = {E(1,0,0,1,0): 1, E(0,2,0,0,0): P - 1}
f2 = {E(1,0,0,0,1): 1, E(0,1,1,0,0): P - 1}
f3 = {E(0,1,0,0,1): 1, E(0,0,1,1,0): P - 1}
GB = [f1, f2, f3]
LTs = [lt_lex(g) for g in GB]
print("LTs:", LTs, flush=True)
from itertools import combinations
def spoly(F, G, ltf, ltg):
    L = tuple(max(a, b) for a, b in zip(ltf, ltg))
    qf = tuple(L[k] - ltf[k] for k in range(5))
    qg = tuple(L[k] - ltg[k] for k in range(5))
    D = {}
    for t, c in F.items():
        u = tuple(t[k] + qf[k] for k in range(5))
        D[u] = (D.get(u, 0) + c) % P
    for t, c in G.items():
        u = tuple(t[k] + qg[k] for k in range(5))
        D[u] = (D.get(u, 0) - c) % P
    return {t: c for t, c in D.items() if c}
for i, j in combinations(range(3), 2):
    r, s = reduce_full(spoly(GB[i], GB[j], LTs[i], LTs[j]), GB, LTs)
    print(f"S({i},{j}): steps={s} remainder={r}", flush=True)
print("DONE", flush=True)
