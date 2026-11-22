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

# Verification notes

The accompanying `check_spectra.py` implements direct quaternion geometry, independent symmetric-power representations of \(SU(2)\), and numerical Gram eigenvalue checks. Run it with Python 3 and NumPy using `python3 check_spectra.py`. On the reviewed executable: the two six-point classes had the same pairwise relative rotation traces, projective lift spans of dimensions four and three, and independently assembled representation matrices matching the character Gram formulas in degrees one through six. A separate finite scan checked degrees one through 10,000, and 1,000 positive-weight trials checked the symmetrization inequality numerically.

The finite checker is corroboration, not an infinite-degree proof. The character formula, six-residue exact inequalities, projective span argument, and symmetry averaging establish the universal statements in the written proof. The conclusion excludes mixed-degree recovery and does not establish bibliographic uniqueness; independent audit has not been performed.
