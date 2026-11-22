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

# Finite verification and proof coverage

Execute `python verify.py` from the same extracted directory. The standalone script enumerates every symmetric matching with zero, one or two edges on \(n=1,\ldots,8\) vertices, independently evaluates the stable-extension axioms, enumerates all potentially nonconstant query supports of sizes up to four, and computes exact Littlestone depths by recursive splitting of hypothesis sets. It reproduces the polynomial coefficients and online dimensions, ending in `VERIFY_OK 8`.

The tests do not prove the all-order theorem. That theorem follows from the explicit mathematical proof in `RESULT.md`, including the zero/one/two-edge case split, the positive-fiber argument and the all-size path construction. The 2026 motivating article's full text was not accessible for complete historical priority comparison. Independent review has not been performed.
