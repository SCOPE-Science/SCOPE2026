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

# Computational verification and limits
Run `python -m pip install -r requirements.txt` and `python check.py` in a directory containing those two files. The program builds each Fourier Gram matrix from exact integrated trigonometric moments, obtains high-precision eigenvalues, and compares against the *independently coded* Legendre coefficient for degrees \(1\)–\(5\) and several angles. It checks the antipodal closed-form coefficient and strict coefficient optimality, and samples finite-width angular competitors in the lower degrees. Its reported output on the packaged code is:

`NARROW_TWO_ARC_CHECKS_PASS 112`

The finite computations are not an exhaustive proof over all degrees or arc widths. The analytical proof in `RESULT.md` supplies that argument. Historical originality comparison is necessarily provisional. Independent mathematical validation has not been performed.
