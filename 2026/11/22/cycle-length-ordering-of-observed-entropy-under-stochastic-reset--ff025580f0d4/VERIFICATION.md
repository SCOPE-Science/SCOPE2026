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

The standalone Python standard-library checker `verify.py` independently constructs the finite transition kernels, solves rational stationary balance equations, and computes merged-destination Markov entropies. On execution it reports 1,048 passing checks across ring sizes from 3 through 14 and six exact-rational reset probabilities, plus Green-function recurrence tests. It checks finite-state normalization, entropy formulas and the finite-size deficit identity. It does not certify the infinite family or bibliographic priority; the full proof and source comparison appear in RESULT.md. Independent scientific audit has not been performed.
