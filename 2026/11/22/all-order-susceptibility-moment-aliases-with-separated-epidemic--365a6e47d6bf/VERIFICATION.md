---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The Gaussian complex moment gives the sine factor sin(9n*omega)=sin(2*pi*n)=0 for all n>=0, including normalization. Since |a|<1 the densities are positive. Integrating the susceptible equation and applying conservation gives pressure dynamics q'=beta F_a(q;r). F_a(0;r)=r>0 and F_a(beta/gamma;r)<0; strict concavity forces a unique positive root and negative slope there. The pressure approaches that root monotonically and the fraction newly infected is (gamma/beta)Q_a-r. Common roots for a and -a occur exactly when H(Q_0(r))=0. The signed measure defining H is nonzero, so Laplace uniqueness and real analyticity give isolated zeros at positive pressure. Q_0'(r)=-L_0/F_0'>0, giving a discrete exceptional set of seeds. All finite moments permit differentiation up to pressure zero from the right; differentiation of the autonomous equation recursively gives identical time derivatives, including the compartments. Analyticity of q at zero would yield an analytic inverse since q'(0)=beta*r>0, contradicting the zero Taylor radius of L_a. The two trajectories cannot coincide on a time interval with positive pressure. For the specific gap witness (not all rates or seeds), I independently evaluated the 18-term lower sum and Mills upper tail with exact rational bounds, not the submitted rounded Decimal check. Replay: record5_rational_bounds.py uses the alternating Machin arctangent series for pi, isqrt enclosures for the Gaussian normalization, reflected alternating sine bounds on [0,pi/2], and alternating Taylor enclosures for exp(-x/64) raised to the 64th power with outward rational rounding. It yields subtotal >99018259/500000000 and tail <431725319/5000000000, in particular >0.1979 and <0.0864 respectively. Thus -H(1/2)>0.1115. The roots straddle the baseline, and F_a'>=-gamma at beta=1 bounds each signed displacement from below after converting pressure to attack fraction. The resulting separation is >1.44*0.1115=0.16056. The approximate roots reported in the source are illustrations, not certificates. The source scripts were inspected, not run. This is a deterministic population-model identifiability result, not a finite-population or clinical prediction.

## originality

PASS

Moment-indeterminate lognormals, the heterogeneous SIR Laplace final-size equation, and warnings against finite-moment closure are established. The distinct supported result combines identical full local time jets with an all-integer-moment alias that separates final sizes at fixed rates outside a discrete seed set, and a rigorous explicit gap for one construction. The main 2026 source was obtained in full for this audit, unlike the access reported in the frozen record.

## value

PASS

The exact counterexample separates two seemingly strong forms of local information—every susceptibility moment and every initial time derivative—from a terminal observable. The separation is robust to the seed away from a discrete set and quantitatively substantial in one proved example, rather than a consequence of finite sampling or a numerically tiny discrepancy. The limitation to an unbounded moment-indeterminate law and a deterministic model is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
