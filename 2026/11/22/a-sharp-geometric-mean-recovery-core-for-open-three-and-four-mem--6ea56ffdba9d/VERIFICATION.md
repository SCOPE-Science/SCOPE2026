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
# Verification and reproducibility

The proof is self-contained in `RESULT.md`. The optional `check_hypercycle.py` uses only the Python 3 standard library and checks the polynomial identities by exact rational calculations, the five-species obstruction, numerical roots, and forward-invariance samples. Run from the extracted package directory: `python check_hypercycle.py`.

The all-parameter and infinite-time claims rest on the invariant-region argument and the invariance principle, not on sampled trajectories. The numerical outputs cannot validate historical originality. The full text of the 2012 primary comparison has imperfect mathematical extraction, so its possible implication of this particular recovery certificate remains an explicit priority risk. Independent audit: not performed.
