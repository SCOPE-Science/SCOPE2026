---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Each binary four-bit vertex has two incoming and two outgoing edges, so a cyclic Euler traversal determines one of two local bijections at each vertex. Conversely any set of these choices gives a permutation of the 32 edges, and a single orbit is exactly a de Bruijn cycle; its unique 00000 factor gives one canonical start per rotation class. The terminal convention counts a repeated final suffix once and is implemented consistently. An independently written exhaustive Euler traversal rooted at 00000, checking all 32 circular factors on every representative, yielded 2,048 cycles. Independent set and trie parses agreed on the complete phrase sequences of all 65,536 cuts. The six bins in displayed order were (6,44,746,1172,30,50), and the canonical counts for 11–14 phrases were (18,480,1508,42). The regenerated sorted 2,048-row certificate matched the attached file byte for byte. Replay: branches/6e838f3b-fbd3-44ff-94c0-0497be5e9f33/audit.py and audit-order5.txt. This establishes the exact finite findings, not any other order or end convention.

## originality

FAIL

A distinct indexed record, 80a175d8f1ba, has the exact same six cycle-level bins and computes the stronger data of all 32 counts in rotation order from each canonical 00000 cut. The anchored histogram is a projection of those rows. This is demonstrated equivalent and stronger coverage in the existing catalogue. The overlapping entry's displayed path date, 2026-11-02, is later than the frozen path date, 2026-10-26; the evidence does not establish earlier publication, independent origin, or direction of provenance. The decision is about distinct scientific coverage, not credit for priority.

## value

FAIL

This is a meaningful finite benchmark in principle: all cycles have the same circular five-bit frequencies, yet the parsing count can change when the root changes. Order five is the first of orders 1–5 with nonconstant cycle maxima (the separate lower-order benchmark in review_evidence/lz78_orders_1_to_4.mjs gives only maxima 2, 3, 5 and 8 respectively). However, as a separate finding the precise frozen outputs are covered by the existing all-root data; the extra anchored histogram is a single-coordinate tally, not an independently valuable uncovered remainder. No repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
