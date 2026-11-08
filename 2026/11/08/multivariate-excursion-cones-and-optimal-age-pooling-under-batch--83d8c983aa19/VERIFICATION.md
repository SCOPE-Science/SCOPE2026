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

# Verification and reproducibility

The analytical proof in `RESULT.md` establishes the stationary process, exact tagged-age survival, matching local exponential bounds, conditional Gaussian Laplace principle, strictly convex age minimization and optimal isotonic pooling. The proof explicitly limits the observed set to \(3\le k\le N-m+1\). The sharp angular nonsmoothness is verified by adjacent analytic branches and their derivatives.

From the directory containing the embedded files, run:

```shell
python3 verify.py
```

The standard-library verifier enumerates finite marked-subset hazards and checks the exact increment identity, certifies the four exhibited pooling partitions, tests KKT stationarity and multiplier signs, checks the equal-threshold formula, and compares the computed value with many randomly perturbed feasible ages. A completed execution produced:

```text
PASS 29382 deterministic tests (combinatorial hazards, four regimes, KKT, convex samples, equal-level law)
The logarithmic LDP and non-C2 claims require the written proof.
```

A separate SciPy SLSQP minimization, not required to run the standalone verifier, agreed with the analytical PAV optimum on 1,500 random independent convex programs and 7,500 additional feasible-age perturbations. These finite computations cannot prove uniqueness for all parameters or the infinite-threshold limit. No external formal proof certificate, experimental dataset or independent scientific audit is claimed.
