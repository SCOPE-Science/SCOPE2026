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

For each of the two torus complements, the proof gives a complete divisor and intersection census. A direct finite-additivity calculation gives \(\chi(V_{\mathrm I})=5\) and \(\chi(V_{\mathrm{II}})=4\). The standard smooth very affine ML-degree theorem turns these exact topological values into generic reduced logarithmic critical counts.

The separate reproducibility script `verify_hexagon_ml.py` performs exact rational saturated Gröbner-basis calculations for the exponent vector \((2,3,5,7,11,13)\). The inverse-variable equation eliminates all points with vanishing torus coordinates or any deleted polynomial. The lex leading monomials are \((z,y,x^5)\) and \((z,y,x^4)\), and the respective \(x\)-eliminants have no repeated factors. Thus the concrete finite schemes each have the asserted numbers of reduced points. Code uses SymPy and requires no source data download.

This computation checks one parameter choice; genericity for arbitrary parameters follows from the cited theorem and the complete topological argument, not from numerical extrapolation. Historical priority, other-positive-chart families, and isomorphism of the **full** affine charts are not certified. No independent audit has been performed.
