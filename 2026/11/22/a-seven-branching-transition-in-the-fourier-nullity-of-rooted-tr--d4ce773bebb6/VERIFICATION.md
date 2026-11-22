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

Verification uses the standalone `verify_walsh.py` and `verify_bernstein.py` files. The first enumerates all binary configurations on full rooted trees of up to fifteen vertices, tests the order-ideal predicate, performs the integer Walsh transform, and compares zero and unit-coefficient counts with independently computed structural recurrences. The second constructs exact rational Bernstein coefficients of the five finite positivity polynomials for \(d=2,3,4,5,6\), checks all entries are positive with the stated exact minima, and checks the rational witness at the integer branching threshold \(d=7\). The symbolic certificate uses SymPy; no floating-point computation establishes a mathematical inequality. The remaining steps are proved analytically in `RESULT.md`; finite tests are corroborative and not a substitute for proof.

Independent external review has not been performed. The Fourier result is not a statement about general trees or hard-core Gibbs mixing times.
