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

The result is supported by a proof for every integer \(n\ge2\), not solely by finite enumeration. Run the included standard-library-only script with `python3 verify_affine_queens.py`. Its three logically distinct checks are: exact rational incidence multiplicities for the 12-line arrangement; full comparison with queen-line attacks for all slopes on the six moduli \(2,3,5,7,11,13\); and exhaustive modular-slope census versus the product expression at twelve test moduli through \(143\).

Observed replay result: `RATIONAL_ARRANGEMENT 12 lines 21 points 5x4 4x3 12x2 PASS`, followed by all twelve modulus comparisons and `VERIFY_OK`. The check does not enumerate nonaffine placements, establish literature priority, or constitute an independent mathematical audit.
