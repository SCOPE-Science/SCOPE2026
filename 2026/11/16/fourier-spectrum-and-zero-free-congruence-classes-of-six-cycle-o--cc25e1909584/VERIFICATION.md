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

# Reproducibility
Run `python check_sixcycle.py` using Python 3 (standard library only). The program constructs all six-cycle incidence masks directly, executes an integer Walsh–Hadamard transform, and checks every frequency for \(3\le n\le6\). Separately the exact multinomial summation verifies Parseval, the two congruence classes, exact endpoint norms, and zero fractions through \(n=70\).

The checker has been executed from the embedded source file and its test output matches all claimed finite values. The analytic Gaussian limiting claim is established in `RESULT.md` by the multivariate central limit theorem and uniform integrability, **not** by extrapolation from tests. Independently audited evidence is not available.
