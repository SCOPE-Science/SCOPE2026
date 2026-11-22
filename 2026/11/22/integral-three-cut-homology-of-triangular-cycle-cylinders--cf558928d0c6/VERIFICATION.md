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

The standalone `verify.py` was executed using Python 3 and its literal output is embedded as `verify_output.txt`. For each integer \(5\le n\le10\), it independently constructs the three-wise-connected Alexander dual, exhaustively excludes five-vertex faces, performs every advertised free-face collapse in the evolving simplicial complex, compares the precise residual prism-boundary complex and long edges, and computes the two independent mod-two simplicial boundary ranks. All tests passed. The universal proof is given in `RESULT.md` by symbolic rectangle-and-prism arguments and integral Alexander duality. Finite-field checks do not prove integral torsion-freeness or the all-integer result; the homotopy decomposition supplies both. No external independent audit was performed.
