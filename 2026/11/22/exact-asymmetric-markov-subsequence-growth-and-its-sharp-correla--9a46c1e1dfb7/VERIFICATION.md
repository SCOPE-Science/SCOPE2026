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

The expectation is of distinct nonempty subsequence strings, with stationary transition parameters \(0<p,q\le1\) and arbitrary source length \(n\ge0\).

Actual checks: executing `python verify_markov.py` with SymPy available returned three PASS assertions: 67 positive rational parameter pairs, 603 independently enumerated expectation comparisons, and 68,474 weighted host strings; exact agreement of the four-state expectation recurrence with the scalar rational generating function; and exact symbolic equality for the characteristic polynomial, transfer determinant, and rational numerator. The enumeration uses a set of strings, not an embedding count, and exact fractions for every Markov probability.

Proof coverage: the state recurrence is derived from the deterministic subsequence update; exact matrix identities are stated and can be recomputed; Perron–Frobenius theory establishes the exponential root for strictly positive transitions, including the explicit alternating endpoint; implicit differentiation proves strict monotonicity and the maximizing boundary. The finite computational checks are corroborating evidence and are not an infinite proof. The result makes no claim about sample-path almost-sure limits or distributions of the count.
