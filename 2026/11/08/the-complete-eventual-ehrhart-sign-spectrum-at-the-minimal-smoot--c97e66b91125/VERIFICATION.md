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

# Verification of the eventual sign classification

The standalone file `verify_signs.py` uses Python 3 standard-library exact rational arithmetic. It computes coefficient polynomials in the integer twist parameter by applying Newton interpolation in the dilation variable to the lattice-height binomial sum. It then checks the two leading-twist coefficient identities, their signs and degrees for every \(r\) from 4 through 12, the proposed complete sign patterns, consistency with integer-height lattice counts at several twist/dilation inputs, and recursive enumeration at small parameters. It passed 518 exact checks on the package file.

The proof in `RESULT.md` shows why the conclusions apply to all integers \(r\ge4\); finite verification cannot prove that extension. The least admissible twist is not computed. Mathematical correctness and historical priority have not received an independent audit.
