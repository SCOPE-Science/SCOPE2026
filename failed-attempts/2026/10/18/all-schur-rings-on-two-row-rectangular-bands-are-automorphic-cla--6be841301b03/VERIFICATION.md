---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The product coefficient is r_X(i)c_Y(j). Summing equal coefficients over either block index gives equality of row and column signatures separately, since the constant marginal totals 2 and n are nonzero in Q. Conversely those equalities suffice for closure. If the two row signatures differ, matching column signatures force identical column partitions on the two rows. Otherwise every block has equal row cardinalities. A block label can occur only with one partner label, because any columns sharing it have the same unordered label multiset. For distinct partners, equal row counts force equal orientation halves; a self-partner gives one monochromatic group. This also makes the column partition and decoration recoverable. A column-group stabilizer acts on separated rows; for balanced rows the within-half permutations and the coupled row/half swap act transitively on each label without merging labels. All automorphisms preserve the row and column equivalences characterized respectively by equality of right- and left-multiplication maps, so the ambient group is S2×Sn. Unordered equal halves account for the factor 1/2 and the two empty formal terms are excluded. Independent enumeration through n=5 recovered the 2,5,13,48,184 totals and checked accepted partitions by multiplying actual cells and testing orbits of the full blockwise stabilizer.

## originality

FAIL

An earlier distinct Resultary record proves the same exhaustive classification of labeled two-row partitions and their automorphicity and gives the same enumeration. The earlier primary semigroup paper's lower bound and small cases alone would not establish coverage, but the earlier Resultary finding does.

## value

FAIL

The structural classification would itself be valuable, but this submission reproduces the already classified family, orbit realization, enumerator and small table without a distinct substantive remainder. The verified computation is corroboration, not a new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
