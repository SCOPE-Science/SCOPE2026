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

Run `python3 verify.py` using only Python standard library. The program reconstructs exact facet normals from all signed edge-gradient words for \(3\le n\le15\), checks the exact extremal norm and multiplicities, and independently verifies the known covariance identity for \(3\le n\le9\). It also enumerates the full gradient alphabet with the rank constraint for small dimensions. The continuous functional limit and universal extremal classifications are proved in `RESULT.md`; the program does not certify functional weak convergence or the infinitely many dimensions. Exact output and checker source must be inspected together.
