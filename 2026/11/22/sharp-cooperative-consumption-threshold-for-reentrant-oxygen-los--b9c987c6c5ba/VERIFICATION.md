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

For each fixed k>0 the linear oxygen equation has a unique equilibrium with exponential convergence. With x=k/K and z=x^p, the sign of its mixing derivative equals the sign of 1-qG(z), where G=z(p-1-z)/(1+z)^2. For p<=1, G<0. For p>1, G'=[p-1-(p+1)z]/(1+z)^3 and the positive maximum at z0=(p-1)/(p+1) is (p-1)^2/(4p). This gives the exact threshold, including strict increase at a single stationary double zero. Above threshold the derivative numerator has precisely the two displayed simple roots in (0,p-1) and sign pattern +,-,+. The curve runs from -infinity to Cs from below; strict monotonicity on each branch gives the stated level counts, including tangencies and no level at or above Cs. A positive level is necessary for physical meaning. At fixed p, the root gap in z is asymptotic to 2 sqrt(p) sqrt(q-qc)/(1+qc); the smooth x(z) conversion gives the printed splitting coefficient. For the concentration gap, integrate (q+1)(z-z_-)(z_+-z) times the smooth positive weight (r0/K)/[p z^(1+1/p)(1+z)^2] over that interval; its integral scales as the cube of the root gap with a strictly positive limiting coefficient. Independent bounded replay: python3 /workspace/review_replay.py, check 5, including the exact gain maximum, an exact positive-root count in the p=2 example and its numerical levels. This establishes a conditional model theorem, not a field-data claim.

## originality

PASS

The supported distinct claim is the exact all-parameter fold and level-count boundary for the specified positive-baseline Hill balance, not the use of Hill laws, generic positive-feedback folds or universal onset exponents. The mathematically equivalent rational response is a material historical-priority risk, searched explicitly. The available prior statements did not establish the same exact critical condition or an implication covering this constant-plus-Hill gain. The access limitations below do not establish absence.

## value

PASS

With ventilation and mixing-stimulated oxygen demand competing, the threshold tells exactly when monotone ventilation gain can give way to a rise–fall–rise steady response. The positive-baseline/all-parameter classification and exact crossing counts provide a precise model benchmark and parameter demarcation, not an arbitrary numerical slice or a claim that generic fold exponents are new. Biological interpretation is restricted to positive equilibria under an explicitly uncalibrated law; no field tipping point or transient prediction is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
