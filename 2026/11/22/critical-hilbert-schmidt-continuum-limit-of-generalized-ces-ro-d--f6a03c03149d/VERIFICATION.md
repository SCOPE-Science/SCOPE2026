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

# Reproducibility and limits

The accompanying `check.py` uses only Python's standard library. Execute `python check.py` from the directory containing the two files. It verifies 288 finite Hilbert–Schmidt Gram identities exactly using rational arithmetic, three numerical Frullani-kernel integrals, and nine comparisons of finite-parameter Gram sums with the limiting logarithmic formula. The finite sums have explicitly bounded missing positive tails, although cancellation makes their measured errors much smaller. The checker is supplementary evidence for algebra and normalization only; it does not certify convergence over infinitely many indices.

The analytic proof in `RESULT.md` establishes Hilbert–Schmidt convergence using the exact Gram identity, the Frullani computation, almost-everywhere convergence of step kernels, weak-plus-norm convergence in \(L^2\), and the singular-value perturbation inequality. All limits require fixed positive rates; no claim is made about rate sequences depending on mesh or individual closed-form limit singular values. Independent audit status: not performed.
