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

# Verification notes

The full proof appears in `RESULT.md`. The decisive algebraic identities are: the regular-grid alias relation \(e^{\pm imz}=1\); the norm-one orthogonal witness \((\psi_0-\psi_m-\psi_{-m})/\sqrt3\); the top-mode sample orthogonality on both three-or-more-point component polygons; and cancellation of the \(m\)-frequency Fourier spike across the two staggered cosets. The exact residual tail is \(\varepsilon(1-2^{1-m})\). These imply the claimed strict comparison for all even \(m\ge6\) and \(0<\varepsilon<2/15\).

Run `python verify.py` to reproduce direct floating-point RKHS Gram calculations on four even landmark counts and four positive tail amplitudes. The script implements the Fourier series in closed form, inverts the full and truncated Gram matrices separately, and asserts both inequalities and strict improvement. It exercises 16 parameter combinations, including the six-point example. These finite checks do not constitute the proof for all \(m\), and they do not certify floating-point accuracy for extremely small \(\varepsilon\).

The analytic kernel and the finite checker use matching normalizations: circle Haar measure has total mass one; the rank-three truncated kernel is \(2+2\cos(\theta-\phi)\); the alignment objective is \(3-\operatorname{tr}(K_Z^{-1}K_Z^{(3)})\).

Independent external validation has not been performed.
