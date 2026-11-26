---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Theorem 4.3 of Olberding–Walker gives a submersion on the whole quadrangle manifold, including both endpoints. The critical line u=0 has positive rank-one Hessian (in the w=1 chart the normal coefficient is 2/(1+4v^2), and in v=1 it is 2/(w^2+4)); the complementary chart u=1 has precisely one stationary point with Hessian diag(-8,-2). A submersion pulls back the Hessian bilinear form at a critical point, and its kernel is the preimage of the base Hessian kernel. Theorem 3.6 gives the principal-bundle projection: in a local product trivialization s is independent of the group coordinates, so removing those tangent directions preserves cleanness, normal rank and signature. Both aspect levels are nonempty (Theorem 5.4).

## originality

FAIL

The exact name Morse–Bott is not needed in the prior source. The frozen normal ranks, signs and critical sets are a direct specialization of the published Grassmann Rayleigh-quotient gradient/Hessian to the rank-one orthogonal projector on RP^2, with only an invertible source-coordinate change and submersion pullback/descent. Olberding–Walker supply all the geometry used and already give the two endpoint loci, their codimensions even on the quotient, and the lack of other critical points. No independent geometric claim remains outside that combination.

## value

FAIL

The endpoint observation is a correct explanatory remark, but the frozen contribution is a routine application of a projective Rayleigh-quotient calculation to level sets whose identification and codimensions are already known. It neither resolves an additional quadrangle-specific Hessian obstruction nor gives a new global or subgroup-specific conclusion beyond automatic submersion transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
