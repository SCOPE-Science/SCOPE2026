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

The accompanying `check.py` contains a standalone standard-library Python replay. Run `python3 check.py` from this directory. Expected final line:

```text
K4_CYCLE_ISING_CHECKS_PASSED 163
```

The code independently compares the original-hamiltonian 16-state-column min-plus and counting recurrence with the ten-state and five-state negative-subset descriptions at fields \(h/J=3\) and \(h/J=5\) for \(n=3,\dots,9\). It also tests the claimed high-field plateau and saturation, the two integer spectral recurrences and selected magnetization coefficients through \(n=16\), and full labelled spin enumeration for \(n=3,4\) at five fields. A passing replay corroborates only those finite calculations; it cannot certify an all-size proof or historical novelty.

The all-size proof and fluctuation argument are written in `RESULT.md`, based on the exact local nonnegative energy identities, a ten-dimensional invariant-subspace decomposition, and analytic dominant-eigenvalue perturbation. No unproved infinite extrapolation from the finite tests is used.

The underlying publication-priority check is provisional and separate from this verification. Independent scientific audit has not been performed.
