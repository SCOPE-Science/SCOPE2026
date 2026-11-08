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

Analytic proof: strict endpoint descent uses the integral cosine remainder and the cycle Laplacian inequality; finite critical-set classification and expanding saddle directions yield convergence and full-measure attraction. The exact alternating invariant line and strong-stable foliation supply the inverse-square critical law.

Reproducibility: run `python verify.py` with Python 3, NumPy, and SymPy. This checks the scalar cubic jet and reciprocal-square increment, ring spectra, sampled strict-potential decreases, exact alternating-line identity, and the asymptotic coefficient on three even rings. Its recorded output is:

`VERIFY_OK exact_scalar_cubic=1 exact_reciprocal_coefficient=1 strict_descent_samples=1500 alternating_invariant_lines=3 critical_amplitude_limits=3 sink_spectra=6`

Finite sampling cannot establish the global theorem or originality. The invariant-manifold and centre-stable results are analytic inputs; independent validation has not been performed.
