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

# Verification and reproducibility

`brute_check.py` and `transfer_certificate.py` are standalone standard-library Python 3 scripts. Invoke them with `python3 brute_check.py` and `python3 transfer_certificate.py` from the same directory. Their expected outputs are stored verbatim in `brute_output.txt` and `transfer_output.txt`.

The direct checker enumerates every three-position deletion, reading the actual erased pattern, for all sixteen pattern/phase possibilities across source lengths 3 through 24. Its 176 pattern-and-host cells (with bit-complement phase comparisons) match the theorem. Enumeration proves only these finite cases.

The second checker determinizes the eight-state epsilon-NFA of the proof, reports actual state transitions and terminal-state sets, verifies the first four coefficients for both source parities, and checks 148 exact integer fourth-difference identities across eight patterns and two parity classes. The full theorem follows from the abstract, human-readable automaton equivalence and the finite-dimensional Cayley–Hamilton recurrence: if a scalar matrix-powered sequence has its first \(q\) terms zero for a \(q\)-state matrix, the entire sequence is zero. The arithmetic is over unbounded Python integers, not floating point.

Scientific limits: arbitrary nonalternating sources and patterns of other lengths are not addressed. Code is a checkable exact finite computation, not independent external validation; an unindexed earlier equivalent remains possible.
