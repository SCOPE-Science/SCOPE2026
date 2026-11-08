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

# Finite-field verification details

The standalone `VERIFY.py` uses integer encodings of \(\mathbb F_9\), \(\mathbb F_{81}\), and \(\mathbb F_{729}\). Its field moduli are proved irreducible and the program tests \(x^{q-1}=1\) for every nonzero field element. For each relevant \(c\) and each \(y\), it exhausts every \(x\) in the field and records the exact fiber distribution \((n_0,n_1,n_3)\). The affine total is \(n_1+3n_3\), with precisely two projective points at infinity. It also checks all eight base-field coefficients and the condition for tangent order four. Reconstructing the Weil numerator from the first three extension counts uses proved genus-three Newton identities and the functional equation, not extrapolation from additional untested extensions. The calculation finds rational Jacobian orders 1183 and 949 and ends with `VERIFY_OK`.

This establishes exact finite evidence only for the stated curves. It is not an independent mathematical audit, and it does not address different parameter normal forms or further historical-priority questions.
