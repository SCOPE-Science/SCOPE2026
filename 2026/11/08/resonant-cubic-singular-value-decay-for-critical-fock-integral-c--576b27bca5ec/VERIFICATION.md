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

# Verification of the stated theorem

The proof supplies a monomial-by-monomial exact coefficient and two full asymptotic expansions with nonzero coefficients in all claimed cases; these produce the infinite-dimensional singular-value and Schatten consequences without extrapolating finite computation.

Run `python3 CHECK.py` from the directory containing the extracted file. This standalone standard-library program recomputes exact factorial-normalization identities, the first two logarithmic coefficients, the pairwise cancellation expressions, and selected high-precision evaluations of the commutator weights. It reports 3,932 checks in four categories (1,470 / 98 / 2,352 / 12). Numerical agreement in its last category is only corroborating evidence. No external or independent mathematical audit has been performed.

The paper arXiv:2611.01959v1 provides the precursor normalized critical integral weight formula; this result additionally analyzes the commutator's next two orders. Its claim is restricted to the given integer monomial class. The related 2023 thesis was available in extracted text but its PDF page-image retrieval timed out.
