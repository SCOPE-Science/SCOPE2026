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

# Verification record

An analytical proof appears in `RESULT.md`, including the moment-ratio and strict Laplace-transform inequality steps. Its hypotheses require positive rate, equal numbers of both sexes, independent lifetimes, reusable male mating, and independent pairwise Poisson encounters. The strict order is for nonconstant lifetimes and count thresholds at least two; the zero-mating event is tied. Degenerate lifetimes and one-pair populations have identical full count laws.

The standalone `check.py` is executable with Python 3 without additional packages. The command `python check.py` completed successfully, printing `EXACT ASSERTIONS: 13754`. It uses exact rational arithmetic on reproducibly sampled finite-support laws for \(e^{-aT}\). Its exhaustive enumeration is over the specified test cases only and is not an exhaustive test over lifetime distributions or a substitute for the general analytical argument. No external independent validation has been performed.
