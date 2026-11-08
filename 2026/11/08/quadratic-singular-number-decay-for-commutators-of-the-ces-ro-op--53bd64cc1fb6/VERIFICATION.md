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
# Analytical and finite verification

The analytical proof in RESULT.md establishes \(s_n([C,S^m])\asymp_m n^{-2}\) for every fixed positive integer \(m\), and the exact Hilbert–Schmidt formula, without extrapolating from finite tests. The dyadic upper bound uses rank-\(k\) step approximations of the summation matrix; the lower bound uses zero-total-sum vectors whose images have disjoint dyadic supports. The Schatten classification follows from comparison with the convergent/divergent series \(\sum_{n\geq1}n^{-2p}\).

Run `python checker.py` from the directory containing this file. A successful direct execution printed `CESARO_SHIFT_COMMUTATOR_EXACT_FINITE_OK 20678`. The checker has no nonstandard Python dependencies. It verifies coefficient formulas for truncated matrices, dyadic cancellation and difference inverses with exact fractions, plus finite inequalities against the closed-form Hilbert–Schmidt sum. It does not certify infinitely many cases, singular-value asymptotics, or literature priority.

An exact leading limit for \(n^2s_n\) is neither asserted nor checked. Independent audit has not been performed.
