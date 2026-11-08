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

# Verification of the noncentral regular-simplex face-vector theorem

`verify.py` uses the Python standard library only. Run it with `python verify.py` in a directory containing this file and `RESULT.md`. A successful run ends with `ALL_NONCENTRAL_SIMPLEX_SECTION_CHECKS_PASSED`.

## Checks performed

The verifier enumerates all sign configurations for \(4\le n\le8\), compares face counts with a direct enumeration of mixed-sign subsets of size \(j+2\), and tests that the balanced split maximizes each face count. It checks the exact vertex identity \(F_{n,0}=K(n-K)\). It generates independent Gaussian samples and normalizes their centered coordinates to obtain Haar directions, using the same sample standard deviation in the threshold.

At sample size \(n=800\) and 3,600 seeded replicates per setting, it checks the limiting imbalance mean and variance at centroid offsets zero and \(1.5/n\), and the corrected fixed-scaled-offset variance at \(0.85/\sqrt n\). It checks polynomial quadratic coefficients for face ranks zero through four. The random seed is fixed to permit replay.

## Mathematical and computational limits

The finite enumerations are exact only for the listed small dimensions. Monte Carlo tolerances are deliberately wider than finite-sample bias and sampling error; they are consistency checks rather than confidence guarantees or exact evaluations of a probability law. Equations (4)–(12) and the accompanying empirical-process lemma in `RESULT.md` establish the infinite-dimensional claims. No independent mathematical audit, external certification or formal proof-assistant project has been performed.
