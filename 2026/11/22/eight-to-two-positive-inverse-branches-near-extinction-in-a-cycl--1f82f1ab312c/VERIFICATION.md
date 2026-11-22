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

# Reproducibility

Execute `python3 CHECK.py` with Python 3.9 or later; no third-party packages are needed. The checker builds three exact rational zero fibers, verifies each point maps exactly to zero, tests nonvanishing exact Jacobian determinants and missing-coordinate multiplier identities, then uses Newton's method only as a finite small-target diagnostic. It also checks the exact two-root formula at the equal-interaction point.

The theorem's uniform local inverse count follows instead from the exact support decomposition, nonzero Jacobian determinants, the inverse-function theorem, and compactness of the strictly positive inverse domain near zero. The numerical trial is explicitly not a proof of the quantifier over all small targets. Scope excludes one coefficient exactly one while the other differs, general nonpositive inputs, nonsmall outputs and global dynamical classifications. Independent audit: not performed.
