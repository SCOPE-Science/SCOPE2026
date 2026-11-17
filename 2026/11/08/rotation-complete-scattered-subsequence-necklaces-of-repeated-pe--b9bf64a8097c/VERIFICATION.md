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

For a linear host (0...q-1)^k, the greedy earliest-occurrence argument uses 1 plus linear weak descents blocks; over rotations a nonconstant circular word has an ascent so the worst rotation uses 1+c(u) blocks, whereas a constant word of length h needs h copies. The trace tr(M_q(z)^h) marks cyclic weak descents; Burnside counts a d-fold repetition by substituting z^d and weights phi(d)/h, with the q correction at h=k. Strictly increasing runs between cyclic weak descents have length<=q, proving h<=q(k-1) and the (2,2) boundary exception. For q>=3 and deficit<=2<q, no false new boundary ascent can occur, so one/two missing-symbol cyclic arc configurations yield the three top-layer formulas. Independently enumerated every query necklace and each rotation against the fixed host for (q,k)=(2,2),(2,3),(3,3), confirming the exact weak-descent criterion, support and top length. All-parameter proof is the structural argument, not finite tests.

## originality

PASS

Published same-day short-deletion necklaces concern a CIRCULAR permutation-power host and output necklaces from deletion masks rather than demanding all rotations occur as subsequences of one fixed LINEAR host. Fleischmann–Germann–Nowotka investigate universality of a host for ALL query words and existence of a favorable HOST rotation; Lyndon-subsequence counting asks about a canonical primitive representative, not all rotations including periodic necklaces. Kosche et al. study bounded-range matching and one circular-host application. These comparisons are not sufficient to imply the exact filtered Burnside formula or the sharp top-three deficit classifications; best-of-knowledge originality passes with inaccessible-paper residual risk.

## value

PASS

A complete natural enumeration of cyclic word classes accepted uniformly across rotations of a fixed periodic host is mathematically motivated by the genuine quantifier distinction between circular matching and fixed-host acceptance. The exact transfer count, sharp maximal support and defect-one/two classification are reusable exact combinatorial data, not arbitrary small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
