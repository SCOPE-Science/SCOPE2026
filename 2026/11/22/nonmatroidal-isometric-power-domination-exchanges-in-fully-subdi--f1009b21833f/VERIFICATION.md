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

## Checks performed

The standard-library Python program `check_enumerator.py` directly enumerates every sensor subset and simulates the power-domination process for orders three through five. It independently enumerates labeled forests, reconstructs the complete polynomial and compares all coefficients. It then enumerates all optimum sets from the two proved types for orders three through nine, constructs the exchange graph, computes all-pairs shortest distances, and checks exact degrees, edge counts, eccentricities and Johnson isometry.

The C++17 program `check_forest.cpp` independently constructs incidence graphs and applies synchronous propagation to every one of the \(2^{n+\binom n2}\) subsets for \(3\le n\le6\). In particular, the order-six comparison covers all 2,097,152 initial configurations, and each case agrees with the residual acyclicity test. The final outputs of both scripts report PASS.

## Scope and limitations

These are finite exhaustive checks only at the stated orders. The all-order claims are justified by the cycle-obstruction, forest-peeling, optimum-classification and explicit exchange-path proofs in `RESULT.md`, not by extrapolating finite data. No independent scholarly or formal verification is asserted.
