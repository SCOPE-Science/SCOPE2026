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

The delivered `verify.py` was run using the Python standard library and emitted `PASS 36 checks`. It exhaustively enumerated all bond-retention states for rim sizes \(3\) through \(7\), calculating exact rational probabilities by connected-components union-find and comparing against the finite reliability and tagged-component formulas. It tested the two-parameter continuum formulas at five finite sizes and multiple boundary parameter choices, the nested high-cut regime at nine parameter pairs, and a seeded 50,000-trial Poisson-circle experiment for consistency with the analytic mean and connectivity probability.

The simulation is statistical, and the finite enumeration is not an exhaustive infinite proof. The proofs of the global statements appear in `RESULT.md`, including the logarithmic coefficient identity, Poisson point-process convergence, Gamma tagged-interval distribution and nested-limit exponent. No independent audit or external certification has been performed.
