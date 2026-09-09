"""Lane-403 attack v4: Odometer-Exclusion certificates + corrected rigidity.

(a) Factor-miss cert: 2^n mod 3 != 0 for n <= 64 (binary odometer admits no
    3-block cyclic quotient at any level; combinatorial shadow of the
    eigenvalue obstruction).
(b) U_3 nonempty (finite-level proxy): explicit single-24-cycle psi on atoms
    0..23 with psi cycling 3 fixed blocks of 8 (B_j = {a : a mod 3 == j}),
    i.e. proj(psi(a)) = proj(a)+1 mod 3. Minimality proxy: single cycle.
(c) Corrected rigidity for pure odometer (factorial tower 2,6,24): uniform
    closeness d(phi^k,id) measured by deepest tower level whose quotient is
    fixed pointwise by phi^k (Cantor-uniform shadow), NOT atom-move fraction.
(d) Pure binary odometer single-cycles to level 12 + coherence.
"""
import json, os

ART = os.path.dirname(os.path.abspath(__file__))
res = {}

# (a)
res["pow2_mod3"] = {n: (2 ** n) % 3 for n in range(1, 65)}
res["pow2_mod3_all_nonzero"] = all(v != 0 for v in res["pow2_mod3"].values())

# (b) U_3 witness: blocks B_j = {a: a mod 3 == j}; psi(a) = rho(a)+1 mod 3
# class, cycling within fiber. Build: order atoms linked-list style.
def build_U3():
    # fibers: F_j = [a : a%3==j], each size 8. Chain F0 -> F1 -> F2 -> F0
    # so psi maps a in F_j to an element of F_{j+1}; arrange single cycle:
    # list cycle: interleave F0,F1,F2 orderings then close.
    F = [[a for a in range(24) if a % 3 == j] for j in range(3)]
    cyc = F[0] + F[1] + F[2]  # visit order
    # psi(cyc[i]) = cyc[(i+1) % 24]: check block advance by +1 mod 3?
    # cyc boundaries: F0->F1 ok (+1), F1->F2 ok (+1), F2->F0 wrap ok (+1 mod 3).
    psi = [0] * 24
    for i in range(24):
        psi[cyc[i]] = cyc[(i + 1) % 24]
    return psi

psi = build_U3()
proj = [psi[a] % 3 - a % 3 for a in range(24)]
res["U3_witness"] = {
    "psi": psi,
    "block_advance_const_plus1": all(((a % 3) + 1) % 3 == (psi[a] % 3)
                                     for a in range(24)),
    "single_24_cycle": (lambda p: (lambda n: (lambda s, x, c: c == n)(
        [None for _ in range(n)], 0, 0))(24))(psi),
}
# single-cycle check, plainly:
seen = [False] * 24
x, c = 0, 0
while not seen[x]:
    seen[x] = True
    x = psi[x]
    c += 1
res["U3_witness"]["single_24_cycle"] = (c == 24)

# (c) corrected rigidity: pure odometer tower N=(2,6,24); for k in probes,
# deepest level with phi^k == identity on that quotient.
def odo(N):
    return [(a + 1) % N for a in range(N)]

def compose(p, q):
    return [p[q[i]] for i in range(len(q))]

def power(p, k):
    n = len(p)
    r = list(range(n))
    base = list(p)
    while k:
        if k & 1:
            r = compose(base, r)
        base = compose(base, base)
        k >>= 1
    return r

def fixes_quotient(pk, N, M):
    # pk atom-perm on N atoms; quotient blocks a mod M: fixed pointwise iff
    # pk(a) % M == a % M for all a
    return all(pk[a] % M == a % M for a in range(N))

TOWER = [2, 6, 24]
s = {N: odo(N) for N in TOWER}
rig = {}
for k in [1, 2, 3, 5, 6, 7, 8, 12, 24, 48, 72, 144]:
    pk = power(s[24], k)
    depth = [M for M in TOWER if fixes_quotient(pk, 24, M)]
    rig[k] = {"fixes_quotients": depth,
              "uniform_shadow_le": ("2^-3" if 24 in depth else
                                    "2^-2" if 6 in depth else
                                    "2^-1" if 2 in depth else ">2^-1")}
res["rigidity_corrected"] = rig

# (d) binary odometer single cycles + coherence to level 12
def single(p):
    n = len(p)
    seen = [False] * n
    x, c = 0, 0
    while not seen[x]:
        seen[x] = True
        x = p[x]
        c += 1
    return c == n

sig = {n: odo(2 ** n) for n in range(1, 13)}
res["binary_single"] = {n: single(sig[n]) for n in range(1, 13)}
coh = True
for n in range(1, 12):
    for a in range(2 ** (n + 1)):
        if (sig[n + 1][a] >> 1) != sig[n][a >> 1]:
            coh = False
res["binary_coherent"] = coh

with open(os.path.join(ART, "finite_level_log4.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "pow2_mod3"}, indent=1))
print("pow2_mod3 nonzero for all n<=64:", res["pow2_mod3_all_nonzero"])
