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

The proof reconstructs the Hermitian-line restriction, the descent of each Frobenius triple to a nondegenerate plane, the cyclic Gram matrix, norm normalization, the exact projective stabilizer and the smooth-section cardinality. No computational step is used as a proof over all finite fields.

`verify.py` is a standalone Python-standard-library enumeration of the \(q=2\) specialization, using \(\mathbb F_{64}=\mathbb F_2[z]/(z^6+z+1)\), with \(\mathbb F_4\) its fixed field under the fourth power. Every normalized point of the Hermitian surface is listed; each triple rank is computed by elementary elimination. For each rank-three point all \(85\) rational planes are tested. It asserts that there are \(4545\) surface points, \(45\) rank-one points, \(1620\) rank-two points and \(2880\) rank-three points, and that the latter lie uniquely on \(40\) non-tangent planes with \(72\) points per plane.

Run from the extracted package directory with `python3 verify.py`. The exhaustive test is over a single small field and neither certifies historical novelty nor replaces the proof in `RESULT.md`.
