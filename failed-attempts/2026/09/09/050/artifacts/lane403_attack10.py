"""Lane-403 attack v10: E1 at m=4 (levels 16->32), exact count check."""
import json, os

ART = os.path.dirname(os.path.abspath(__file__))
res = {}

def compose(p, q):
    return [p[q[i]] for i in range(len(q))]

def odo(N):
    return [(a + 1) % N for a in range(N)]

def single(p):
    n = len(p)
    seen = [False] * n
    x, c = 0, 0
    while not seen[x]:
        seen[x] = True
        x = p[x]
        c += 1
    return c == n

def invert(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return q

def conj(g, s):
    return compose(compose(g, s), invert(g))

s4 = odo(16)
s5 = odo(32)
# lifts: psi(a) = s4(a%16) + 16*e_a, bijective iff e_b != e_{b+16} per b.
# Parametrize: e_b = bit_b(mask), e_{b+16} = 1 - bit_b. (2^16 bijective lifts.)
lifts = set()
for mask in range(2 ** 16):
    psi = [0] * 32
    for b in range(16):
        e = (mask >> b) & 1
        psi[b] = ((b + 1) % 16) + 16 * e
        psi[b + 16] = ((b + 1) % 16) + 16 * (1 - e)
    # quick single check via parity-sum shortcut? just full check
    if single(psi):
        lifts.add(tuple(psi))
res["U_cyclic_lifts"] = len(lifts)
res["predicted"] = 2 ** 15  # 2^{2^4 - 1}

# V-orbit: 2^16 fiber swaps; enumerate all
loc = set()
for mask in range(2 ** 16):
    g = list(range(32))
    for b in range(16):
        if (mask >> b) & 1:
            g[b], g[b + 16] = g[b + 16], g[b]
    loc.add(tuple(conj(g, s5)))
res["V_size"] = 2 ** 16
res["distinct"] = len(loc)
res["predicted_orbit"] = 2 ** 15
res["covers_all"] = lifts <= loc
res["equal"] = lifts == loc
res["coverage"] = len(lifts & loc) / len(lifts)

with open(os.path.join(ART, "finite_level_log10.json"), "w") as f:
    json.dump({"U_cyclic_lifts": res["U_cyclic_lifts"],
               "predicted": res["predicted"], "V_size": res["V_size"],
               "distinct": res["distinct"], "covers_all": res["covers_all"],
               "equal": res["equal"], "coverage": res["coverage"]}, f, indent=1)
print(json.dumps({k: v for k, v in res.items()}, indent=1))
