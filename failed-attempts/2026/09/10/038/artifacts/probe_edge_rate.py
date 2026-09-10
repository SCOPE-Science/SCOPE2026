"""Bounded recovery probe: iid-uniform vs Ginibre edge linear statistic.

Statistic: L = sum_i phi(sqrt(n)(|lam_i|-1)), phi(u)=exp(-u^2/2).
Reports per-n means, relative discrepancy D(n)=|mean_iid-mean_gin|/mean_gin,
with standard errors, plus a log-log slope fit (exponent estimate with SE).
Fixed seed. Writes results JSON next to this script. stdlib+numpy only.
"""
import json
import math
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

def ginibre(n, rng):
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0 * n)
    return Z

def iid_uniform(n, rng):
    # centred, Var|entry|^2 = 1/n, bounded density, symmetric (0 third moment).
    # Re,Im iid Uniform[-a,a], a^2/3 = 1/(2n).
    a = math.sqrt(3.0 / (2.0 * n))
    Zr = rng.uniform(-a, a, size=(n, n))
    Zi = rng.uniform(-a, a, size=(n, n))
    return Zr + 1j * Zi

def edge_stat(vals, n):
    r = np.abs(vals)
    u = math.sqrt(n) * (r - 1.0)
    return float(np.sum(np.exp(-0.5 * u * u)))

def run_case(n, trials, seed):
    rng = np.random.default_rng(seed)
    Lg, Lu = [], []
    for _ in range(trials):
        Lg.append(edge_stat(np.linalg.eigvals(ginibre(n, rng)), n))
        Lu.append(edge_stat(np.linalg.eigvals(iid_uniform(n, rng)), n))
    Lg = np.array(Lg)
    Lu = np.array(Lu)
    mg, sg = float(Lg.mean()), float(Lg.std(ddof=1) / math.sqrt(trials))
    mu, su = float(Lu.mean()), float(Lu.std(ddof=1) / math.sqrt(trials))
    D = abs(mu - mg) / mg if mg else float("nan")
    sD = math.sqrt(su**2 + sg**2) / mg if mg else float("nan")
    return {"n": n, "trials": trials, "mean_gin": mg, "se_gin": sg,
            "mean_iid": mu, "se_iid": su, "D": D, "se_D": sD}

def main():
    t0 = time.time()
    ns = [64, 128, 256]
    trials = 24
    out = [run_case(n, trials, seed=605000 + n) for n in ns]
    # log-log slope of D vs n with inverse-variance-ish weighting (delta method on log)
    xs = np.array([math.log(o["n"]) for o in out])
    ys = np.array([math.log(o["D"]) if o["D"] > 0 else float("nan") for o in out])
    w = np.array([1.0 / max((o["se_D"] / max(o["D"], 1e-12)) ** 2, 1e-12) for o in out])
    ok = np.isfinite(ys)
    slope = float("nan")
    se_slope = float("nan")
    if ok.sum() >= 2:
        X = np.column_stack([np.ones(ok.sum()), xs[ok]])
        W = np.diag(w[ok])
        XtW = X.T @ W
        try:
            beta = np.linalg.solve(XtW @ X, XtW @ ys[ok])
            resid = ys[ok] - X @ beta
            dof = max(ok.sum() - 2, 1)
            cov = np.linalg.inv(XtW @ X) * float((resid ** 2).sum() / dof)
            slope, se_slope = float(beta[1]), float(math.sqrt(max(cov[1, 1], 0)))
        except np.linalg.LinAlgError:
            pass
    res = {"rows": out, "loglog_slope": slope, "se_slope": se_slope,
           "target_delta": 1 / 24, "elapsed_s": time.time() - t0,
           "note": ("slope<0 means decay; certifying delta>=1/24 needs slope<=-1/24 "
                    "with CI excluding 0 and D>>noise; check rows for monotonicity.")}
    with open(os.path.join(HERE, "probe_edge_rate_results.json"), "w") as f:
        json.dump(res, f, indent=2)
    for o in out:
        print(o)
    print({"loglog_slope": slope, "se_slope": se_slope,
           "elapsed_s": res["elapsed_s"]})

if __name__ == "__main__":
    main()
