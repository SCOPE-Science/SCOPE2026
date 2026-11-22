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

The complete mathematical proof is in `RESULT.md`. The standalone standard-library checker `verify.py` exhaustively checks the local four- and five-bit identities, independently computes finite-time image languages through four iterations by de Bruijn subset automata and finite-state product-graph closure, compares direct input-block languages for selected lengths, and reproduces the characteristic polynomials with exact integer arithmetic.

Execute `python3 verify.py` and require the final `VERIFY_OK` line. The finite computations are exact for their expressly stated finite scopes; the conclusion for every temporal iteration follows from the symbolic defect-motion and inverse-branch induction, not extrapolation. No external or independent mathematical audit is recorded.
