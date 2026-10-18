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

The one-deletion-plus-at-most-s-substitution output set includes the Hamming radius-s ball of the fixed last-coordinate deletion. Distinct correcting codewords must therefore have punctured prefixes at Hamming distance at least 2s+1. At n≤2s+1 the prefix length n−1≤2s forces M=1; at n=2s+2 the prefixes differ in every one of the 2s+1 coordinates, so the first symbol injects the code into a q-element alphabet, giving M≤q. The q constant words have disjoint descendant Hamming balls at radius s and attain M=q. Independent literal output-ball enumerations covered q=2,3 and s=0,1,2, with all correct short-block pair-compatibility tests (finite corroboration only). The quantifiers include s=0 and n=1.

## originality

FAIL

This exact boundary is an immediate coding-theoretic corollary of the classical q-ary Hamming/Singleton bound after the obvious common-position puncturing: the necessary punctured Hamming code has length n−1 and distance 2s+1, hence at boundary at most q words, and constant codewords trivially attain it. The first-length feasibility obstruction needs no deletion-specific lemma beyond a one-line inclusion of one puncturing output ball. Thus although the channel is a legitimate model and primary combined-error papers do not print these exact short-block numbers, the entire finding is mathematically covered by an elementary specialization of established Hamming theory; changed terminology or n,s parameters do not establish originality.

## value

FAIL

The first feasible length is a natural model parameter, but here both sides of the proposed “sharp threshold” collapse through routine prefix puncturing, classical Hamming sphere separation/Singleton, and repetition. There is no new structural characterization of deletion overlap, nontrivial extremizer classification, or threshold mechanism beyond that textbook reduction. Under the same standard used for other elementary deductions, correctness and all-parameter notation alone do not make this independently worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
