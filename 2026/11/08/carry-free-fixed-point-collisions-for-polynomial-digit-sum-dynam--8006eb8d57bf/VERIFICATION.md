---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

From g(Y+a-1), coefficient positivity and the leading monomial guarantee the sum of all coefficients other than any specified one >=a; hence every coefficient <=g(a)-a=b-1. Because g(a)=b+(a-1), its base-b digit sum is a. Substitute Y=b: g(g(a)) is carry-free and its digit sum equals g(a). Differences exactly b-1 imply separate fixed cycles and non-injective semiconjugacy; square-progression expansions in RESULT.md each have legal digits and give disjoint residues 4,7 mod9. Recomputed exactly 2880 polynomial/base examples and 200 progression examples. These finite tests corroborate algebra, not infinite validity.

## originality

PASS

The uniform all-polynomial carry-free collision and positive-density square-map progression theorem go beyond the primary source’s arithmetic semiconjugacy and finite base tables. Earlier generalized Dudeney fixed-point bounds treat fixed bases and do not imply the constructed varying-base families. Resultary hits for positive-density digit-sum products concern a different map n*s_b(n), not s_b(g(n)). Unindexed equivalent constructions remain possible.

## value

PASS

The finite tables and open base-dependence problem are naturally strengthened to a constructive obstruction for every positive polynomial generator and positive lower density in the square case, showing a structural failure of residue-class basin decomposition rather than one isolated counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
