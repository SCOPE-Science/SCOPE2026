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

# Verification details

The proof derives every Fourier coefficient of the two canonical finite-field line arrangements from character orthogonality and inclusion–exclusion. The exact operator norm follows from convolution and a complex input saturating the row sum. The strict inequality is established analytically for all prime powers, with exact binary and ternary boundary checks.

Run `python3 checker.py` using Python 3 and its standard library. Direct transforms agree with the claimed closed expressions for the nine fields of orders 2, 3, 4, 5, 7, 8, 9, 11, and 25. The checker also exhausts all arrangements of three distinct line directions and offsets at orders 2, 3, 4, and 5 (3,256 arrangements). The finite list alone would not certify the arbitrary-field theorem; its role is to test the normalization, elementary sums, and field arithmetic.

The original 2026 motivating article and relevant existing general Fourier-algebra/coset theory were inspected. The closest indexed same-object sampling and three-step-walk reports could not be retrieved as complete source documents, and searches do not establish uniqueness. Independent review remains unperformed.
