---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Equivariance requires a union of full source orbits, maps them injectively to complete target orbits, and permits exactly one of ell shifts on each paired orbit. Dividing by full rank gives the stated falling-factorial weights. The summable majorant for bounded m/ell proves pointwise and total-variation convergence after normalization. At R=sqrt(m/ell) with R/m tending to zero, the successive ratio is uniformly separated from 1 on the two indicated buffered sides; comparing each exterior boundary to an interior weight by Theta(R) such ratios and summing the exterior geometric series gives the claimed concentration. Independently enumerating partial endofunction arrays with an undefined sentinel, deleting arrays with repeated defined images, and checking commutation gave rank counts (1,8,8) at ranks (0,2,4) for (m,ell)=(2,2), (1,12,18) at (0,3,6) for (2,3), and (1,18,72,48) at (0,2,4,6) for (3,2); omitted ranks had count zero. This finite check supports the coefficient identity only.

## originality

FAIL

The central novelty claim is the critical Bessel crossover rather than the credited finite count. The entire critical probability generating function is a ratio of ordinary Laguerre polynomials to which the classical complex-uniform Mehler–Heine theorem applies immediately. This covers the critical law including total variation, not just the appearance of the Bessel normalization. The subcritical limit comes from the very same theorem at parameter zero; the remaining relative concentration is the elementary single-mode ratio estimate for the known weights. There is no claim here that a prior centralizer paper literally states all three regimes.

## value

FAIL

The centralizer statistic is natural, and the translation is a useful illustration, but the headline nondegenerate law is a direct reparameterization of the standard Laguerre limit once the known count is written as a polynomial. The remaining ratio estimate is routine localization of that same known coefficient sequence, with no further fluctuation scale or structural consequence proved. No independently useful nonroutine remainder is established in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
