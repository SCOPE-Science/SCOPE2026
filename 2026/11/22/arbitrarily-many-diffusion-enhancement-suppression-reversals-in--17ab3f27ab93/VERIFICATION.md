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

# Reproducibility

Execute `python verification/certify.py` with Python 3: it uses only the standard library and exactly verifies the four rational values of \(H(t)\) and alternating signs at the two-mode witness rates. This is a finite exact certificate of the witness inequalities, not the analytic induction.

Execute `python verification/galerkin.py` with Python 3, NumPy and SciPy. It independently solves the Fourier-truncated stationary Fokker–Planck equation and periodic corrector equation for \(k=1,25\), \(w=1,50\), \(\varepsilon=0.015\), at four switching rates. It evaluates diffusion via both Brownian and telegraph-jump quadratic-variation terms. Fourier resolution is \(|n|\le65\), and integration uses 1024 equally spaced phase points; results have the same four strict signs as the exact coefficient. The calculation is numerical, not an infinite-dimensional interval enclosure. Independent convergence checks and error margins are therefore not asserted for this simulation.

The proof of infinitely many sign-crossing *examples* uses analytic fixed-rate perturbation, a finite-sign preservation argument at each inductive stage, and the intermediate-value theorem. Neither numerical truncation nor a finite census is used to establish the infinite construction. The admissible weak forcing may shrink with spatial complexity and is not explicitly quantified.
