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

# Verification notes

The supplied `verify.py` is a stand-alone standard-library Python checker. Run with `python verify.py` in the directory containing this document. The observed terminal markers were:

```
EXACT_INVARIANT_AND_CYCLIC_MARKOV_REDUCTION_OK
EXACT_CRITICAL_TAIL_AND_CONSTANT_1_OVER_24_OK
FINITE_VARIANCE_DIRICHLET_CONSTANTS_OK
DIRECT_NONLINEAR_ITERATION_AGREES_WITH_CONSENSUS_OK
DIRECTED_MANY_LOCI_VERIFICATION_OK
```

The rational-arithmetic checks establish selected small-dimensional algebraic invariant identities; high-precision arithmetic tests the exact gamma tail expansion; numerical dynamics corroborate convergence to the stationary weighted ratio. Monte Carlo illustrations for \(a=1\) and \(a=2\) are explicitly finite-sample evidence only and cannot certify an infinite-dimensional central limit theorem. The complete analytical proof and its tail/Lindeberg steps are in RESULT.md, including the exact scope and excluded cases.

Independent audit has not been performed.
