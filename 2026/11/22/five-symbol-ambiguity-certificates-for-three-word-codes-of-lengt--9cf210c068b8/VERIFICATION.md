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

For z=abc the only possible initial Sardinas–Patterson residual is c, requiring ab in X. A one-letter residual follows the edge p→q from each short word pq. Its only possible transition to length two is a→bc by stripping a from z. If z is nonconstant then bc differs from ab, so bc cannot be cancelled from the front of z; nor can it make any transition with a length-two word other than equality. Thus nonconstant ambiguity requires bc in X and reachability of a from c using the two edges a→b and b→c. This holds exactly when c=a (if c=b≠a the only outgoing edge from c loops; otherwise c outside {a,b} is a sink). If z is constant, aa in X suffices and is necessary by the initial prefix test. The displayed concatenations give witnesses of length five; no shorter length has two distinct feasible length patterns or more than one factorization with a fixed pattern. Counting the disjoint families as unordered short-word pairs gives q(q−1)(q+2) and the stated probability.

## originality

PASS

Pass the explicit two-pattern classification with the uniform sharp five-letter witness and closed labeled count, not the decision algorithm or general study of three-word decipherability. The 2001 family is a real scope overlap; no inspected statement establishes equivalent structural or witness coverage for this profile. The limited access risk is material and remains open.

## value

PASS

The smallest mixed-length profile with two distinct shortest words, no one-letter words, and a longer third word gives a natural test case for witness length. The surprising absence of any codes whose first ambiguity appears after length five is stronger than a routine test of an individual codebook; the complete failure locus also gives the baseline random-codebook failure rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
