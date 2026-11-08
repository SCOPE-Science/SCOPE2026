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

# Direct finite-field verification

`verify.py` constructs the algebra's multiplication table in its standard monomial basis and calculates all powers and ranks using its own finite-field row reduction. It does **not** implement Smith normal form and does not use the predicted matrix diagonalization to perform the direct tests. It compares the resulting complete partition histograms with predictions from the theorem.

The test covers the nine pairs \((m,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)\). Every nilpotent element is tested in each finite example. The quadratic extension \(\mathbb F_4\) is represented by a polynomial modulus \(z^2+z+1\). The included output ends with `WIDTH_TWO_JORDAN_SPECTRUM_DIRECT_CHECK_OK`.

All computations are finite. The proof for arbitrary positive length and arbitrary field is the algebraic matrix-power and Smith-normal-form argument presented in `RESULT.md`. This check does not certify novelty, full-text coverage of unlocated literature, or any independent audit.
