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

# Reproducibility and verification

Run `python3 verify.py` using Python 3 and its standard library. The verifier constructs multiplication tables in the finite incidence algebra, independently enumerates its idempotent generators, computes the corresponding inner-derivation matrices and their ranks over \(\mathbb F_2\) and \(\mathbb F_4\), and compares the complete distributions against the theorem. It also enumerates all vertex-color tripartite cuts for \(1\le n\le10\), checking maximal rank and its exact number of colorings.

Executed checks:

```
BINARY_EXHAUSTIVE_OK 1 6 {0: 1, 2: 12}
BINARY_EXHAUSTIVE_OK 2 18 {0: 1, 4: 96, 6: 1024, 8: 2304}
GF4_EXHAUSTIVE_OK {0: 1, 2: 48}
MAX_CUT_ENUMERATION_OK through n=10
VERIFY_OK
```

The finite enumeration supports the small cases only. The general rank polynomial and concentration theorem rely on the six mathematical proof steps in `RESULT.md`. The asymptotic is for fixed \(q\) and does not make a claim uniform in field size. No independent mathematical audit or external verification has been performed.
