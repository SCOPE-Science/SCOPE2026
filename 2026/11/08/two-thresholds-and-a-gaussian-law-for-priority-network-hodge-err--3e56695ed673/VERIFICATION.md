---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducing the mathematical checks

Run `python verify.py` with Python 3.10+ and NumPy installed. The program performs three separate classes of tests:

1. Exact rational enumeration of every simple graph on \(2\le n\le5\) vertices, for edge probabilities \(1/4\) and \(2/3\), to compare all five claimed first/second graph-moment formulas; 40 exact equalities are checked.
2. Direct Euclidean least-squares Hodge projection of every two-priority linear-payoff game on every simple graph through four vertices, without using the closed-form energy ratio during projection; 74 graph instances are checked.
3. Seeded Erdős–Rényi Monte Carlo samples at \(n=700\), for mean degrees \(0.7\) and \(1.8\), comparing observed centered rescaled variance with the derived Gaussian coefficient. These are approximate diagnostics only.

A successful execution prints:

```
Exact graph-moment equalities: 40
Direct Hodge least-squares graphs: 74
Gaussian-scale variance check: 0.7 0.063343 0.063977
Gaussian-scale variance check: 1.8 0.024386 0.026857
PASS
```

The rational enumerations and least-squares projections validate identities only for the indicated finite cases; no finite verification replaces the infinite-limit cumulant and concentration proofs in `RESULT.md`. The Monte Carlo comparison is intentionally given a tolerance to allow random sampling variability and is not a mathematical certificate. The proof's dependency-cumulant bound, Gaussian centering and zero-edge convention should be inspected directly.
