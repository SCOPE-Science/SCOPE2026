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

The exact polynomial factorization used to prove \(F_a(\delta)\ge2-a^2\) was verified by bivariate integer-coefficient polynomial arithmetic. The checker additionally tests rational nonnegativity on the full permitted grid, verifies unit-diagonal identities of the equality family, and independently computes candidate circle intersections and polygon half-plane containment across a deterministic numerical parameter sweep. Executing `python3 verify.py` with Python 3 standard library passed 8,204 assertions in the packaged version.

The proof itself is the universal algebraic factorization and geometric containment argument in `RESULT.md`; the finite checks cannot establish an infinite-parametric theorem independently. The sharp witness lies on polygon vertices, which the stated closed-polygon definition permits. Priority outside the inspected published sources remains unverified. Independent mathematical audit was not performed.
