---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

A recovery set R for coordinate i exists iff the coordinate functional factors through the projection to R, hence iff a dual word is supported on R union {i} with nonzero coefficient at i. The given dual distance 4 makes minimum recovery size 3, and each such support is a published weight-4 block. Puncturing all 4-blocks containing i in a 3-(q+1,4,lambda) design produces exactly the derived 2-(q,3,lambda) design. Standard t-design counting yields b=lambda*q*(q-1)/6, r=lambda*(q-1)/2, pair multiplicity lambda. Inclusion-exclusion for blocks meeting E of size3 yields at most 3r-3lambda+1, and greedy selection guarantees ceil(b/(3r-3lambda+1)) disjoint triples. Independent arithmetic confirms q=9,25,81 formulas. The mathematics is correct given the cited source’s code and design hypotheses; full source proof of those premises not re-audited in this run.

## originality

FAIL

The claimed derived design, local multiplicities, and crude greedy matching bound are direct textbook consequences of the exact 3-design and dual minimum-distance facts already stated by Xiong–Wang–Zheng–Ji. Their source even uses these supports for all-symbol locality 3. No additional code-specific construction or unknown non-implied invariant survives; different recovery terminology does not produce an original structural theorem.

## value

FAIL

Although balanced repair hypergraphs are important, once the source proves the complete weight-4 3-design, passage to a 2-design through a point is an elementary standard derived-design construction. The repair count and greedy lower bound use only two universal parameters and make no additional code-specific calculation or optimal availability classification. Because everything is automatically determined by the known stronger source, this package adds no sufficiently motivated independent mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
