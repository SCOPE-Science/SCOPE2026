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

# Verification of the stated theorem

The accompanying `verify.py` requires Python 3 and SymPy. Run `python verify.py` in the extracted directory. It reconstructs the source method coefficients on reciprocal meshes, multiplies the exact companion matrices, checks the characteristic polynomial and three Schur-polynomial identities, tests both algebraic boundary roots and verifies the rational pole example \(r=9/2\), \(\lambda h=96/11\).

The proof in `RESULT.md` establishes the all-positive-ratio and infinite-step claims analytically; no finite grid, simulation, or log is relied upon as an infinite proof. Only periodic exact arithmetic and real scalar test equation solvability are covered. Independent audit has not been performed.
