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

# Verification record

From the extracted package folder run `python3 verify.py`, using the Python 3 standard library. Recorded output in `verification.log`: `VERIFY_OK trees=629 exact_vertex_pairs=16090`.

Checks: exact rational multiplication of signless Laplacian powers; edge \(B^3\) and \(B^4\) walk identities; the strict edge inequality \(c^2<2sb\); distance-two and distance-three entry coefficients; distance-four positivity and no off-diagonal entries beyond graph distance four. Generated trees and weights test only a finite sample. The continuous-weight, all-size and no-reentry claims are proved analytically in `RESULT.md`; code output alone cannot certify them.

Independent audit and external validation are not performed.
