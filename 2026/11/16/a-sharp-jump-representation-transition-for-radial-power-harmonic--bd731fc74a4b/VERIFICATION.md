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

The weight is defined on \(\mathbb D\) by \((1-|z|^2)^\alpha\) for real \(\alpha\ge0\); integration uses normalized planar area and the complex gradient pair. For any boundary Fourier mode \(e^{in\theta}\), angular orthogonality yields exactly \(\psi_\alpha(|n|)=n^2B(n,\alpha+1)\), eliminating normalization ambiguity. The proof checks all parameters and modes analytically, including the constant mode.

The key nonstandard calculation is the beta first-difference identity
\[
\psi_\alpha(n+1)-\psi_\alpha(n)=\int_0^1t^n(1-t)\alpha(1-\alpha t)(1-t)^{\alpha-2}\,dt.
\]
This is integrated termwise against the normalized Poisson kernel to obtain a positive jump measure for the full \(0<\alpha\le1\) range. The impossibility direction uses only positive measure, pointwise Fejér/Cesàro convergence away from the diagonal and Fatou's lemma; it does not presume translation invariance, spectral completeness of a finite truncation, or nonlocality of a guessed kernel. Angular singularity uses an integrable scaled majorant; the critical closed form is checked by elementary integration.

Execute `python CHECK.py` from the directory containing the file. The recorded run passed 674 finite assertions, including exact rational beta recurrences at admissible and inadmissible rational exponents, the classical and endpoint spectra, high-precision checks of the exact critical jump density, and numerical checks of the small-angle singularity. The checks are supplementary and cannot prove an all-parameter or all-frequency statement on their own. No external independent mathematical validation has been performed.
