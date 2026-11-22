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

# Verification record

The proof follows from the explicit moment identity, the exact rational-angle kernel, an analytic Schur-complement reduction, and a geometric conditional-variance calculation. The latter is not inferred from numerical data.

Run `python VERIFY.py` using Python 3 and NumPy. The checker evaluates the complete finite Gram matrix, confirms resonant nullity and the positive hard spectrum, computes the predicted moment-matrix soft eigenvalues separately, and compares the normalized small-angle soft spectra and sharp condition numbers over all coprime fractions with denominators \(2\) through \(5\), every admissible redundancy, and three sample geometric weights, with perturbations of both signs. It also tests exact rational cases at denominator \(2\). A direct replay produced `PASS: 768 assertions`.

The numerical checks do not cover arbitrary denominators, weights, or asymptotically small angles, and are not an independent proof. The quoted \(O(|\varepsilon|^3)\) error is justified analytically by the finite-dimensional Schur complement. Publication priority and independent audit remain unperformed.
