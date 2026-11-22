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

## Reproduction

Run `python3 checker.py` in the same directory as this file. Python standard library only. The checker uses rational arithmetic and independent stationary exponential-flight trajectory simulation. It reports exact four-polynomial excursion identities, the analytic exponential-flight \(2/45\) variance limit for unit parameters, and a direct finite-time simulation comparison.

## Scope of computational checks

The exact rational identities confirm the pathwise primitive on multi-flight sample paths, including both nonzero initial and terminal flight phases. They are not a numerical proof of the nonarithmetic renewal mixing theorem or the moment-cutoff equivalence. Those steps follow mathematically from the stationary equilibrium-cycle construction, the nonlattice renewal limit and length-biased moments given in `RESULT.md`. Finite-time Monte Carlo does not certify the infinite-time weak limit. No independent scientific audit has been performed.
