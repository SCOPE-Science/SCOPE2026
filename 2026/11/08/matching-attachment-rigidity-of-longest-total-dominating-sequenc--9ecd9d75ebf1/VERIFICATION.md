---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

After an edge-selection prefix in the underlying complete graph, the undominated vertices of its line graph are exactly edges among unused ground vertices plus isolated selected-edge components. Distinguishing A,B0,B1,C1,C2 legal moves yields conservation L=n-u-b1-c2; a completed sequence has u in {0,1}, and the transition to a first nontrivial component forces L<=n-1, with equality only odd n and near-perfect-matching/attachment structure. Explicit even construction attains n-2; rooted contracted-tree order realizes each odd support. Matching and attachment choices count n!(n-1)!/2^m without overcounting ordered sequences. Independently computed open-neighborhood bitset dynamic-programming maximum length and number for n=3..8, yielding odd counts 6,720,453600 and matching length at each n; finite DP is corroboration only.

## originality

PASS

The exact longest open-neighborhood sequence classification and ordered enumeration for the triangular graphs are distinguished from minimum total dominating sets and longest sequences on their Kneser complements; assessed original on substantive comparison, with unindexed-literature risk.

## value

PASS

The maximal legal open-neighborhood domination length and complete equality-pattern/ordered census are natural structural invariants of a highly symmetric graph family, not a short parameter substitution. The matching-to-spanning-tree support bijection supplies a useful combinatorial characterization beyond a scalar maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
