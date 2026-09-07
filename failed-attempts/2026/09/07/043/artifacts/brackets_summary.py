"""Summary: margins vs 12/60 curves, effective constant, lower-bound sanity,
grid-lower cross-check at large N (independent code path, must sit <= exact)."""
import numpy as np
import json, csv

ART = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-78/output/artifacts/"
tab = json.load(open(ART + "dem_table.json"))
A1F = float(np.cbrt(2.0) - 1.0)
A2F = float(np.cbrt(4.0) - 1.0)


def grid_lower(xs, ys, G=256):
    N = len(xs)
    X = np.sort(xs)
    g = np.arange(1, G) / G
    best = 0.0
    invN = 1.0 / N
    for a in g:
        sub = np.sort(ys[xs < a])
        c = np.searchsorted(sub, g, side="left")
        best = max(best, float(np.abs(c * invN - a * g).max()))
    return best


rows = []
Chat = 0.0
for Ns, r in sorted(tab.items(), key=lambda kv: int(kv[0])):
    N = int(Ns)
    D = r["D"]
    ln = np.log(N)
    b12 = 12 * ln * ln / N
    b60 = 60 * ln * ln / N
    chat = N * D / (ln * ln)
    Chat = max(Chat, chat)
    nd = N * D
    lb = N / (2 * (N + 1))  # projection-lemma threshold for N*D
    rows.append([N, D, b12, b12 - D, b60, chat, nd])
    print(f"N={N:6d} D={D:.9f} 12-curve={b12:.6f} margin={b12-D:.6f} "
          f"Chat={chat:.4f} N*D={nd:.4f}(>={lb:.4f}) 60-curve={b60:.6f}")
    assert D < b12 and D < b60 and nd >= lb - 1e-9
print("effective C_hat (exact checkpoints) =", Chat)
assert Chat <= 8, "target-curve fit exceeded!"

for Nc in (16384, 20000):
    n = np.arange(1, Nc + 1)
    xs, ys = np.mod(n * A1F, 1.0), np.mod(n * A2F, 1.0)
    gl = grid_lower(xs, ys)
    print(f"N={Nc}: grid-lower={gl:.9f} <= exact={tab[str(Nc)]['D']:.9f} "
          f"(ratio {gl/tab[str(Nc)]['D']:.3f})")
    assert gl <= tab[str(Nc)]["D"] + 1e-12

with open(ART + "summary.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["N", "D_exact", "bound12", "margin12", "bound60", "C_hat_N", "N_times_D"])
    w.writerows(rows)
print("wrote summary.csv; ALL CHECKS PASSED")
