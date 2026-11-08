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

Run the provided standard-library script with `python3 verify_fano_lines.py`. The code enumerates reduced row-echelon representatives of all two-dimensional vector subspaces of four-dimensional space over \(\mathbb F_2\) and \(\mathbb F_4\), checking the four coefficients of the restricted cubic. It confirms 15 lines over \(\mathbb F_2\) and 27 over \(\mathbb F_4\).

The explicit \(\mathbb F_{256}\) witness uses polynomial representation modulo binary polynomial `0x11b`; all field multiplications and powers are exact. The affine point \((1,2,4,179)\) lies on the cubic surface, has tangent-space quadratic coefficients \((157,67)\), and the unique quadratic-root slope `151` gives cubic value `48` (nonzero). Thus the quadratic and cubic defining a ruling transverse fiber have no common nonzero zero at that sample. The formal Hilbert-series calculation for a bidegree \((2,3)\) regular sequence yields length six.

The script's independently reproduced output is contained in `verification_output.txt` and ends in `ALL_CHECKS_PASSED`. The general irreducible-support classification, local complete-intersection argument, generic reducedness of planar components, and the passage from a witness to a nonempty Zariski-open locus are proved mathematically in `RESULT.md`; finite-field calculations alone cannot prove these statements. The completed scheme at component intersections was not computed.
