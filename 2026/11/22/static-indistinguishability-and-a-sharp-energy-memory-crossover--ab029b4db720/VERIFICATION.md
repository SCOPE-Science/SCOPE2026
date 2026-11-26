---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Conditional on the stationary last-reset age a, the free sign segment from the last reset to observation starts in equilibrium for each protocol, and position starts at zero. Its law together with the independent Brownian increments is identical, including the final sign. Mixing over Exp(r) gives equality of the full position–diffusivity law; the scalar characteristic function follows from the two-state Feynman–Kac resolvent. Full reset regenerates; for P the independent sign chains can be coupled to coalesce, followed by a shared position reset. All used moments are finite since the age has exponential tails and diffusivity is bounded. Independently, write J_a=∫₀ᵃ S_u du; conditional on the segment, position is centered Gaussian of variance 2da+2hJ_a. Stationary sign correlations e^(−2k|u−v|) give E[J_A S_A]=1/(r+2k) and E[J_A²]=2/[r(r+2k)] on averaging over A. Thus E[X²]=2d/r, E[X²S]=2h/(r+2k), and its squared-position variance is V as displayed. At lag t, the original squared position contributes e^(−rt)X_0² to conditional mean, and the noise injected at time u contributes conditional mean 2(d+h E[S_u|S_0])du times e^(−r(t−u)), the probability of no subsequent reset. Future resets after u are independent of the sign history up to u in both models. The sign mean is S_0 e^(−λu), with λ=2k for P and λ=r+2k for F. Centering and averaging yields the claimed convolution coefficient B. Its P-minus-F integrand has the additional positive factor 1−e^(−ru), while V,B>0. Evaluating the convolution gives the two rates, the t e^(−rt) term at r=2k, and all ratio asymptotics for r,k>0 and d>h>0. The supplied symbolic and matrix-exponential checker was inspected, not rerun; the path calculation is exact.

## originality

PASS

The stationary framework and the general phenomenon of static blindness with temporal separation are not new. The supported distinct result is the equality for these two interventions in a switching diffusion, with exact strictly ordered squared-position covariances and a critical r=2k energy-relaxation law. The strongest prior analogue uses a different transport mechanism and observable.

## value

PASS

Two physically interpretable reset interventions cannot be distinguished even by measuring the stationary joint position and diffusivity. The exact squared-position witness works at every positive lag and tells when the reset clock ceases to set the long-lag decay under retention, including the critical polynomial prefactor. It is more informative than merely finding that some transition statistics differ, and is not a finite-sample identification claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
