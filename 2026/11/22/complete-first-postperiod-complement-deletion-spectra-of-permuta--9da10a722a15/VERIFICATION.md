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

The weak-descent jumps in period indices give the embedding count by stars and bars. For a collision, equal retained letters force aligned index differences in {−q,0,q}; a sign change without a zero would require one skipped run of at least 2q positions, impossible with q+1 deletions. At the two ends of a nonzero run each mask is forced to have a full consecutive q-block of deletions. Removing that block always gives P^(n−1), in which distinct single-position deletions give distinct remnants (the symbols between two such positions would otherwise all be equal). For a fixed remaining deletion j=qk+a, there are k+1 or k prefix placements and n−1−k or n−2−k suffix placements, as determined by phase. Both forms can represent the same target only for a fully cyclic q+1-word; exactly the adjacent-block pair represents one mask twice, leaving n−1 distinct masks at each of n−1 indices. The other placement ranges give one fiber of each stated nontrivial size. The excess multiplicities sum to the three deficits. At n=2 the cyclic class has just one singleton output per pattern and every class has zero deficit; absent patterns have zero embeddings and no correction. The class sizes follow by counting prefix and suffix families whose intersection has size q.

## originality

PASS

The supported distinction is the complete length-(q+1), fixed-pattern, rooted output-fiber law for q≥3. The embedding term and first-collision threshold are known; binary three-deletion and one-full-period results are close but do not give the four-class theorem. The same-day matches are considered on substance, without inferring priority from the date.

## value

PASS

The first deletion budget beyond a whole period changes conditional ambiguity in three different ways. The classification identifies every target susceptible to collisions and gives all residual list sizes, which cannot be recovered from the embedding count, injectivity threshold or unconditional deletion sphere.

The dated certificate retains the supplied scientific assessment, sources and limitations.
