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

## Reproducibility

The analytic proof is self-contained in `RESULT.md`. Run `python checker.py` in an environment with Python 3, NumPy and SciPy to replay 64 numerical checks of the exact one-pair distribution, seven parameter-specific two-sided tail constants, and fixed-three-point spherical sampling. The simulation seed is specified in the code. A run reports `PASS 64 checks`.

The numerical work is not an infinite-threshold proof. The theorem relies on the exact spherical dot-product density, pairwise independence of distinct pair angles by conditional rotation invariance, and a finite-sum one-large-pair argument; no numerical exploration is used as a substitute for these steps.

## Scientific limits

The constants apply to deterministic \(a\in[-1,1]\), fixed \(n\ge2\), iid uniform observations on \(\mathbb S^2\), and the exact \(2/n\) centering. A mixed growing-sample/large-threshold limit and finite-quantile approximation error are not supplied. Independent audit has not been performed.
