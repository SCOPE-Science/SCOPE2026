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

# Reproducibility and verification

Run `python check_cusp_overshoot.py` using the Python standard library from this package's root. The checker prints `HYPERBOLIC_CUSP_OVERSHOOT_CHECKS_OK` after 80,000 direct Euclidean-circle geometry comparisons, numerical integration of the exact probability for three cusp widths and three threshold heights, declining relative errors for its two-term expansion, and the beta–Dirichlet normalization and second-moment identities.

The analytic proof in `RESULT.md` establishes the deterministic horocycle criterion, the exact two-dimensional probability, the uniform asymptotic remainder \(O_w(H^{-10})\), and the \(O_w(H^{-2})\) total-variation bound. Numerical integration and random tests corroborate those calculations but cannot establish identities for all parameters or convergence of measures. The scientific comparison uses full relevant sections of Haas (2007) and Gadre (2014), Borthwick (2010) for cusp coordinates, and the complete mathematical result texts of two nearby 2026 published records. A broader independent historical-priority assessment has not been performed.
