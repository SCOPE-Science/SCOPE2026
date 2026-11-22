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

Exact symbolic checks, using Python 3 and SymPy, were run with the standalone `verify_volterra.py` file in this package. All 205 assertions passed: both triangular expressions of the integral kernel coincide; ranks and high-degree antidiagonals agree for all 25 pairs of integers from one to five; self-commutator determinant, characteristic parity and reflection identities hold at the first five orders.

The analytical derivation, not the finite symbolic range, establishes the arbitrary-order theorem. In particular, the finite checks do not imply that all integer orders have been exhaustively computed. Exact arithmetic and the stated formula for the Hilbert matrix determinant suffice to reproduce the symbolic certificates. No independent mathematical audit has been performed.
