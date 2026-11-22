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

The file `pgl2_dual_check.py` uses only standard Python and is executable with `python pgl2_dual_check.py`. It constructs \(\operatorname{PGL}_2(\mathbb F_q)\) directly as scalar-normalized invertible matrices and the additive trace-zero kernel, for \(q=3\) and \(q=5\). It independently enumerates the possible involution lifts, verifies projective commutation for each pair, checks both expected degree multiplicities and the exact ordered-pair count, and confirms every edge has exactly one common neighbor. It reports the final marker `PGL2_DUAL_INVOLUTION_CHECKS_PASSED`.

Observed: for \(q=3\), \(81\) vertices, degree counts \(54\) of degree \(6\), \(27\) of degree \(12\), \(729\) ordered commuting pairs and \(108\) triangles; for \(q=5\), \(625\) vertices, degree counts \(375\) of degree \(20\), \(250\) of degree \(30\), \(15,625\) ordered commuting pairs and \(2,500\) triangles. The proof in `RESULT.md` is symbolic for arbitrary odd prime-power \(q\). A finite script cannot establish the arbitrary-field statement or historical novelty.
