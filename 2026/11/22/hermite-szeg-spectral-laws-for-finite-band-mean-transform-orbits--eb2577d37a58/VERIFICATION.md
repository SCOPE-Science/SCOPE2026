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

# Verification of the finite-band mean-transform theorem

The exact polar and binomial iterate identity is proved in RESULT.md, followed by local Fourier asymptotics with a global tail bound and a finite-band spectral localization argument. These steps, not numerical experiments, provide the infinite-index conclusions.

The included `checker.py` runs finite tridiagonal spectral tests for the non-diagonal three-site example with \(\varepsilon=0.2\) and \(q=1/2\). It independently verifies \(\operatorname{Tr}(A_k^2)=4\varepsilon^2\binom{2k}{k}/[(k+1)4^k]\) against eigenvalues at five iteration indices, checks its first-moment cancellation, and checks the approach to the three explicitly predicted scaling constants. At \(k=640\), the scaled operator norm is approximately \(0.09145274579\) (limit \(0.09678828981\)), the scaled squared Hilbert–Schmidt norm is approximately \(0.01126398804\) (limit \(0.01128379167\)), and the scaled trace norm is approximately \(0.2032895423\) (limit \(0.2031796350\)). The script reported PASS.

Computational scope is finite and illustrative. No independent audit, machine-checked infinite proof, or external certification has been performed.
