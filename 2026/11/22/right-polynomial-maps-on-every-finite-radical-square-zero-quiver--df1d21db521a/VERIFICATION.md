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

# Verification and limits

The mathematical argument is in RESULT.md. The following direct checks were completed on small prime fields by multiplying elements of each truncated path algebra and enumerating distinct evaluation-vector functions. They corroborate but cannot establish the unrestricted theorem.

The standalone CHECKER.py requires only the Python standard library. Run `python CHECKER.py` after extracting the complete package. The successful terminating marker is `RIGHT_POLYNOMIAL_QUIVER_CHECKS_OK`.

- Over the two-element field: one loop has 64 right-polynomial functions and 8 bijective ones; two parallel loops have 256 and 32; either one-edge orientation has 256 and 16; a directed two-cycle has 4096 and 64; a source fork has 4096 and 128; and a directed three-vertex path has 16384 and 128.
- Over the three-element field: one loop has 19683 right-polynomial functions and 1296 bijective ones; a single directed edge has 531441 and 7776.

For each model, the checker independently obtains the dimension of the coefficient-evaluation linear span and exhaustively enumerates all functions in that span to test injectivity. It also checks the explicit coefficient witness for non-closure where a nonloop arrow exists. The general proof applies to every finite field, including nonprime fields, and every finite quiver even when loops and oriented cycles occur; the checker covers only listed prime-field cases. An independent scientific audit has not been performed.
