---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The factor equations follow exactly from I+U=1-S-sigma C and dot U = dot R+(1-sigma) dot C, with residual C coefficient (1-sigma)(sigma delta-gamma)(1+eps I). At gamma=sigma delta the scalar C fiber has strictly positive damping and the factor reduces to dot I=I[beta-h-beta(I+U)], dot U=alpha I-(a+bI)U. Below/at R0=1, dot I<=-(h-beta)I or -beta I² and all stable linear fibers decay. Above threshold, U=v-I and U=alpha I/(a+bI) intersect uniquely in (0,v); physicality of all steady compartments follows from positive formulas. With q=alpha-bU*=aU*/I*>0, the entropy plus beta/(2q) quadratic Lyapunov derivative is EXACTLY -beta(I-I*)²-beta(a+bI)(U-U*)²/q; I independently checked the cancellation symbolically using sympy. Its properness near I=0, simplex compactness and LaSalle imply global attraction for I(0)>0, then the stable C equation transfers it to S,R,C. At sigma=1 the structural necessity claim is correctly not made.

## originality

PASS

A genuine algebraic balance surface generates a two-dimensional factor and strict global entropy identity; the earlier all-feedback uniqueness theorem explicitly stops at equilibria and does not establish stability. Available information for the original SIRCm paper does not supply an equivalent all-feedback global theorem on gamma=sigma delta; definitive exclusion of an uninspected full manuscript is not claimed.

## value

PASS

A physically motivated parameter cancellation produces a sharp dynamical statement—global threshold dichotomy and no nonconstant periodic orbits at arbitrarily large prevalence feedback—where the source model exhibits instability for a different feedback regime. The flux-balance locus is derived from the equations rather than an arbitrary numerical slice and admits an explicit coercive Lyapunov certificate. Equilibrium uniqueness alone is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
