---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Eliminating steady-state R,C yields F(I)=I+alpha I N(I)/D(I)=1−(mu+alpha)/beta with N linear and D quadratic in I. The quotient derivative numerator n0d0+2n1d0 I+(n1d1−n0d2)I² has strictly positive coefficients; the source factorization Q>0 works for independently varying epsilons and 0<=sigma<=1. Unique root 0<I<L reconstructs a strictly positive simplex state; fixed-I parameter derivatives yield strict epsilon1 and conditional epsilon2 monotonicity, equality at sigma=1. The uniform positive lower bound on I makes a,b grow when respective feedbacks diverge, establishing the two distinct one-axis rational limiting equations and the joint I->L with immune states vanishing. The inspected SymPy checker tests algebraic identities, a finite example and boundaries, not an infinite proof.

## originality

FAIL

A Resultary-published October 11, 2026 record for exactly this prevalence-driven SIRCm system gives the same unconditional independent-two-feedback uniqueness, strict parameter responses, sigma=1 cancellation and the same scalar elimination and coefficient/sign identities, confirmed by reading its complete RESULT.md, predating October 12 source. The extra asymmetric limits in the current source arise by sending a or b to infinity in precisely the published rational equilibrium formulas; they do not rescue acceptance of the original covered headline. Strong prior statement/implication is decisive.

## value

FAIL

The global all-strength uniqueness and comparative-statistics classification already exists with the same exact formula and stronger scope in the October 11 record. The remaining two one-axis limits arise immediately by coefficient comparison in those already published rational formulas, without a new structural lemma or independently motivated unsolved parameter invariant. Correctness and a worked example do not make this duplicated global theorem an original worthwhile contribution. No narrowed corrected full science package was developed, so rejecting the unchanged original is appropriate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
