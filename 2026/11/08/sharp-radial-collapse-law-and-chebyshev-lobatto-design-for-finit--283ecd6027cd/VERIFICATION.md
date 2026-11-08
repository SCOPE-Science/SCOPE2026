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

The analytic proof specifies the real Frobenius basis, sampled coherent-state normalization, angular DFT block decomposition, rank-one scaled inverse limit, strict asymptotic ordering of other blocks, and weighted Chebyshev equality. Run `python3 check.py` with NumPy from the same directory as this document. The same-model script separately forms all sample rows directly for `\(2\le n\le6\)`, checks exact design constants, near-collapse singular values, positive rank, and randomized radial alternatives; 105 assertions passed in the local verification. Tests are finite and do not constitute an infinite proof. Independent audit and independent mathematical validation have not been performed. Historical priority is provisional; in particular the scalar Chebyshev design inequality is established earlier work.
