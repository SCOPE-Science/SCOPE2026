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

The analytical proof uses direct Gram integrals, exact block diagonalization, a strict negative determinant and explicit rationalization. The saved standalone `CHECK.py` executed with `numpy` and `sympy`, printing `TWO_ARC_FOURIER_CHECKS_PASSED 3591`. These checks include direct exponential integrals from interval endpoints, direct eigenvalue calculations, Rayleigh-quotient energy integration, symbolic determinant identity and limits for the two small-window asymptotic constants.

For any arbitrary width in the specified open interval, the strict negativity is proved analytically from \(0<\beta<\pi/2\), \(B>0\), and \(C>B\); a numerical parameter grid is not an exhaustive infinite-domain certificate. The theorem does not address larger Fourier subspaces or unequal observation windows. Publication originality has not been independently audited; the most relevant 2026 multiwindow preprint was available only by abstract.
