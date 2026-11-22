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

Execute `python3 checker.py` with a standard Python 3 interpreter. It requires no third-party packages. `checker_output.txt` is the actual captured stdout from the exhaustive checks in eleven parameter pairs. For each coefficient vector, the program builds the matrix on the maximal ideal by multiplying and truncating polynomial coefficients, then computes linear ranks from matrix powers via modular Gaussian elimination. The predicted Jordan partition is separately computed from the first nonzero degree and the floor-rank formula. All cases passed; the exhaustive computational range is finite (prime fields of orders 2, 3 and 5 only) and does not replace the universal proof in RESULT.md. The code does not assert an independent audit, external certification, or a test of fields of nonprime order. Leading degree is nilpotent for the nonautomorphisms considered here. The identity-preserving endomorphism has a separate unit eigenline and is not the linear operator enumerated.
