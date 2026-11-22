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

# Reproducibility and limits

The attached `verify.py` is self-contained; execute `python3 verify.py`. The checker was run against this precise code, not a stale verifier from another result, and ended in `ALL CHECKS PASSED`. It exhaustively checks all `2**16` vertex masks for each graph, its distance-two parameters, each forbidden induced path, exact mod-two chain boundary ranks using distinct column and row algorithms, square-zero identities and Euler compatibility. All computations use exact integer bit operations. The result is a finite coefficient-field computation only; integral homology, rational homology and homotopy types are not established.
