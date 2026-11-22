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

# Verification details
The embedded `verify.py` generates the full set of distinct restrictions of all \(2n\) dihedral permutations to all \(2^n\) domains, deduplicates them as partial-function tuples, and performs every ordered composition for \(n=3,4,5,6,7\). It compares each rank coefficient with independent exact `Fraction` polynomial arithmetic and verifies the count of monoid elements and the exact mean. The corresponding standard output is preserved in `verification_output.txt` and ends with `VERIFY_OK_CYCLE_RESTRICTION_PRODUCT_RANKS`.

The universal product theorem and the Gaussian limit are proved analytically, not inferred by extrapolation from finite cases. The self-review is not independent mathematical certification.
