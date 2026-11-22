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

# Verification of the inverse-valence trichotomy

The companion file `lozi_inverse_check.py` can be run with Python, SymPy and SciPy. It verifies the Jacobian determinant and exact scalar-sheet derivative using symbolic algebra; uses root isolation to reconstruct one hundred remote supercritical predecessors for each of two targets; tests critical root counts zero, one, or two per remote phase cell on either sheet; and checks the square-root displacement at memory indices 100, 1000 and 10000. All tests passed in this package's execution.

The proof, not the finite numerical tests, establishes the infinite count and uniform sharp parameter threshold. The critical equality tests use stable evaluation of \(1-\cos s=2\sin^2(s/2)\) to avoid cancellation when identifying tangent roots. No claims of exhaustive numerical verification over real parameter space or of independent audit are made.
