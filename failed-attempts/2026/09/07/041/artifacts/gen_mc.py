import numpy as np, json, time
N, n, p = 160, 80, 0.2
seed = 20260907
T = 2000
rng = np.random.default_rng(seed)
smins = np.empty(T)
t0 = time.time()
for i in range(T):
    B = (rng.random((N, n)) < p).astype(float)
    R = rng.choice(np.array([-1.0, 1.0]), size=(N, n))
    Y = B * R / np.sqrt(p)
    smins[i] = np.linalg.svd(Y, compute_uv=False)[-1]
q = {f"q{pct}": float(np.quantile(smins, pct / 100)) for pct in [1, 5, 10, 25, 50, 75, 90, 99]}
hist, edges = np.histogram(smins, bins=20)
np.savetxt("output/artifacts/smins_seed20260907_T2000.csv", smins, delimiter=",")
json.dump({"seed": seed, "T": T, "N": N, "n": n, "p": p,
           "mean": float(smins.mean()), "sd": float(smins.std(ddof=1)),
           "min": float(smins.min()), "max": float(smins.max()),
           "quantiles": q,
           "freq_le_2_0": int((smins <= 2.0).sum()),
           "freq_le_1_5": int((smins <= 1.5).sum()),
           "CP95_upper_0events": 1 - 0.05 ** (1.0 / T),
           "hist_counts": hist.tolist(), "hist_edges": edges.tolist(),
           "elapsed_s": time.time() - t0},
          open("output/artifacts/mc_summary.json", "w"), indent=1)
print("mean", float(smins.mean()), "sd", float(smins.std()),
      "min", float(smins.min()), "max", float(smins.max()))
print("q05", q["q5"], "median", q["q50"])
print("freq<=2.0", int((smins <= 2.0).sum()), "freq<=1.5", int((smins <= 1.5).sum()))
