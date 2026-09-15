"""Bounded recovery probe: thin-shell psi1 vs psi1/2 on symmetric isotropic models."""
import numpy as np, json

rng = np.random.default_rng(0)

def sample(model, n, N):
    if model == "gauss":
        return rng.standard_normal((N, n))
    if model == "cube":
        return rng.uniform(-np.sqrt(3), np.sqrt(3), size=(N, n))
    if model == "laplace":
        return rng.laplace(0.0, 1.0 / np.sqrt(2.0), size=(N, n))
    raise ValueError(model)

out = {}
for model in ["gauss", "cube", "laplace"]:
    for n in [20, 100]:
        N = 120000 if n == 20 else 40000
        X = sample(model, n, N)
        R = np.linalg.norm(X, axis=1)
        m = float(R.mean())
        Z = np.abs(R - m)
        var = float(Z.var())
        Mp = {}
        for p in [1, 2, 4, 6, 8]:
            mp = float((Z ** p).mean() ** (1.0 / p))
            Mp[str(p)] = {
                "Mp": round(mp, 4),
                "Mp_over_p": round(mp / p, 4),
                "Mp_over_p2": round(mp / p ** 2, 4),
            }
        tails = {}
        for t in [3.0, 5.0]:
            tails[str(t)] = round(float((Z >= t).mean()), 6)
        out[f"{model}_n{n}"] = {"mean": round(m, 3), "var": round(var, 4),
                                "moments": Mp, "tails": tails, "N": N}
        print(f"{model} n={n}: mean={m:.2f} var={var:.3f} tails={tails}")
        for p, d in Mp.items():
            print(f"   p={p}: Mp={d['Mp']} Mp/p={d['Mp_over_p']} Mp/p^2={d['Mp_over_p2']}")

with open("output/artifacts/thin_shell_psi1_probe.json", "w") as f:
    json.dump(out, f, indent=1)
print("wrote output/artifacts/thin_shell_psi1_probe.json")
