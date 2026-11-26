---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently set z=u'/u with u''=p^2 u or u''=-q^2 u in the two phases. A zero launch (u,u')=(1,0) gives u' at the end of the pair equal to p sinh(pL/n) cos(qT/n) minus q cosh(pL/n) sin(qT/n); for qT/n<π/2 this has the sign of F(0) and changes sign at the stated T_n. For positive states below the first adverse tangent pole the signed pair map has positive denominator and is strictly increasing. Subtracting z leaves a numerator B_0−αz−Cz^2 with α,C>0. Below threshold B_0>0, so each iterate stays on its own side of the unique positive fixed point and moves monotonically toward it. The phase flows give convergence to the periodic profile; an increasing map has no nontrivial periodic cycles. At equality F(0)=0 and 0<F(z)<z for z>0, hence convergence to the zero endpoint without finite-time loss; that limiting boundary-touching cycle is not a surviving periodic trajectory. Above threshold, indefinite survival would force a nonnegative fixed point from a decreasing sequence, impossible. At or beyond qT/n=π/2 the first adverse interval kills every finite starting state. For c=p/q, the derivative of arctan(c tanh x) is c(1−tanh²x)/(1+c²tanh²x), strictly decreasing on x>0. Its chord slope and its cubic coefficient −(c+c³)/3 give strict all-n threshold increases and the stated n^−2 deficit with O(n^−4) remainder at fixed parameters. Replay: frozen RESULT.md lines 24–54, VERIFICATION.md and checker.py (inspected, not executed). Independent bisection of the transfer derivative with p=q=L=1 returned T_1≈0.6508801680, T_2≈0.8657694832 and 64²(1−T_64)≈0.666504, consistent with the analytic coefficient 2/3. Conclusions are for starts at a favorable boundary and the stipulated repeated identical pairs, not arbitrary histories.

## originality

PASS

The supported distinct contribution is the joint viability phase diagram and exact finite-fragmentation comparison for a prescribed scalar forcing schedule with loss at zero. The Riccati-to-linear transformation, projective period map, and time-averaged forcing limit are background mechanisms, not claimed as new. No covering statement for the joint result was established in the available evidence.

## value

PASS

Holding total favorable and adverse exposure fixed isolates a motivated timing effect. The exact all-frequency threshold identifies where a positive mean falsely predicts survival and how fast that discrepancy shrinks; the strict ordering and leading coefficient answer quantitative questions not addressed by averaging alone. The contribution is to this stylized switched model, not a field-validated ecological prediction or an optimality theorem for all schedules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
