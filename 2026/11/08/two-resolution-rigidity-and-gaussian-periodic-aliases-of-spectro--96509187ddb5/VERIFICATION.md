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

# Mathematical verification
The proof establishes the claim for all strictly positive continuous polynomially upper-bounded spectral densities, not just the numerical example. Its critical nonstandard steps are the Gaussian Laplace-transform shift identity, the global finite-difference equation for \(\log S\), and the growth-driven exclusion of a nondecaying exceptional branch.

Execute `python CHECK.py` in the same directory. The checker uses only the Python standard library; it verifies the exact parameter compatibility \(k_1-k_2=h\), \((a+c_1)k_1=(a+c_2)k_2\), independently integrates \(I_c=2c\operatorname{Var}\) at the two designated widths for a smooth nonconstant periodic example, checks that a third width generally distinguishes the example, and compares against the closed Gaussian formula. It does not certify the infinite-domain statement, which is proved by the argument in `RESULT.md`.

Independent audit: not performed. No statistical reconstruction, finite-sample stability, or coverage of possibly vanishing spectra has been asserted.
