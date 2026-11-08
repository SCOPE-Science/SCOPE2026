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

# Reproducible symbolic and finite-field checks

Run `python3 verify_cartier_quintic_char3.py` from the directory containing the executable script. No packages beyond the Python standard library are required. The successful marker is:

`CYCLIC_QUINTIC_CHAR3_CARTIER_PASS symbolic_C2_ninth= [0, 0, 2, 1, 1, 2] tested= [(3, 1), (9, 7), (27, 25)]`

The coefficient vector is in ascending powers of the parameter, over \(\mathbb F_3\); it is the polynomial \(-\lambda^2(1+\lambda)(\lambda-1)^2\). The script checks a symbolic polynomial identity over \(\mathbb F_3[\lambda]\), independently derives coefficient entries of the Cartier operator from \(f\), \(f^2\), and \(xf\), verifies the semilinear inverse-Frobenius matrix-composition rule, and exhaustively checks all smooth parameters in \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). The count of tested smooth parameters is respectively \(1\), \(7\), and \(25\). It checks finite-field arithmetic and root-extraction consistency in each field.

The infinite-field theorem does **not** rely on finite-field sampling: it follows from the explicit Cartier formula and symbolic ninth-power factorization given in `RESULT.md`. No computer output by itself certifies the differential-basis derivation or the claim of historical originality; those are supported by the mathematical argument and documented source comparisons. Independent audit and independent validation have not been performed.
