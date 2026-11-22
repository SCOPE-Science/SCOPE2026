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
# Reproduction and proof limits

Run `python3 verify.py` from the directory containing the extracted files, using Python 3 with only the standard library. The verifier was run from the actual source file and printed `VERIFY_OK 12445`. Its finite checks include all connected simple graphs with 2–5 vertices, weighted clique instances, exact nullcline examples, and the closed-form killed clique spectral-variance identity. It does not claim to exhaust all finite or weighted graphs; the universal proof is in `RESULT.md`.

The exact witnesses at the three-vertex path and killed two-vertex edge do not require a floating-point tolerance. The proof uses only finite-dimensional spectral calculus, graph connectivity and exact matrix algebra. The result is a self-review, not an independently audited mathematical certificate.
