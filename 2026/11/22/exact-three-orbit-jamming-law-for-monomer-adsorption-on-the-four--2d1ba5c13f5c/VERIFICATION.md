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

# Verification

The standalone scripts use only Python 3 standard-library integer operations and `fractions.Fraction`, with no downloaded dependencies. Run both programs from the directory containing this file:

```sh
python3 verify_available.py
python3 verify_configurations.py
```

The first program uses recursively memoized residual-vertex masks and verifies the three conditional second-choice distributions and full exact law. The second independently constructs the graph via Hamming distances, propagates exact rational masses over independent accepted sets, enumerates every terminal configuration, and checks all automorphism orbits. Both must print `PASS`. The mathematical argument is finite and exact; no floating point estimate or random experiment substitutes for a proof. No independent scientific audit has been conducted.
