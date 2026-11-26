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

For a difference d=y−x, equality of adjacent read increments is exactly d_(i+h)=d_i; equality of the first read is the additional condition Σ_(j≤h)d_j=0. Together these are necessary and sufficient, including a single window. Each mixed binary column is rigid under constant shifts; pure columns can be recolored independently subject only to conserving t, their number of one columns. Thus the invariant data give precisely a binomial fiber, and the products over mixed columns count the full fiber census. For B(z)=∏(b_j+z), the total is B(1)+B′(1); the singleton count is 2B(1)−B(0), since t=0 and t=p coincide only when p=0. This remains valid for columns of length one. For h+1, there are h−1 non-singletons with all columns pure and 2(h−2) with the sole length-two column mixed. The maximal central binomial coefficient at h≥2 cannot be matched by fewer columns; the maximizing reads are the one or two central constant vectors. A zero-error code is a transversal of the fibers. A fresh independent direct grouping of 16,388 word-width instances across 45 pairs 2≤h≤n≤10 agreed with the full histogram and all counts, including the boundaries.

## originality

PASS

The exact finite census in the nonwrapping model with general (possibly unequal) column lengths closes a named counting gap in the same-model literature and gives more than K. Boundary cases, the shared pure/mixed rigidity argument, and the divisible-length full census are already covered. The distinct cyclic results, including the same-day multilevel result, do not cover the general nonwrapping theorem.

## value

PASS

Resolves the explicitly posed general count of ambiguous read classes in the exact ordered binary model. The full distribution distinguishes many different collision behaviors with the same total, proves the extremal ambiguity, and determines finite zero-error code size. The result is a complete natural census, not just a check of a boundary number or a restatement of asymptotic capacity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
