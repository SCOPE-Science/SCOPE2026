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

Run `python3 check_theta.py` in the directory containing `theta_spectra.csv`. It uses the Python 3 standard library only, enumerates all \(22\) partitions of eight, traverses \(28\) two-subsets and \(35\) unordered four-plus-four partitions independently from a cycle generating-function formula, and verifies all first-three-extension signatures, exact orbit spectra and listed collisions.

Actual successful execution output:

```
THETA_GENUS_THREE_THREE_EXTENSION_INJECTION_VERIFIED
22 partitions; 19 odd spectra; 21 even spectra; 19 two-level fingerprints; 22 three-level fingerprints
```

The finite certificate checks all conjugacy types; the deduction for all odd finite fields additionally depends on the algebraic theta-subset identification and the existence of irreducible polynomials of every positive degree over each finite field. Tests by themselves do not establish those geometric facts. The complete cycle spectra are encoded in `theta_spectra.csv`, where each string `d:m` means \(m\) Frobenius cycles of length \(d\).

No independent audit or independent mathematical validation has been performed.
