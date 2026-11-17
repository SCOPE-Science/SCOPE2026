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

# Reproducibility

Run `python3 verify_oneway.py` using Python 3 standard library. The program directly computes all functional-graph cycles for ring lengths 5 through 14 and compares fixed-point counts and global orders with the symbolic formulas. It completes with `ALL FINITE CHECKS PASSED`.

Counts of labelled states checked across these lengths: 32,736. At ring length six the global recurrent order is six, while individual primitive orbit lengths are only one, two, and three; at ring length ten the order is ten and individual periods only one, two, and five. This corroborates the stated nonattainment phenomenon.

The proof does not depend on the computation: it uses the coordinate identity, monotone domain walls, a four-state transfer, and finite-order arithmetic. Independent validation and comprehensive historical priority examination have not been performed.
