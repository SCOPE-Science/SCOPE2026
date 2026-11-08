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

# Reproducible consistency verification

Run `python3 verify.py` with Python 3.10 or later. No third-party packages are necessary.

The verifier reconstructs utility as the exact rational fraction of occupied cycle neighbors of another type, moves each agent to the unique vacant vertex, and tests for strictly beneficial deviations. It does not call the structural formula as its decision procedure. On the saved package code, the following finite checks passed:

- Direct payoff-versus-characterization comparisons for all \(131{,}064\) two-color profiles with occupied length between \(3\) and \(16\).
- Fixed-composition count checks for \(3{,}159\) positive type-count pairs with total population between \(3\) and \(80\).
- Balanced-count identity checks for every \(m\) from \(2\) through \(80\).
- A full four-site labeled-agent census, including all vacancy choices.

The run-length equivalence, Fibonacci identity, and exponential rate require and receive mathematical proofs in `RESULT.md`; the finite tests alone do not establish any universal or asymptotic statement. The checks are not an independent external audit.
