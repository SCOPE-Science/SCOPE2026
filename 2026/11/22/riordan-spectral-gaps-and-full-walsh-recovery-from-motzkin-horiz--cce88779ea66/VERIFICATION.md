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

# Reproducibility and checks

The attached `verify.py` is standalone and uses only the Python 3 standard library. Run `python3 verify.py` in the extracted directory. In the recorded run it reported `PASS: 18430 exact assertions`.

Direct checks: for each \(0\le n\le12\), recursively enumerate every legal Motzkin excursion (including those of zero length), aggregate its exact horizontal-position mask, compare every multiplicity to the Catalan deletion formula, apply the integer fast Walsh transform to the resulting length-\(2^n\) vector, and compare every Fourier coefficient with an independently implemented nonnegative half-line transfer. Further checks verify thirteen initial Riordan counts and the symmetry, sign/monotonicity and minimum-gap properties of the transfer for every \(n\le60\).

The proof's infinite part is the exact identity \((A+I)(A-I)=A^2-I\), the entrywise nonnegativity of \(A^2-I\), and the central Riordan-path interpretation. Finite checks cannot certify an all-length result by themselves. No external independent audit, formal proof assistant certification, or analytic continuation of numerical observations is claimed.
