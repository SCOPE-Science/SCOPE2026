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

The 90 indexed words have composition (2,2,2); unequal adjacent swaps give the stated graph metric. Radius-one balls are disjoint exactly at minimum distance at least three (use the midpoint of a path of length two in the converse). Independent enumeration checked the listed 18-word construction at distance three and the nine orbits of distance-at-most-two cliques under relabeling and reversal. Their 72 distinct cliques have total integer weight 360 and cover every vertex with integer weight at least 19. An independent set uses at most one vertex per clique, so integer incidence counting gives |C| ≤ floor(360/19)=18. The exhibited code thus attains the optimum.

## originality

PASS

No equivalent fixed-composition Kendall optimum was demonstrated in the bounded searches. The exact Resultary match is the assigned record itself. The distinct deletion-code result has the same domain and value, but not the same channel; the distinct Ulam result uses yet another metric. The original multipermutation Kendall paper is directly relevant but its numerical passage could not be independently retrieved; credit its model and bounds as relevant antecedents without claiming that all possible implications were ruled out.

## value

PASS

This is the first ternary equal-multiplicity setting beyond ordinary permutations: the exact size determines a useful benchmark for correcting one adjacent transposition in a natural constant-composition source. The orbit-weighted integer upper bound closes the size question rather than adding a small improvement in a nonsharp bound, and the explicit witness is a usable code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
