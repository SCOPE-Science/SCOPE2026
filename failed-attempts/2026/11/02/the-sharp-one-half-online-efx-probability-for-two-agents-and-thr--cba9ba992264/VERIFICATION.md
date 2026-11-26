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

For one singleton and one pair, the singleton owner's good must be weakly maximal in her values, with no further restriction. Fixing arrival-order tie breaks gives strict rankings for the proof without changing that sufficiency. When the first two rankings disagree, one first-coin outcome leaves both agents with their preferred early good; this succeeds unless both rank the third good top, in which case the other outcome, stacking the two early goods, succeeds. If both favor the first good, the success lower bound conditional on first recipient i is (1−T_i+T_j)/2 for T_i the indicator that the third ranks top; averaging cancels the indicators. If both favor the second, exactly one second-coin branch certifies success based on the other agent's top. For identical positive inputs (1,1,ε) and (1,1,L), 0<ε<1<L, only 1+2 splits can be EFX, and the first two goods must be split on the low-tail input and stacked on the high-tail input. The distribution on that decision is shared, so one success probability is at most 1/2. An independent direct enumeration of the policy found 9,200, 2,800, 3,625 profiles at probabilities 1/2, 3/4, 1 over {0,…,4}⁶, and checked all eight recipient strings for each of two positive tails.

## originality

FAIL

Resultary 5609d624fa0a states the exact optimal 1/2 guarantee for the same horizon and information model and proves it even for normalized nonnegative monotone set valuations. It supplies an additive upper witness, so the additive restriction here changes neither the lower nor the upper bound. The frozen policy is not identical, but the mathematical finding is already covered.

## value

FAIL

The original exact 1/2 benchmark for the first nontrivial horizon is meaningful. Here it is a restriction of an existing sharp theorem with an equally elementary online rule. The changed policy and exhaustive grid cross-check do not give a separately motivated improvement or new invariant, and the additive restriction is not a surviving distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
