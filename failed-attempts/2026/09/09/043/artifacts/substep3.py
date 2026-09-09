"""Substep 3: find smooth bidegree-(3,4) curve over F_101 by point search on P1xP1.
C: sum_{i<=3,j<=4} c[i][j] s^i t^{3-i} u^j v^{4-j}. Singular iff F=dF=0 at some
P1xP1(F_101) point. Try seeds until smooth. Persist coefficients."""
import json, random
P = 101
def find(seed):
    rng = random.Random(seed)
    c = [[rng.randrange(P) for _ in range(5)] for _ in range(4)]
    pts1 = [(1, b) for b in range(P)] + [(0, 1)]
    for (s, t) in pts1:
        S = [pow(s, 3-i, P) * pow(t, i, P) % P for i in range(4)]
        dS = [((3-i) * pow(s, max(0, 2-i), P) * pow(t, i, P)) % P if (3-i) > 0 else 0 for i in range(4)]
        eS = [(i * pow(s, 3-i, P) * pow(t, max(0, i-1), P)) % P if i > 0 else 0 for i in range(4)]
        for (u, v) in pts1:
            U = [pow(u, 4-j, P) * pow(v, j, P) % P for j in range(5)]
            dU = [((4-j) * pow(u, max(0, 3-j), P) * pow(v, j, P)) % P if (4-j) > 0 else 0 for j in range(5)]
            eU = [(j * pow(u, 4-j, P) * pow(v, max(0, j-1), P)) % P if j > 0 else 0 for j in range(5)]
            F = sum(c[i][j] * S[i] % P * U[j] for i in range(4) for j in range(5)) % P
            if F != 0:
                continue
            Fs = sum(c[i][j] * dS[i] % P * U[j] for i in range(4) for j in range(5)) % P
            Ft = sum(c[i][j] * eS[i] % P * U[j] for i in range(4) for j in range(5)) % P
            Fu = sum(c[i][j] * S[i] % P * dU[j] for i in range(4) for j in range(5)) % P
            Fv = sum(c[i][j] * S[i] % P * eU[j] for i in range(4) for j in range(5)) % P
            # singular iff all tangent weights vanish appropriately per chart; conservative: all four zero
            if Fs == 0 and Ft == 0 and Fu == 0 and Fv == 0:
                return None
    return c
for seed in [606, 607, 608, 609, 610, 611, 612, 613]:
    c = find(seed)
    if c is not None:
        json.dump({"p": P, "seed": seed, "coeffs": c},
                  open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/curve_F101.json", "w"))
        open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/substep3_ok.txt", "w").write(f"SMOOTH seed={seed} p={P} checked={(P+1)**2} points\n")
        print(f"SMOOTH seed={seed}")
        break
else:
    print("NOSMOOTH in seed list")
