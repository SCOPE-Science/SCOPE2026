---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Let α_i be the A-normalized mass or minus B-normalized mass; Σα=0. Discrete summation by parts gives mean_A(f)−mean_B(f)=−Σ S_k Δf_k, so variation of P_μ f is W|Σ S_k Δf_k| and the exact sharp constant is W max |S_k|/w_k, attained by a single jump at a maximizing edge. Projection fixes 1_A, proving K≥1. If K=1 the transition-edge equality for 1_A forces exact run fractions b0/W, (b_{j−1}+b_j)/W, blast/W and the remaining internal-edge constraints; these are sufficient. Distributing epsilon mass inside runs and boundary masses adjacent to each transition yields positive μ with K=1 for arbitrary positive w. The universal bound K≤W/w_* is strict when W>w_*; concentrating opposite colors on opposite sides of a minimum-weight cut approaches it and continuity on the positive mass cone fills exactly [1,W/w_*). This argument includes singleton runs and two-run equality W=w_*.

## originality

PASS

Distinct edge-weighted fixed-word positive-mass contraction design and full attainability spectrum extend the known cyclic theorem and differ from global partition envelopes. No logically dominating formulation found in reviewed sources.

## value

PASS

For nonlocal color-class averaging, total-variation contraction is not automatic even though positivity and idempotence hold. The result gives a complete and constructive answer for every two-color word and independently prescribed positive edge costs, including rigid optimal mass distribution and every achievable sharp amplification. It supplies mathematically motivated exact stability design rather than a trivial projection norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
