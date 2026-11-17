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

The stationary Poisson backward age has density r e^{-ra}. Integrating the Gamma maturation CDF against the phase-locked square-wave signal and taking its first Fourier harmonic gives A/(4q/pi)=[x/sqrt(x^2+w^2)] [(1+x/k)^2+(w/k)^2]^(-k/2), valid for all k,w,x>0 by Tonelli/Fubini. Differentiating log amplitude and multiplying positive denominators produces exactly the stated quartic P; independently verified symbolically with SymPy. Coefficients have exactly one positive-to-negative sign variation for all k>0 (including 0<k<1,1<=k<2 and k>=2), and P(0)<0,P(infty)>0, giving a unique global peak. The derivative ∂_k(k(k+x)/((k+x)^2+w^2))=[x(k+x)^2+(2k+x)w^2]/denom^2>0, independently verified, proves that increasing shape moves the unique root left. The rescalings x~w^(2/3) and x~w/sqrt(k), expansion a=(1/k-1)/3, leading amplitude constant and deterministic x(x^2+w^2)=w^2 are obtained by balancing polynomial powers. Finite symbolic/numeric tests support, not substitute for, these universal deductions.

## originality

PASS

Best-of-knowledge: Wang et al 2026 original main and supplemental primary source already gives the general renewal harmonic transfer and deterministic phase-dependent transit, including w^(2/3) low-frequency scaling; these premises receive no originality credit. The cited full text does not give an independently Gamma-distributed maturation mark at fixed mean, an exact one-positive-root quartic for all real k, strict monotonic k ordering or x~w/sqrt(k) high-frequency optimum. Radice studies Gamma distributed RESET intervals rather than maturation marks after Poisson resets. A broader unindexed refractory-response theorem could imply this explicit case; risk retained.

## value

PASS

Exact rate-optimization and response-exponent laws distinguish heterogeneous maturation from deterministic delay in a natural renewal-response observable. The full positive shape continuum and monotonic preference ordering are mathematically informative, providing a sharp parametric resonance classification rather than another mere numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
