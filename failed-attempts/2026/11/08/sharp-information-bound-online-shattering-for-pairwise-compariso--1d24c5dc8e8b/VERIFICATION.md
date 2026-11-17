---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For all strict total orders on n labeled elements with pair-comparison instances, a fixed query support is VC-shattered iff its undirected graph is a forest; so VCdim=n−1, including n=1. A depth-d complete adaptive mistake tree requires 2^d distinct hypotheses, giving Ldim<=floor(log2(n!)). The actual complete `order_certificates.json` contains depth 1,2,4,6,9 trees for n=2..6; every internal queried pair and all 2,4,16,64,512 leaf witness permutations were independently checked against full root-to-leaf answer histories, with no duplicate witness and correct hypothesis counts. This is exhaustive finite certificate for only n<=6, not an induction or claim for larger n. The n=1 value is zero.

## originality

FAIL

The earlier complete 2026-11-02 Resultary theorem "The seven-item entropy obstruction for adaptive permutation comparisons" treats the exact SAME concept class, query domain, bit convention and definitions. It proves VCdim=n−1 and exact Ldim values (0,1,2,4,6,9,11) for n=1..7; in particular it supplies the identical six-item 512-leaf lower witness and cardinality upper bound, and strengthens the submitted theorem with seven-item obstruction and unbounded gap. Complete earlier primary RESULT.md inspected. The submitted six-item table is a strict special case and cannot be new.

## value

FAIL

Exact finite comparison dimensions for a natural hypothesis class would be independently useful if unknown, but all submitted numbers, witnesses and VC characterization already appear in the stronger 2026-11-02 result. A reassembled 512-leaf certificate and a narrower table are known-table recomputation rather than a distinct mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
