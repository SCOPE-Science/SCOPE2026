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

# Reproducible mathematical checks

Execute `python3 VERIFY.py` with Python 3, NumPy and SciPy in the directory containing the extracted checker. Its observed successful output was:

```
EQUATOR_JET_PASS exact_assertions=22848 direct_matrices=176 max_spectral_error=1.47e-14
```

The first group tests integer/fraction formulas and rank/alias counts over degrees \(1\le\ell\le64\) with numerous positive node counts. The separate matrix construction evaluates normalized spherical harmonics and their actual colatitude derivatives with SciPy through degree eleven, and compares the complete Gram eigenvalue lists with the analytic classes for every tested grid size. A reported finite test is not a substitute for the all-degree analytic proof: the source of the theorem is Legendre parity and exact amplitudes, Fourier orthogonality, residue arithmetic, and monotone factorial ratios in `RESULT.md`.

# Scope, limits and review status

The theorem covers exact-degree spherical harmonics on the two-sphere and equispaced equatorial value/meridional-derivative data at precisely the stated relative scaling, not a general multidegree or nonregular sensor theorem. Historical priority remains bounded by the listed accessible literature. Self-review: passed. Independent audit: not yet performed.
