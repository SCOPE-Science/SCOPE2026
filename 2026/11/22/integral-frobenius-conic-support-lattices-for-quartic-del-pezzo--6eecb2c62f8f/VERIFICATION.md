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

# Reproducibility and boundaries

The standard-library Python 3 verifier is `verify.py`; it requires the co-located `cases.csv` and no network access or installed mathematics package. Run `python3 verify.py` from the extracted directory. It recomputes the sixteen exceptional-curve classes, ten conic pencils, their precise component incidence and the full eighteen-row integer Smith classification for every even-signed permutation of five labels. It checks the exact geometric Smith diagonal, the completeness of each Weyl conjugacy class, and the positive five-cycle \(4\)-by-\(2\) integer orbit-sum matrix. The observed run produced four `PASS` lines followed by torsion counts for 11, 6 and 1 conjugacy classes.

An additional separate local cross-check using `sympy.matrices.normalforms.smith_normal_form` for one representative of all eighteen signed-cycle types agreed with the verifier's integer diagonals. That optional library is not needed to reproduce the included proof checker.

The enumeration of all \(2^4\cdot5!=1920\) Weyl elements is exhaustive; the theorem's extension to any finite-field surface follows from classical geometric descriptions of the sixteen exceptional curves, ten conic pencils and their Weyl Galois action. It does **not** follow from sampling field rational points. The verifier does not classify the existence of all types over particular fields, nor does it assert that this formal incidence torsion is Picard/Brauer torsion. Literature originality is provisional, and independent mathematical audit is not yet performed.
