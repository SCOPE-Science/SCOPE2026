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
# Verification notes

The standalone `verify.py` uses only the Python standard library. It constructs double-star host edges, derives the two-token graph by the symmetric-difference rule, finds a maximum matching with a generic augmenting-path search, and tests each theoretically specified maximum independent configuration. For the nine boundary pairs with \(1\le a,b\le3\), an independent bitset recursion computes the exact optimum and number of maximizers without using the structural proof.

Run with `python3 verify.py` and compare with `verify.log`. The log records 64 matching-size checks, 81 constructed optimizer checks and nine independent exhaustive optimizer counts. These tests do not establish the unrestricted theorem by enumeration; the exact all-parameter matching, cover and uniqueness arguments are in RESULT.md.

No external or independent validation is claimed.
