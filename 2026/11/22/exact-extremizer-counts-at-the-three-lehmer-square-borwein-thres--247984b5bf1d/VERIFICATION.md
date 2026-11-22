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

The complete claim is a finite, exhaustive classification with no numerical tolerance. Compile `check.cpp` using a conforming C++17 compiler with integer arithmetic, then run it. The expected final output is:

```text
degree=34 symmetry=0 normalized=2 signed=4 OK
degree=38 symmetry=1 normalized=1 signed=2 OK
degree=41 symmetry=-1 normalized=2 signed=4 OK
TOTAL signed=10; degree-34 is a single reversal/sign orbit; VERIFIED
```

The implementation uses two different control structures, recursive branch enumeration and an integer ternary counter. Both encode all allowed low-degree output coefficients and independently enumerate the entire finite candidate domain. The product check uses all coefficients of \(L^2H\), not only a truncated prefix, and tests exact leading and constant coefficients. An additional coefficient-reversal test identifies the unrestricted orbit. The code includes the five expected quotient vectors and rejects an unexpected vector or a count discrepancy.

The existing minimum degrees \(34,38,41\) are cited results, not independently recomputed by this package. The complete classification at those degrees is proved and reproduced directly here. No external or independent audit has been performed; this is an exact arithmetic check with transparent finite coverage.
