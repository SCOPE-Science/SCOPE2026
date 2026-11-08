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

# Verification

The analytical proof uses the monomial action of \(A_{z^k}^{z^N}\), the nilpotence \(QU=0\), and a quotient computation with independent coefficients. These steps hold for every integer \(n\geq1\).

The supplied `verify_defect.py` builds exact integer matrices in SymPy and checks eight independently instantiated cases, \(n=1,2,\ldots,8\). It checks the perturbation's rank, inverse factors, kernel identity and dimension, zero constant terms, and the quotient's exact rank. Its successful run prints `TRUNCATED_TOEPLITZ_SHARP_DEFECT_EXACT_OK 8`.

Finite checks corroborate the symbolic construction only; they do not prove the theorem for arbitrary \(n\). The analytical proof supplies that quantifier. The general upper bound is credited to the cited 2026 theorem, and the new proof supplies matching examples and intrinsic lower bounds. No independent audit has been performed.
