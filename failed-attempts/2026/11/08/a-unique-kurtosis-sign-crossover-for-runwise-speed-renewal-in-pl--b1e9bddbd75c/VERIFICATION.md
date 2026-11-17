---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For stationary isotropic two-dimensional velocity marks, projected m2=E[R^2]/2 and m4=3E[R^4]/8 give normalized radial kurtosis sign equal to the projected fourth cumulant sign. Ordered four-time Poisson renewal gives cumulant 24 alpha^-4[(m4-m2^2)I(s)-2m2^2 J(s)] with positive kernels. The ratio J/I decreases strictly by a monotone-likelihood-ratio ordering on span distributions. Its endpoints 1 and 1/2 yield rho thresholds 2 and 4/3, respectively. Additional independent translational Brownian motion contributes only to variance, not to fourth cumulant. The boundary limit t^2 K(t)=-m2^2/(alpha^4(D+m2/alpha)^2) is consistent with the previously published exact cumulant at R=2. The all-time sign statements follow analytically; no finite simulation establishes an infinite-domain result.

## originality

FAIL

Decisive exact prior implication: the published October 18 theorem on isotropic RTP in every dimension d gives a strictly decreasing complete-refresh fourth-cumulant threshold R_*(alpha t) from 3 to 2 with R=m4/m2^2=3d rho/(d+2). Set d=2: R=3rho/2, and the earlier three regimes become precisely rho<=4/3, 4/3<rho<2, rho>=2, with identical unique time crossing. The independent Brownian term leaves this cumulant unchanged, adding only deterministic variance; the boundary coefficient follows directly from the same earlier closed-form cumulant. This is a covered specialization, not a distinct surviving theorem.

## value

FAIL

The moment-sign question is mathematically motivated, and the proof is coherent, but the asserted sharp sign diagram is a literal d=2 specialization of the already published arbitrary-dimensional exact cumulant theorem. Adding an independent Gaussian diffusivity cannot change the fourth cumulant, and gives only its elementary normalization. Repackaging covered results does not yield an original substantive finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
