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

# Verification

Run `python CHECK.py` with Python, SymPy, NetworkX and NumPy installed. The exact symbolic checks verify four algebraic identities for the two-color derivative and the three Schur factors. Four explicit irregular, regular and unbalanced bipartite graphs at four diffusion values verify fixed-point residuals and full-matrix eigenvalues, yielding `BIPARTITE_LOGISTIC_EXACT_OK algebra=4 graph_cases=16`. These are finite corroborations only; the rigorous unbounded graph-size claim is proved analytically in RESULT.md by graph symmetrization and singular-mode Schur inequalities. No independent mathematical audit has been carried out.
