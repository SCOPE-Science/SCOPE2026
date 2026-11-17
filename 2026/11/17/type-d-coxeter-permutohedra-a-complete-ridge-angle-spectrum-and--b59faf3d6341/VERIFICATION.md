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

The accompanying `check_type_d.py` performs exact finite reconstruction of the fan rays and their two-dimensional cone pairs, for \(n=4,5,6\). Each actual pair is obtained by even-signed permutations of doubled fundamental weights and deduplicated as an unordered pair of integral rays. Rational squared cosines are computed from integer Gram products and compared with the complete formula's multiplicity histogram; all tested cases pass.

Closed-form multiplicity and mean-angle identities are independently evaluated for additional ranks, with relative numerical tolerance on floating angles. General all-rank coverage and the exact mean formula rest on the algebraic argument in `RESULT.md`, not on a finite test or a numerical approximation. Reproduce with `python3 check_type_d.py` from the directory containing this file; Python standard library only. No external independent audit is claimed.
