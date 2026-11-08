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

The proof in `RESULT.md` is an exact all-depth construction: a finite affine nesting orbit is separated before local piecewise-linear slopes are imposed; the prescribed values are unchanged, and all nonstandard estimates are explicit. The global bound on the autonomous relay reference solution verifies the strict amplitude assumption needed to invoke the source's invisibility theorem. The resulting nested delayed-argument derivative is \(1-\sum_{k=1}^{i-1}q^k\), constant on an actual interval. No finite enumeration is used as an infinite proof.

Run the standalone standard-library checker with `python verify.py`. It verifies the exact rational construction, breakpoints, history bounds, nesting values and delayed-argument derivatives at representative depths, producing:

`VERIFY_OK exact_rational_checks=345 witness_depths=3..7 additional_below_threshold=3..8`

The irrational equality \(q=\nu_i\) is handled directly by the algebraic defining identity; finite rational tests check examples strictly above and below. The verification does not establish any independent scientific audit or historical priority. The result does not infer behavior of arbitrary histories above the universal bound.
