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

# Verification and limits

The analytical proof constructs the full singular spectrum through finite-dimensional principal-angle blocks and all bosonic occupation degrees. The exact \(S_2\) formula is the sum of convergent geometric series when the common intersection is trivial. The essential-norm equality in the noncompact case is proved using an infinite vacuum/occupation tensor factor, not by extrapolating finite experiments.

Run `python3 checker.py` in the same directory as this document. It requires only the Python standard library. Successful execution gives:

```text
FOCK_PROJECTION_PRINCIPAL_ANGLES_EXACT_OK 1705 rank_one_c=3/5 two_angle_S2_squared= 480625/100368
```

The checker uses exact rational matrix multiplication on the homogeneous polynomials in two variables, including their diagonal Gaussian monomial Gram weights, to verify projection identities, the commutator cubic identity, and the two repeated singular-value squares for degrees \(1\) through \(12\). It then verifies truncated two-angle occupation generating functions for degrees up to \(19\). These are finite checks of proof identities, not exhaustive verification of infinitely many degrees or independent scientific validation.

The inspected primary literature establishes ordinary composition-operator theory and prior qualitative compact-difference conditions. Its possible earlier quantitative overlap, especially in older inaccessible articles or general second-quantization treatments, is a stated publication-priority risk.
