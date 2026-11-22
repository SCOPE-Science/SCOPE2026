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

Run `python verify.py` using Python 3.10 or later; only standard-library modules are used. Successful replay reports 417 checks and prints the optimal rung probabilities for selected graph sizes.

The program independently inverts exact rational matrices \(I-P+J\), compares them against the rational closed form when \(\sqrt b\) is rational, verifies the published unweighted Kirchhoff table for small graphs, checks Fourier-mode identities and derivatives, and evaluates several asymptotic instances. Exact rational equalities are exact computations; floating-point comparisons use explicitly bounded tolerances.

## Scope and limitations

Checks cover finitely many graph sizes and parameter values. Strict convexity, global uniqueness against asymmetric competitors, the strict all-size inequality, and the sharp asymptotic coefficients are established analytically in `RESULT.md`, not inferred from the tests. Source comparison does not certify publication priority; independent mathematical audit has not been performed.
