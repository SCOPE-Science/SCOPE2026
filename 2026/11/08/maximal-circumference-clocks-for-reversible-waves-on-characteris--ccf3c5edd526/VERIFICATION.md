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

# Verification

The package includes two executable standard-library Python programs and their captured standard outputs. From the extracted package root, execute `python3 verification/check_graph.py` and `python3 verification/check_polynomials.py`. Both completed with `PASS` in this package's preparation.

`check_graph.py` constructs a periodic nearest-neighbor adjacency matrix in the physical coordinate basis, builds the reversible two-layer matrix, and checks exact ranks of powers of \(F+I\) as well as fixed-subspace dimensions of \(F^t\). Its cases include \(d=3\), with up to 256 phase-space coordinates. `check_polynomials.py` independently constructs the same spatial operator in the truncated polynomial basis and checks ranks of every power up to the asserted nilpotency index; it also covers a \(d=4\) case. Neither script uses floating-point arithmetic.

The proof for arbitrary \(d\) is algebraic and self-contained in `RESULT.md`; these finite checks test implementation and representative cases, and their limits are expressly finite. They do not constitute exhaustive enumeration of all possible dimensions or independent external verification. Independent audit status is not_performed.
