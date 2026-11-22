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

# Verification scope

The exact polynomial identity was checked over all \(5^4=625\) rational grid points in four amplitude variables. Each variable has polynomial degree at most four, so this is an exact identity check by polynomial interpolation, not an extrapolation from finite data. The relative phase-deficit term is nonnegative by the elementary complex inequality \(\operatorname{Re}(z\bar w)\le|z||w|\). The complete upper bound and optimizer classification are proved analytically in `RESULT.md`.

`checker.py` uses only Python 3 standard-library modules (`fractions`, `itertools`), constructs rational Walsh block optimizers in dimensions \(4\) through \(24\), verifies all entries of their column Gram matrices, and checks the sharp value and comparison identities. Run `python3 checker.py`. These computations are reproducibility checks, not substitutes for the all-dimension argument. The source moment formula is separately reconstructed in the written proof and corresponds to arXiv:2610.02843 Appendix A.

Independent mathematical auditing is not performed here.
