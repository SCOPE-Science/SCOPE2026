---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact finite verification

Run `python3 verify.py` and `python3 alternate.py` in the directory containing both scripts and the two certificate JSON files. Both use only the Python 3 standard library. The first checks the full source-language enumeration, codeword distance condition, disjoint complete graph-vertex partition into odd cycles and edges, and exact upper-bound arithmetic. The second checks erasure injectivity separately by coordinate puncturing and checks exact coverage and adjacency using encoded integer states. The expected success terminals are `VERIFY_OK` and `ALTERNATE_OK`; both were observed on the supplied files.

The pairwise minimum-distance property is equivalent to unique decoding of an erasure whose position is supplied. All graph edges used in the upper certificate differ in exactly one coordinate. The certificates cover every state (including across classes) without duplication. For any independent set the maximum contribution of each odd cycle is its half-length rounded down and that of an edge is one. The witnesses attain this bound.

These are complete finite certificates for exactly the two stated lengths. No infinite theorem, unverified search-exhaustion claim, all-length optimum, unknown-location deletion, or independence from future external review is claimed.
