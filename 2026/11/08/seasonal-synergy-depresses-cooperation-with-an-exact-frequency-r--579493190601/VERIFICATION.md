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

The standalone `verify.py` (Python 3, SymPy) is included in this package. Running `python verify.py` prints `VERIFY_OK` after exact symbolic verification of the equilibrium, its Jacobian and trace/determinant, all quadratic Taylor contractions, the second-order mean shift, and the frequency optimizer. The proof of the local forced periodic orbit uses the ordinary real-analytic Poincaré-map implicit-function theorem, with a hyperbolic unforced fixed point. The code checks algebraic obligations, not the existence theorem by numerical enumeration.

Independent numerical diagnostics used period-map root solving, high-accuracy adaptive integration, and period averaging at feedback speeds \(arepsilon=0.6,1,2\) and multiple frequencies. At \(arepsilon=1\), \(\omega=\sqrt3/4\), the finite-amplitude estimates of the normalized mean correction were \(-1.99888413\) at forcing amplitude \(0.01\) and \(-1.99305173\) at amplitude \(0.005\), approaching the exact \(-448/225\). These tests support but do not prove the asymptotic theorem.

The statement does not cover the stability boundary, the zero-frequency limit with coupled amplitude scaling, or any finite-amplitude global optimum. The supplementary continuous-forcing appendix of the peer-reviewed source remained inaccessible through the tested public link; publication-priority risk persists. Independent audit has not been performed.
