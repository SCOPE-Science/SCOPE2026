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

The 3-uniform substitution gives w(3n)=w(3n+1)=w(n), w(3n+2)=1-w(n); adjacent differences satisfy d(3n)=0, d(3n+1)=1, d(3n+2)=1-d(n). For a square period p, adjacent-difference comparisons rule out all p nonzero modulo 3 (including p=2 by direct residue check); restricting p divisible by 3 to positions divisible by 3 reduces to a square with period p/3. Therefore only p=3^k. Complementary length-L substitution blocks force precise starts i=qL+r: r=0 requires adjacent equal parent letters; r>0 requires a parent triple; cube only at r=0 with parent triple; no fourth power. Recurrence for D(N)=# differences ones proves density 1/2 for changes and 1/6 for parent triples, yielding square density (L+2)/(6L) and cube 1/(6L). Both 0- and 1-triples occur; primitive odd L blocks generate two disjoint length-L cyclic conjugacy classes, hence exactly 2L distinct least-period-L square words. Independent literal comparison on length-19683 fixed point verified square/cube statements and no fourth powers for all periods <=149, part of 5,875,875 cumulative assertions. All-power proof comes from substitution recurrences.

## originality

PASS

The earlier 2022 paper on the same 001/110 word concerns pseudoperiodic matching, which is a different predicate from ordinary repeated equal blocks. The 2003 classical fourth-power-free assertion and known critical exponent are explicitly credited; those coarse facts do not imply which powers of three appear at each start, densities and 2L distinct cyclic squares. Resultary also has a recent antisquare classification on the same word, but antisquares use complementary blocks, not ordinary squares. Searches for synonymous repetition language and period spectrum did not locate same theorem.

## value

PASS

An exact all-period and all-start classification for a canonical automatic word, including positive densities and complete distinct-square factor complexity, is a natural full combinatorics-on-words invariant, rather than another finite sample of factors; triadic rigidity is structurally informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
