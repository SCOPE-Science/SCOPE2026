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

# Exact verification record

Run `python verify.py` from the directory containing this file. The checker uses only the Python standard library and no network or external data. The actual execution reported `PASS`.

The checker constructs all twenty lines using two independently organized finite-field methods (slope/intercept and pair displacement) and confirms that each pair of points determines exactly one line. It forms the 480 noncollinear triples and verifies 90 bases through each point and 12 through each pair. It then computes all 65,536 signed Walsh multipliers by a complete integer butterfly transform and independently recomputes each one via the exact incidence-moment identity. Both methods agree at every frequency.

The observed zero-weight histogram is six: 960; eight: 4,230; ten: 960; all others: zero. Every weight-six zero passes the unique line-plus-transversal test, and the twenty lines with 48 qualifying exterior pairs each exhaust the 960 witnesses. The full absolute histogram, convolution rank 59,386, smallest nonzero magnitude 4, and sharp endpoint projection kernel numerator 2,232,436 are checked by assertions. The resulting projection constant is \(558109/16384\), and the sharp positive-spectrum condition number is \(120\).

The algebraic first-zero proof and the averaging proof of projection optimality are written in `RESULT.md`. The full finite histogram is an exhaustive computation, not an asserted structural classification in arbitrary affine orders. The verification is same-model only; independent mathematical audit has not been performed.
