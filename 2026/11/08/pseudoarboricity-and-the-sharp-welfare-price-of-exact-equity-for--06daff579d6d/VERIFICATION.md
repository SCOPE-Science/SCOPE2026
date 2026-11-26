---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Hall applied to t copies per agent is equivalent to the subset inequalities on agents: every set of copies uses the neighborhood of its projected agents and has size at most t times their count. |N(S)|=D|S|−e_G(S) counts each internal shared good once rather than twice. Every unmatched good can be placed with a nonapprover since n≥3 and support is at most two, giving exact equality; if n=2 this step need not work. The degree bound gives t*≥floor(D/2), so another bundle can contain at most D−t*≤t*+1 of any agent's approved goods; every optimal EQ allocation is EF1. Since m=nD−e_G(N), fixed positive λ entails a subset of at least two vertices with at least (λ−1)|S|+1 edges. Two vertices with 2λ−1 parallel edges and singleton fill achieve this lower edge threshold in every feasible layer. The λ=0 ratio is 1, the λ=1 ratio is larger, and the positive-layer expression increases strictly with λ, yielding the fixed-(n,D) optimum. Independently recoded check at /workspace/branches/231cf4c4-c615-41c9-a890-526e28f32348/independent_check.py: all 346 specified small multiplicity profiles, literal EF1 and exact matching, 34 exhaustive complete-assignment cases, and the explicit extremizers over 190 (n,D) pairs. The argument, not that finite sample, proves universal sharpness.

## originality

PASS

Best-of-knowledge pass for the combined exact common-utility and sharp density-layer welfare characterization, not for the Hall or pseudoarboricity characterization itself.

## value

PASS

The result resolves a natural quantitative compatibility question on a two-support domain without laminarity: exact EQ can have a welfare cost, but adding EF1 at its optimum costs nothing further. The sharp penalty at every density layer and the explicit extremizers are useful beyond a routine matching feasibility check. The scope allows transfers to nonapprovers, so no efficient-allocation claim is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
