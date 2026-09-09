"""Lane-403 attack v5: fix quotient convention (mod, not >>) + genuine U3 witness."""
import json, os

ART = os.path.dirname(os.path.abspath(__file__))
res = {}

# genuine U3 witness: B_j = {a : a%3==j}; +1 advance; psi^3 = 8-cycle on F0
F = [[a for a in range(24) if a % 3 == j] for j in range(3)]
psi = [0] * 24
for i in range(8):
    psi[F[0][i]] = F[1][i]
    psi[F[1][i]] = F[2][i]
    psi[F[2][i]] = F[0][(i + 1) % 8]
assert sorted(psi) == list(range(24))
assert all((psi[a] % 3) == (a % 3 + 1) % 3 for a in range(24))
seen = [False] * 24
x, c = 0, 0
while not seen[x]:
    seen[x] = True
    x = psi[x]
    c += 1
res["U3_witness"] = {"psi": psi, "advance_plus1": True, "single_24_cycle": c == 24}

# binary odometer coherence under mod-quotient
def odo(N):
    return [(a + 1) % N for a in range(N)]

coh = True
for n in range(1, 12):
    s1, s0 = odo(2 ** (n + 1)), odo(2 ** n)
    for a in range(2 ** (n + 1)):
        if (s1[a] % (2 ** n)) != s0[a % (2 ** n)]:
            coh = False
res["binary_coherent_mod"] = coh

with open(os.path.join(ART, "finite_level_log5.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1)[:800])
print("U3 ok:", res["U3_witness"]["single_24_cycle"], "coh:", coh)
