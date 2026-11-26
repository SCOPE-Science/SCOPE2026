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

Idempotence and distant commutation are immediate; either three-comparator side of the braid sorts its triple. Hence the type-A 0-Hecke presentation gives at most n! transformations. On an auxiliary n-label chain, every permutation is reachable from the descending input: starting at the target, exchange adjacent ascents until descending, and reverse that sequence of exchanges. Each reversed exchange sorts an adjacent inversion. The n! possible evaluations therefore exhaust and distinguish the normal forms on the auxiliary chain. The increasing binary threshold maps commute with every comparator. The n−1 threshold images of any auxiliary permutation recover every coordinate's label, so the descending binary cuts already distinguish all the normal forms, establishing n! elements also for m>=2. For the packed probe indexed by G={k_1<...<k_r}, the inclusive threshold >=r−s+1 yields precisely the descending binary cut after k_s. Thus ceil((n−1)/(m−1)) packed probes suffice. For each j, take the reachable auxiliary evaluation that is sorted except for a swap at j,j+1. The resulting transformation G_j is distinct from full sort F, and c_j composed with G_j equals F by equality on the auxiliary input and the normal-form bijection. When G_j differs from F on a word, its final sorting comparator must change that pair, so the sorted output has a strict rise at j. There are at most m−1 rises per probe, which proves the matching lower bound even for arbitrary nonmonotone probes. The single-probe and binary cases and the n=1 or m=1 singleton-action boundaries follow.

## originality

PASS

The exact optimum for pairwise separation in this fixed finite-alphabet action survives comparison with the classical 0-Hecke action, sorting-network recognition, and circuit-fault test sets. The claim does not include new monoid relations, order n!, or binary faithfulness. The access limitations for older sorting test-set papers are material historical risks, not evidence of absence.

## value

PASS

The result answers an exact identification question for a natural fixed action, explaining quantitatively how alphabet size substitutes for input samples. Faithfulness alone does not optimize sample size; the coatom argument imposes the same capacity bound on every input, not just the constructive descending probes. The sharp transition from n−1 binary probes to one for m>=n is useful for comparing these observable actions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
