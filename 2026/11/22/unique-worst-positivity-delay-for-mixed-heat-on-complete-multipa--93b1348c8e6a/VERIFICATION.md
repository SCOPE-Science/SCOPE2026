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

The analytic proof in `RESULT.md` establishes the general assertions. The accompanying standalone standard-library Python checker `artifacts/verify_mixed_multipartite.py` independently constructs the graph matrix and exponential, compares all entries with the claimed spectral formula, tests signs on both sides of the recovery time, and compares the optimized formula and limits.

Executed command:

```sh
python3 artifacts/verify_mixed_multipartite.py
```

Recorded output:

```text
VERIFY_OK matrix-entry-comparisons=19560 parameter-checks=1152 limit-tests=16
```

Finite tests are consistency checks rather than proofs of the all-graph theorem. The zero-time nonnegative identity, positive-time off-diagonal entry cases, positivity threshold and strict uniqueness of the optimizer are handled analytically. Other graph topologies, arbitrary conductances, and other generators are not verified by this package. No independent mathematical audit has been performed.
