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

For u=s−θ1{x>0}, let m and d be the half-sum and half-difference of the two free conditional resolvents. The backward equations give v m′=(u+2α)d and v d′=u m−1. Boundedness selects one decaying mode on each half-line. Matching m,d at zero with p=s−θ and q=s yields F=(1/D_p+1/D_q)/(q/D_q+p/D_p), D_u=√(u(u+2α)), which is the frozen transform. For α=0 a direct two-direction average gives the same result. Full reset renews the process. The unique kernel root has p,q>0 since F decreases from infinity to zero on s>max(0,θ); for nonzero θ, λ lies strictly between 0 and θ, so no extraneous squared root is taken. Squaring the pole equation gives λ²+(2R−θ)λ−Rθ=0. The exponentially tilted renewal kernel is nonlattice with finite mean and its forcing is continuous with an exponential bound, so the root is the genuine SCGF. Bounded support and the derivative range (0,1) give the full LDP, with the endpoint lower bound by interior approximation. For an independent variance check, differentiating the centered renewal transform at tilt zero gives the Laplace transform of Var(A_T), [1/(z+r)+1/(z+r+2α)]/(4z²). Inverting gives slope (1/r+1/(r+2α))/4=1/(4R), including α=0. R increases from r/2 toward r and the sign observable is independent of v>0.

## originality

FAIL

Bressloff's published exact interface and renewal equations already cover this same model and observable for arbitrary reset-direction probabilities. On setting both probabilities to 1/2, adding and subtracting the two interface conditions reduces the resolvent to the frozen ratio; squaring the scalar pole equation is an elementary quadratic cancellation. The explicit rate, SCGF and variance are therefore covered by direct specialization and standard convex duality/renewal arguments, despite the absence of that closed form from the inspected symmetric-case discussion. No exact same-model Resultary comparator was needed for this decision.

## value

FAIL

The finite-persistence Brownian comparison is a clear and useful interpretation, and the explicit reduction removes the need for numerical pole-finding in the symmetric model. The frozen mathematical claim nevertheless consists of that routine exact specialization of the already solved transform, standard large-deviation and variance deductions, and the direct ballistic limit. It establishes no separate nonmechanically implied invariant, renewal regime, or additional nontrivial claim about the correction of the earlier numerical treatment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
