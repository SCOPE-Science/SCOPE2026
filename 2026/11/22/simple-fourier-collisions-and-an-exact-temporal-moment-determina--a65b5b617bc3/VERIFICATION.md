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

Run `python3 verify.py` with Python 3. The code uses only the standard library and carries out exact rational Gaussian elimination for the single-vertex moment matrices at \(n=2,\ldots,12\), four rational biases, and comparisons with independent direct-pair and cosine-factored products. Resonance uniqueness is checked numerically through \(n=18\). The exact conjugate-gap slope at equal weights is checked numerically through \(n=15\). The test suite contains 173 grouped assertions, each involving one or more comparisons.

These finite checks do not establish the general result. The proof in `RESULT.md` explicitly establishes the all-length parameter classification and determinant. No independent scientific audit has been performed.
