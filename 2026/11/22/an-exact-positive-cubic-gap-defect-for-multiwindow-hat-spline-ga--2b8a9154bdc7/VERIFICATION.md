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

Run `python3 checker.py` from the same directory. The exact-rational tests cover 4,134 finite shift multisets on grids of denominators 4, 6 and 8 for each of 1 through 6 windows. The checker reports 143 equality configurations, 324 all-distinct gap inequality tests and exact multiplier/frame-criterion tests. All passed.

This code confirms illustrative finite configurations, not all real offsets. The full proof uses Zak diagonalization, a quadratic integration identity valid for arbitrary gap lengths, a cubic polynomial identity, and derivative jumps for equality. It does not rely on a finite grid as a surrogate for the continuous quantifier.

The unweighted equally spaced global optimizer is known from circle polarization; the newly asserted content is the exact nonnegative identity and the multiplicity-sensitive equality law. Equivalent earlier work cannot be categorically excluded by the literature searches. Independent audit has not been performed.
