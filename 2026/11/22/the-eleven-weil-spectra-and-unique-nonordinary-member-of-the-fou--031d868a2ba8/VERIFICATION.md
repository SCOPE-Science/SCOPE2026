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

# Exact checks and their scope

Execute `python verify.py` with Python 3.10+ and SymPy 1.12+. On a successful run it prints eleven rows followed by `KAWAKITA_F7_COMPLETE_CENSUS_VERIFIED parameters=49 smooth_four_node=29 zeta_types=11 nonordinary=1 p_rank=3 ordinary=28 p_rank=6`.

All projective singularity charts are exhaustively checked with exact characteristic-seven polynomial Gröbner bases; the genus-two factors are checked squarefree. Point counts are exact in the field \(\mathbb F_{49}\) represented by pairs modulo \(i^2+1\). The verifier also enumerates all rational points on the defining plane sextic and confirms the correction from four split ordinary nodes. The cited isogeny relation and the birational quotient construction are published theorems, not re-proved in the program. No independent audit has been performed.
