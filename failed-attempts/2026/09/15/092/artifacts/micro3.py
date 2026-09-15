"""Micro-test 3: diagnose the 2-cycle.
S(0,1) after one step gave {(0,2,0,0,1): 1} -- WRONG sign handling?
S = bcd - b^2 e. Reduce b^2e via f3 (be-cd): b^2 e = b*(be) -> b*(cd) = bcd.
So S -> bcd - bcd. With lc = P-1 = -1: sub_scaled subtracts lc*G*q.
D[u] -= lc*c => for u=bcd: 1 - (-1)(-1) = 1-1 = 0. Good. For u=b^2e... wait q=(0,1,0,0,0),
G*q = {(0,2,0,0,1):1, (0,1,1,1,0):-1}. D -= lc*(that) = D +1*(that)? lc=-1 so D -= -1*Gq = D += Gq.
b^2e: -1 + 1 = 0. bcd: 1 + (-1) = 0. Total 0. So correct result is {}.
But micro2 'after one step' printed {(0,2,0,0,1): 1}. So micro2's inline code has a bug:
it popped t then added terms -- b^2e term: D had {bcd:1, b2e:-1}, popped b2e, then
u=b2e gets D[u] = 0 - lc*1 = 0+1 = 1?? Because D.get(u,0) is 0 after pop, minus lc*c = -(-1)(1)=+1.
AH: the reduction formula is wrong! Standard: replace lc*t by -lc*q*(G - LT)/lc_G...
D -= lc * q * G assumes G monic with LT coefficient 1 AND that t = q*LT exactly reproduces
the popped term: q*G contains q*LT = t with coeff 1, so D -= lc*q*G kills t. But here we
already popped t, so we should add -lc*q*(G - LT). Popping then subtracting double-counts.
Fix: do NOT pop first; or pop and add -lc*q*(G minus LT).
The micro_spair reduce_full has the same bug: pops t then sub_scaled over FULL G,
reintroducing t with coeff -lc. That creates the 2-cycle. Fix now.
"""
P = 32003
def E(*v):
    return tuple(v)
f1 = {E(1,0,0,1,0): 1, E(0,2,0,0,0): P - 1}
f2 = {E(1,0,0,0,1): 1, E(0,1,1,0,0): P - 1}
f3 = {E(0,1,0,0,1): 1, E(0,0,1,1,0): P - 1}
GB = [f1, f2, f3]
LTs = [E(1,0,0,1,0), E(1,0,0,0,1), E(0,1,0,0,1)]

def divmod_term(t, lt):
    if all(t[k] >= lt[k] for k in range(5)):
        return tuple(t[k] - lt[k] for k in range(5))
    return None

def reduce_full(D, cap=10000):
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
        for tt, c in GB[gi].items():
            if tt == LTs[gi]:
                continue
            u = tuple(tt[k] + q[k] for k in range(5))
            D[u] = (D.get(u, 0) - lc * c) % P
            if D[u] == 0:
                del D[u]
        steps += 1
        if steps > cap:
            return None, steps

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

from itertools import combinations
for i, j in combinations(range(3), 2):
    r, s = reduce_full(spoly(GB[i], GB[j], LTs[i], LTs[j]))
    print(f"S({i},{j}): steps={s} remainder={r}", flush=True)
print("GB-CHECK DONE", flush=True)
