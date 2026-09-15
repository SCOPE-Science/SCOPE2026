"""Rauzy-Veech staged-construction tension probe (d=5, target-only lane).

Implements combinatorial Rauzy induction, generates:
 (1) balanced/freedom paths (alternating Rauzy types),
 (2) restriction-like runs (long same-type runs forcing eigenvalue alignment),
and measures matrix norm growth, column distortion (illumination proxy),
and simplex-diameter proxy. Demonstrates the freedom-vs-control tension
blocking the claimed unconditional lower bound HDim >= d-3/2.
"""
import random
import numpy as np

TOP0 = [0, 1, 2, 3, 4]
BOT0 = [4, 0, 2, 1, 3]  # irreducible, not a rotation, non-hyperelliptic candidate
D = 5


def rauzy_step(top, bot, typ):
    """typ=0 top wins, typ=1 bottom wins. Returns (new_top, new_bot, winner, loser)."""
    top = list(top); bot = list(bot)
    a = top[-1]; c = bot[-1]
    if typ == 0:
        w, l = a, c
        bot.remove(c)
        bot.insert(bot.index(a) + 1, c)
    else:
        w, l = c, a
        top.remove(a)
        top.insert(top.index(c) + 1, a)
    return top, bot, w, l


def run_path(types):
    top, bot = list(TOP0), list(BOT0)
    M = np.eye(D)
    for t in types:
        top, bot, w, l = rauzy_step(top, bot, t)
        E = np.eye(D); E[w, l] += 1.0
        M = M @ E
    return M


def stats(M):
    col = M.sum(axis=0)
    ncol = M / col
    # diameter proxy: max L1 distance between normalized columns
    diam = max(np.abs(ncol[:, i] - ncol[:, j]).sum()
               for i in range(D) for j in range(D))
    distortion = col.max() / col.min()
    return float(np.linalg.norm(M, 2)), float(distortion), float(diam)


def experiment(seed=0):
    rng = random.Random(seed)
    out = {}
    # (1) freedom-like: random balanced paths of length n
    for n in [20, 60, 200]:
        rows = []
        for trial in range(30):
            types = [rng.choice([0, 1]) for _ in range(n)]
            rows.append(stats(run_path(types)))
        arr = np.array(rows)
        out[f"balanced_n{n}"] = {
            "mean_log_norm": float(np.log(arr[:, 0]).mean()),
            "mean_distortion": float(arr[:, 1].mean()),
            "mean_diameter": float(arr[:, 2].mean()),
        }
    # (2) restriction-like: same-type runs of length L (force thin direction)
    for L in [5, 10, 20, 40]:
        M = run_path([0] * L)
        nrm, dist, diam = stats(M)
        out[f"restrict_run_L{L}"] = {
            "log_norm": float(np.log(nrm)),
            "distortion": dist,
            "diameter": diam,
        }
    # (3) staged alternation: freedom block of length F then restriction R
    for F, R in [(30, 5), (30, 15), (60, 30)]:
        types = [rng.choice([0, 1]) for _ in range(F)] + [0] * R
        nrm, dist, diam = stats(run_path(types))
        out[f"staged_F{F}_R{R}"] = {
            "log_norm": float(np.log(nrm)),
            "distortion": dist,
            "diameter": diam,
        }
    return out


if __name__ == "__main__":
    import json
    res = experiment()
    print(json.dumps(res, indent=1))
    with open("results.json", "w") as f:
        json.dump(res, f, indent=1)
