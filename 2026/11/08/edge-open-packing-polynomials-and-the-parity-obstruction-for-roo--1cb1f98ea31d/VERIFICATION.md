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

# Verification of the edge-open-packing formulas

The complete argument is given in RESULT.md. Its critical nonstandard points are (1) that two selected rook edges can share a vertex only when perpendicular; (2) that a selected chain of three edges violates the forbidden-third-edge condition; (3) that distinct components have disjoint row supports and disjoint column supports; and (4) that each perpendicular two-edge path has exactly four choices of pivot for fixed row and column pairs. These points produce a unique component decomposition and the stated factorial identity.

Run `python3 verify.py` with Python 3 and no additional packages. The verifier independently constructs edges in \(K_m\square K_n\), forms the conflict relation by literally checking every possible distinct third rook edge, recursively enumerates all compatible edge subsets, and compares the complete coefficient dictionaries to the closed formula. It checks 15 unordered graph profiles with \(2\le m\le n\le6\). It then checks the sharp size and multiplicity identities for a further 261 profiles with \(2\le m\le19\) and \(m\le n\le24\), using exact integer arithmetic.

Observed output:

```
VERIFY_OK literal_graph_profiles 15 literal_packing_sets 852443 all_coefficients=PASS extremal_formula=PASS additional_arithmetic_profiles=PASS
```

Scope: these are finite, reproducible corroborations. All-order correctness rests on the explicit labelled-block proof, not on extrapolating from computations. No independent validation or machine-checked formal proof has been performed. The polynomial counts edge subsets, not isomorphism classes, and includes the empty set by convention.
