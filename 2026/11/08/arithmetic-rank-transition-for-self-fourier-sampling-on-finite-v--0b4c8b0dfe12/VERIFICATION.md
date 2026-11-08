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
# Reproducibility and limits

Run `python verify_half_veronese.py` with Python 3 and NumPy. The checker creates each finite-field multiplication table directly, including explicit quadratic-extension models, enumerates all projective Veronese points, builds the entire Fourier sampling matrix entry-by-entry using the determinant-polar form, and compares independently computed singular values against the proposed multiset. It tests the six complete matrices for field orders \(3,5,7,9,11,25\), confirming the numerically predicted rank defect at order \(25\). It separately calculates Gauss periods for \(\mathbb F_{169}\) and checks the trace-line exclusion and six predicted zero periods; the full matrix is too large to construct as a routine check.

The program checks numerical spectra up to a reported floating-point tolerance; its computations do **not** establish universal invertibility, a lower bound valid for all primes, or an exact rank. Those conclusions follow instead from the explicit proof and (for the exact order-\(25\) nullity beyond the lower bound) the cited exact published Gauss-sum table. The reported self-review does not constitute independent verification.
