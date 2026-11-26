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

The actual claim is the finite joint accumulation set on squarefree three-prime inputs, with the neighborhood lower bound requiring squarefree three-prime outputs too. For odd inputs each largest pair-sum factor is at most half the sum and hence at most P(n); if one input is 2 the bound is 1+2/P(n) for R, which suffices for containment. I checked the pair-sum identities, invertibility, and universal admissibility and complexity of the six forms: (a,a,1) works modulo a prime after excluding zero and at most one other residue (at 2 use a=1); the singleton-plus-two-pair partitions have nonproportional singletons and determinant magnitudes (m,2m),(m,2m),(m,2m^2),(m,4m^2),(m,4m^2),(m,4m^2). The unconditional complexity-two prime theorem on a fixed positive-volume box applies. With the input maximum scaled to 1, the unscaled half-sum is fixed to alpha using the two smaller inputs for alpha<=1/2 and the larger two otherwise. Increasing the fixed m makes S at the equal-small-pair endpoint as small as needed; sending the free smallest input size to zero makes S diverge while R stays alpha. Continuity hits every positive beta. The product bounds on the dilated box and at most six representations of a product give X/log^6 X after removing O(N^2) equality-hyperplane points from the N-scale count. Open neighborhoods on the boundary contain positive interior targets; growing counts then give sequences tending to the boundary. Independent derivation in branches/independent-check/proof_notes.md; inspected the frozen arithmetic checker and its recorded output, not used to prove the asymptotic.

## originality

PASS

Credit the prior six-form prime input and marginal lower bounds. Neither the marginal squarefree result nor the published joint result for repeated-prime inputs contains the squarefree joint interpolation or its simultaneous neighborhood count. No separate exact equivalent was found in the inspected indexed results and primary statements.

## value

PASS

A complete joint classification for the natural squarefree family meaningfully resolves correlations left open by marginal information. The contrast with the repeated-prime curves and preservation of squarefreeness with a neighborhood count make the result useful beyond the separate interval limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
