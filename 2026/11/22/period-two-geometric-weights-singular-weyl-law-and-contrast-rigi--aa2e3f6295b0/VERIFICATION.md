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

# Verification and scope

The accompanying `checker.py` executed with Python, SymPy, NumPy and SciPy and reported **433 assertions passed**. Exact arithmetic checks cover finite conjugated Cesàro inverses at three rational parameter choices and sizes two through eight. Floating-point checks independently evaluate the symbol singular values, the branch splitting, coefficient symmetries, and finite-section inverse-bidiagonal singular numbers at indices 50, 100 and 200. The proof is not inferred from those finite observations: the uniform infinite-dimensional limit follows from the stated Toeplitz counting lemma and explicit reduction. No independent audit has been performed.

The result assumes the geometric decay parameter is strictly between zero and one and the two periodic weights are strictly positive. It neither certifies an error term at infinite rank nor classifies modulations of periods greater than two. An older general Toeplitz article was located but not read in full; the corresponding historical overlap risk remains.
