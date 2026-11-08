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

# Verification of sharp edge laws

The proof is analytical. Its key independent identities are \(\rho_S=4\pi\operatorname{Var}_{\mu_\omega}(X)\) and \(\frac{d}{d\omega}\mathbb E_{\mu_\omega}X=4\pi\operatorname{Var}_{\mu_\omega}(X)\); both follow by differentiation of Gaussian-weighted integrals. The unrestricted flat-edge result requires the Gaussian saddle concentration lemma shown in `RESULT.md`, including convergence of centered second moments.

The self-contained script `CHECK.py` (Python 3, SciPy) tests the bounded spectrum \(S(x)=x^2\exp(-(1-x)^{-\beta})\mathbf1_{(0,1)}(x)\). It calculates Gaussian-weighted moments by quadrature for \(\beta=1/2,1,2\) and compares them with the predicted sharp variance width and mean edge deficit. It also checks the lower-edge power-two asymptotic and independent centered-difference derivatives of the tilted mean. On the packaged code, execution returned `EDGE_ZERO_TAIL_CHECKS_PASSED`.

Finite quadrature cannot prove limits for all positive flatness parameters or validate a publication-priority claim. No external independent audit or validation was performed.
