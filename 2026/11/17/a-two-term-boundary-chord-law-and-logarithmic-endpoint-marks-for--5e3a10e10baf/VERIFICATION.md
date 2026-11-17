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

Run `python verify_reuleaux_boundary.py` after installing the packages in `requirements.txt` (NumPy and SciPy). The checker independently constructs all three circular arcs from their centers, confirms the key two-arc defect identity numerically, evaluates the exact one-dimensional integral with an adaptive quadrature and a bracketing root solve, and compares the two-term approximation over five deficit scales. It then independently simulates 1,200,000 pairs uniformly sampled by boundary arclength and checks three exact probabilities within predeclared five-binomial-standard-error margins plus a fixed small tolerance.

The actual run produced `REULEAUX_BOUNDARY_TWO_TERM_MARKED_DIAGNOSTIC_OK`. At \(\varepsilon=10^{-6}\), quadrature gave \(9.18163843707\times10^{-6}\) and the two-term formula gave \(9.18164012455\times10^{-6}\). At deficit thresholds \(0.1,0.03,0.01\), the simulated frequencies were approximately \(0.21818583,0.08671833,0.03538917\), compared with exact \(0.21857521,0.08731848,0.03579510\). This is finite diagnostic evidence, not a proof of the asymptotic or a separate audit. The proof of the two-term asymptotic and marked total variation is provided in `RESULT.md`. Historical publication priority remains subject to inaccessible older work.
