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

# Reproducibility

Run `python3 verify.py` with Python 3.9 or later; it uses only the standard library. It implements the weighted prism Laplacian and the product Fourier basis from first principles. It evaluates all positive differences between the distinct base-cycle Fourier eigenvalues for every integer \(3\le m\le23\), along with a non-resonant sample, and tests both the eigenvector identities and the PBH ranks for the nested optimal actuator locations. Independently it builds integer Fourier eigenbases for \(m=3,4,6\), groups all their rational resonances, and checks eigenspace independence and optimal-input restrictions by rational Gaussian elimination.

Expected verified output:

```
EXACT_CASES=10 EXACT_PBH_RANKS=56 EXACT_EIGENVECTORS=96
FLOAT_CASES=550 FLOAT_PBH_RANKS=9634 FLOAT_EIGENVECTORS=19154
VERIFY_OK
```

Finite numerical checks group eigenvalues within \(10^{-9}\) and test ranks with tolerance \(10^{-8}\); these are consistency checks and cannot rule out unexpected infinite-parameter behavior. Exact small-instance checks use `fractions.Fraction`. The universal mathematical certificate is the Fourier decomposition and the three explicit restriction-matrix determinant calculations in `RESULT.md`. No independent audit or external theorem certification has been performed.
