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

The proof is self-contained apart from the standard non-extreme de Branges–Rovnyak norm identity and the classical spectral theorem for half-line constant-coefficient Jacobi operators, both stated in `RESULT.md`. `CHECK.py` recomputes coefficient Gram matrices and checks the generalized finite-section spectra for the specified finite ranges. The run passed 36,616 assertions. To reproduce, install `requirements.txt` and run `python CHECK.py` in a directory containing both files. A finite matrix calculation cannot certify an infinite spectral endpoint, nonattainment or exhaustive publication originality; those require the analytic recurrence and external literature comparison in `RESULT.md` and `REVIEW.md`.
