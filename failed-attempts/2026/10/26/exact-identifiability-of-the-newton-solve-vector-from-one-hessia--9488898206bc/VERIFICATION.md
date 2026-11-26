---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

If g=αy, then every consistent A yields A⁻¹g=αv, including α=0. Conversely, for any consistent A, write p=A⁻¹g. If g is not in span(y), then p is not in span(v). Let w be its nonzero orthogonal projection onto v's perpendicular complement. Then A+εwwᵀ for ε>0 is positive definite and gives the same product on v, but its action on p differs by εw(wᵀp)≠0. Thus the solve cannot be common. This verifies the frozen block perturbation argument without making assumptions about the query beyond the stated fixed consistent data. The n=3 example has leading minors (2,3,3) and (2,5,5) respectively, matching products (2,1,0)ᵀ and distinct solve vectors (2/3,−1/3,0)ᵀ and (3/5,−1/5,0)ᵀ by direct multiplication. The conventional Newton step is the negative of the solve vector. Frozen verify_example.py is a replay path for the witness only; it was inspected and not executed.

## originality

FAIL

The one-query criterion is an immediate deterministic implication of earlier exact symmetric matrix conditioning geometry. With B=A⁻¹ the observed equation is By=v. Hennig's symmetric posterior covariance has full support on the symmetric perturbations annihilating y, given nondegenerate weight, and restricts all solutions to that exact observation. If g is outside span(y), the support includes a rank-one direction wwᵀ with w perpendicular to y and wᵀg≠0. At any consistent SPD inverse B a small such perturbation stays SPD and changes Bg; if g is in span(y), Bg is already fixed by By=v. The earlier paper does not itself state an SPD-conditioned posterior or label this an identifiability theorem. The implication uses only the full symmetric affine support and the openness of the SPD cone, not a new positive-definite prior or a new conditions theorem. The earlier inverse-posterior covariance formula for arbitrary exact products also yields the same span criterion in the unrestricted model.

## value

FAIL

The distinction between a single exact observation and recursive Newton-step generation is well motivated, but the exact classification here is a routine consequence of which actions remain free on the orthogonal complement of the observed span. Positivity imposes no new boundary in this setting because the feasible positive cone is open, and the finite example only illustrates that implication. The frozen result provides neither a separate quantitatively sharp boundary nor a genuinely distinct identifiability effect to retain. The fixed-query extension to more columns uses the same routine span reasoning and does not repair the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
