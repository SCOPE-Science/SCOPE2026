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

# Verification and reproducibility

Run the embedded `verify_high_girth_prism.py` with Python 3 (standard library only). The verifier independently enumerates graph distances, all inclusive radius-two cliques, maximal-simplex coverage, elementary collapses against the current global face set, and the final exact residual triangulated-product faces. It prints `HIGH_GIRTH_PRISM_RIPS2_COLLAPSE_OK 165` on success. The embedded output file is the recorded execution. Graph instances include all labeled trees through five vertices, paths and stars through eleven vertices, cycles of length seven through eleven, two bridged septagons and a theta graph with three length-four arms. No finite sample proves the theorem for all graphs; the unrestricted proof is the face-cover and free-face argument in `RESULT.md`. No independent external audit has been performed.
