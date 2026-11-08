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

# Reproducibility and boundaries

Run `OPENBLAS_NUM_THREADS=1 python verify.py` using `requirements.txt` on Python 3.10+. The script uses exact rational integer operations for all algebraic assertions. SciPy's floating-point convex-hull output is used only as a source of candidate facet triangulations; supporting hyperplanes, connectedness/ridge closure, zero-volume degeneracies and volume polynomial identities are independently checked exactly. The determinant interpolation is exhaustive over 15504 five-point subsets, returning 11080 nonzero determinant instances in 30 classes and five positive critical parameters. Six rational chamber representatives cover every noncritical parameter range. Symbolic integration, asymptotic identities, Descartes sign conditions and the positivity certificate for the uniquely larger second peak are verified exactly.

The proof supplies the all-positive-coefficient transformation and sign arguments; finite computations are a proof certificate only because the family has finitely many vertices and all its orientation changes are enumerated exhaustively. The script does not establish any conclusion for other apex configurations or assert historical priority. Independent audit has not been performed.
