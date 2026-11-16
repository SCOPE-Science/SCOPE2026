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

# Verification of the coefficient extremum

The analytical proof is in `RESULT.md`. The standard-library-only `CHECK.py` recomputes rational algebraic identities for sample \(t\), exact endpoint signs, numerical bracketing of the unique positive quartic root, and a deterministic grid of positive-coefficient challengers. The resulting norm agrees with explicit low-exponent examples. Because the calculations check only finitely many parameters, the arguments establishing uniqueness for all real \(t>2\), global maximality, and the infinite-dimensional reduction are the analytical proofs, not these runs.

**External scientific validation:** Not performed. Numerical checks are supplemental; in particular they cannot independently establish the outer-extremizer premise or search completeness of prior literature.
