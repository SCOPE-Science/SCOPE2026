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

The exact algebra and finite regression checks were run with `python verify.py` using SymPy. The checks include direct symbolic inversion of the stated five-by-five precision matrix, all three orbit diagonal identities, both comparison rational identities and their denominators, the orbit difference identity, 210 direct rational inverse experiments over positive screening and weakened-edge weights, and exact rational brackets for the two screening thresholds at edge weight \(w=1/2\).

The observed output was `PASS 871 exact and algebraic/numerical-root tests; root numerics are supplementary, not proof`.

The checker is independent of any precomputed matrix files. The proof of exactly one positive root of each polynomial, the strict root order, and completeness of all optimality cases is analytical and documented in `RESULT.md`. Finite calculations alone cannot prove those universal statements. No independent scientific validation is asserted.
