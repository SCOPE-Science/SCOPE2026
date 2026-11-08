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

The standalone verifier `verify.py` enumerates the original induced-degree condition, not the analytical classification. It exhaustively checks \(28\) labeled parameter profiles with \(3\le a\le b\le5\) and \(0\le t\le a\). There are \(11{,}776\) candidate vertex subsets, and the routine finds \(425\) inclusion-maximal faces. For every case, the face polynomial, maximal-face polynomial, and reduced \(\mathbb F_2\)-Betti numbers coincide with the formulas.

Run: `python3 verify.py`.

Expected successful result:
`VERIFY_OK parameter_profiles=28 all_masks=11776 maximal_sets=425 direct_degree_constraint=PASS complete_face_polynomial=PASS facet_polynomial=PASS mod2_homology=PASS`

Finite agreement over \(\mathbb F_2\) is not evidence of a torsion-free infinite-family theorem. The integral and unrestricted assertions follow instead from the explicit suspension and square-collapse proof in `RESULT.md`. No external independent audit has been performed.
