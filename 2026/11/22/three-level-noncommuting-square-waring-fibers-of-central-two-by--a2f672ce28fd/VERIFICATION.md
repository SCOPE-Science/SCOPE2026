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

# Reproduction and limits

Run `python3 check_waring.py` using Python 3's standard library. The checker constructs matrix products, commutators, determinants and scalar-square sums from field operations. Full ordered-invertible-pair enumeration is performed over \(\mathbb F_3\) and \(\mathbb F_5\), and independent traceless-pair enumeration over \(\mathbb F_7\), \(\mathbb F_9\), and \(\mathbb F_{11}\). The extension field is implemented as \(\mathbb F_3[t]/(t^2+1)\). A successful run ends with `MATRIX_SQUARE_WARING_NONCOMMUTING_OK`.

The proof covers every odd finite field, while the checker covers only the listed fields and, for the larger sizes, the traceless subspace. Exhaustive verification in the tested cases must not be confused with an infinite proof. The field-uniform argument relies instead on Cayley--Hamilton, the two-dimensional matrix centralizer, and elementary quadratic-character sums. The historical literature check is bounded and independent validation is not performed.
