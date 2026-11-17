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
The self-contained script `check_harmonic_commutators.py` ran with the standard Python interpreter. Observed output:

```
EXACT_ITERATED_COMMUTATOR_AND_HARDY_POWER_DOMINATION_PASS n1_to22 orders0_to5
NEAR_EXTREMIZER_RIEMANN_SUM_CHECKS_PASS p1.5_2_3 orders0_to3 N1000_10000_100000
ALL_HARMONIC_CESARO_CHECKS_PASS
```

The exact-rational portion independently expands the diagonal commutator, constructs \(C^{r+1}\), and verifies all matrix-entry identities and domination inequalities for the indicated finite cases. The numerical portion checks the predicted approach to sharp logarithmic Riemann-sum constants for the indicated parameter samples. Exact finite checks are not infinite proofs and numerical lower bounds do not certify operator norms. The full proof requires the general tuple-sorting inequality, the classical Hardy theorem, controlled improper Riemann sums, and the compact-adjoint tail argument given in `RESULT.md`.

The abstract norm \(\|\cdot\|_{\mathrm{ess}}\) is distance to arbitrary compact bounded maps on \(\ell^p\), not just to finite matrices. The proof uses tail projections to address this entire compact class. The unbounded multiplier is defined only on its natural core; no illegal bounded-operator commutator identity is presumed.
