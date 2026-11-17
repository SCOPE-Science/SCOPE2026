---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

An odd XOR label sum around a cycle forbids shattering. On each forest component, every edge labeling induces exactly two complementary vertex-bit assignments; component sizes determine possible cardinalities. Cayley’s formula enumerates tree-shaped supports. Balanced component colorings give |S|≤2min(k,n−k), and a 2r-leaf star attains it when n≥3r+1. The subset-sum gap argument for small forests is valid.

## originality

FAIL

A November 2 theorem proves the identical all-support forest component-size criterion and stable VC dimension for same-block (XNOR) edge queries, which differ only by Boolean output complement from cut (XOR) labels.

## value

FAIL

The central all-cardinality forest shattering criterion and exact stable range are known. The displayed integer-partition face sum is a direct Cayley-counting reformulation of that established full support classification and is not an independently motivated unknown fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
