---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed reward w=κDT Z²+κX√(2DT)Z, conditional mean κDT and variance 2κ²D²T²+2κ²Dσ²T. Compensated ξ=w−v(T+δ)=T(κDZ²−v)+O_p(√T) has two one-sided regularly varying tails by Breiman and a finite higher moment for perturbation; Eξ=0. Centered stable/normal domains of attraction, joint renewal functional time-change, and tight renewal backward age give physical-time normalizations. At q=2 truncated variance 2C log u yields sqrt(n log n) variance C. Independently checked exact symbolic formula Var ξ=2κ²D²ET²+2κ²Dσ²µ+(κDδ/(µ+δ))²VarT. Verifier quadrature checked source as finite support, not proof of infinite-time convergence.

## originality

PASS

PASS (best-of-knowledge): Primary Olsen et al 2024 derives general renewal generating functions and explicitly treats exponential-time harmonic moments, rather than the three heavy-tail physical-clock limits and two-sided compensated constants. General heavy-tailed renewal-reward stable theorems are acknowledged prior tools; the actual model-specific limit intensities, sign asymmetry and δ monotonicity are worked out here. Risk: a broad general theorem may imply the special case after identification.

## value

PASS

PASS: Physical-time work statistics with power-law reset intervals are a motivated thermodynamic observable; clock compensation generates a nontrivial negative stable tail despite raw work being bounded below by a light-tailed Gaussian square. The exact three-regime transition, critical normalization and sensitivity to return overhead are concrete nonroutine results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
