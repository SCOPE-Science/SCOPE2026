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

# Reproducibility and verification

Run `python3 checker.py` with Python's standard library. The script uses exact integer and rational arithmetic, constructs and inverts the four-vertex matrix, verifies all eight normalized-volume determinant identities and the exact Ehrhart numerator by independently enumerating lattice points in each of 24 integer dilations (weights two to nine, dilations one to three). It also checks interior counts and the stated root and coefficient criteria.

The observed execution exited successfully and printed `PASS: 8 exact determinants and inverses; 24 complete dilation counts; interior lattice-point counts, Ehrhart h* formula and thresholds.`

The universal proof requires neither finite extrapolation nor an external computer certificate. The positive coefficient polynomial identities and the four negative cubic discriminants may be checked algebraically independently. No independent mathematical audit has been performed. Claims are restricted to uniform positive integer weights at least two and the specified directed four-cycle simplex.
