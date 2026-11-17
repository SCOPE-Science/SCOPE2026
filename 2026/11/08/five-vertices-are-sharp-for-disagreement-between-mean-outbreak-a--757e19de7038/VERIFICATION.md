---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

At ≤4 original vertices all post-deletion graphs have ≤3 vertices, totally nested by edge inclusion up to relabeling, so one smallest residual graph is stochastically dominated at every p for all monotone component-size losses. For n=5 the exact distribution of the open cluster is sum over connected induced S with boundary closure (|S|/4)R(H[S],p)(1-p)^{b(S)}. The source verifier enumerates all 2^10 labeled graphs, 5! relabelings and 21 connected classes, compares all 105 delete-vertex objective polynomial pairs via two different expansions, and uses rational real-root isolation for inequalities on the whole interval. Both exceptional classes have exact mean/tail differences: A ΔM=p²(1-4p)/2, ΔT=p²(3-4p)/4; B ΔM=p²(p-1)(4p-1)/2, ΔT=p²(p-1)(4p-3)/4. Independent from-scratch enumeration reconstructed all 21 class representatives and those exact factorizations, and checked that only two classes disagree at p=1/2; full all-p claim rests on inspected exact source root-isolation certificates, not the finite check alone.

## originality

PASS

Same-day published full 21-class mean-only vaccination theorem determines the p=1/4 switch for mean size, including both A/B topologies, but does not include the ≥3 tail-risk minimizer. Kenah–Miller discusses major epidemic probability vs attack rate for heterogeneous large populations, not exact small graph conditioned size≥3. Holme 2017 compares different tasks (influence, mean vaccination, sentinel) not both functionals for the same single vaccination. The joint mean-vs-tail two-type census survives originality.

## value

PASS

The distinction between expected total cases and probability of reaching a specified three-person harm threshold is a motivated risk-neutral versus risk-sensitive choice in stochastic network control. The complete first nontrivial graph-order boundary, two exact exception types and full disagreement interval are useful exact graph-reliability invariants not mechanically implied by the mean-only vaccination census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
