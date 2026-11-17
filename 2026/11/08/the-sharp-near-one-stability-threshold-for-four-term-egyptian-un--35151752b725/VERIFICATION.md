---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The classical 3-term Sylvester/Curtiss bound gives beta=41/42 uniquely at (2,3,7). For any other triple prefix and total >beta, the strict rational inequalities x_(j+1)<(4-j)/(beta-s_j) bound each next denominator without a search cutoff. These yield 21 possible triples including one special prefix, 20 other triples in seven listed groups. Each has maximal under-1 fourth denominator max(z,floor[1/(1-s)]+1); rational comparisons give unique maximum 599/600 at (2,3,8,25). Independent exact-fraction derivation recovered these 21 prefixes and unique maximum. For theta>629/630 the special greedy last denominator <=45 and its value >=629/630>599/600, proving uniqueness; on the adjacent interval strict target greed forces 46 and loses. Universal theta statement follows from finite *exhaustive algebraic bounds*, not bounded empirical scan.

## originality

PASS

Nathanson 2022/23 treats the general n-term greedy question, classical Sylvester triple optimality and two-term results; it does not state this sharp fourth-term near-one interval or second-best non-greedy prefix max. Chu covers two terms, and Kovač–Tang concern eventual greed for increasing length at rational targets. A published SCOPE November 2 result on arbitrarily many exactly best three-term representations has different quantifiers and does not imply the present real interval. Searches found no equivalent finite four-term phase threshold.

## value

PASS

This supplies a sharp boundary of greedy optimality on an open real interval for exactly four Egyptian reciprocals, together with a natural second-best extremum 599/600. It answers a motivated fixed-length underapproximation stability question with fully exhaustive rational bounds and a uniquely identified obstruction, not an arbitrary four-tuple computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
