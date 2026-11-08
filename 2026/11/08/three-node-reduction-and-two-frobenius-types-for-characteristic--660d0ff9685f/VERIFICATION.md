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

The general proof uses exact differentiation, resolution of ordinary double points, an Artin–Schreier character sum, and the standard point-count/Picard comparison for geometrically rational surfaces. The finite-field witness is `checks/markoff_verify.py`. Execute `python3 checks/markoff_verify.py` with Python 3; the reference execution output in `checks/output.txt` finishes with `VERIFY_OK`.

The script exhausts all affine coordinate triples and all level parameters for \(\mathbb F_{2^m}\) with \(1\le m\le6\), including the zero-level boundary as an auxiliary check. Finite enumeration is not used as proof for unbounded extensions, and does not independently establish historical novelty, resolution geometry, or Picard rank. The independent audit has not been performed.
