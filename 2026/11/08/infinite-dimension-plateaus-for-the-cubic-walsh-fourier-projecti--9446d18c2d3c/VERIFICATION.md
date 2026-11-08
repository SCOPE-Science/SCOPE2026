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

# Verification of the cubic Walsh projection plateau theorem

The finite-group convolution representation is checked in the proof, rather than assumed from a numerical norm estimate. The identity for the expected absolute value after adding one independent sign reduces the difference to a nonnegative explicit binomial sum. For parity-sensitive equality, the proof uses exact polynomial factorization and an exhaustive interval argument valid for every dimension.

The included standard-library Python checker (`verify_cubic_walsh.py`) was run from the actual packaged source. It verifies exact direct sign enumeration for dimensions 3 through 10, exact binomial-sum evaluations and consecutive-dimension differences for every dimension from 3 through 180 (evaluating the norm at dimension 181), the positive-part identity, and the predicted seven plateau indices in that finite range. Its observed output was:

```text
CUBIC_WALSH_PLATEAU_PASS brute_dimensions=3..10 exact_n=3..181 plateaus=5,21,33,65,85,133,161
```

The checker uses exact Python integer and rational arithmetic; no floating-point thresholds, external certificates or hidden data are required. Its finite tests cannot certify the infinite theorem; the latter follows from the independent written proof. No independent mathematical audit has been performed.
