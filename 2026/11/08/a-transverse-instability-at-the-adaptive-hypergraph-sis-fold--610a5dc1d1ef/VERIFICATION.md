---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Read the actual two-variable recurrence rather than reducing stability to the scalar stationary cubic. Positive stationarity at beta=1 gives F_h(r)=mu h r^3+r^2-r+mu=0 with h=eta/gamma. F_h is strictly convex on r>0 and its double root for 0<mu<1/4 occurs at r*=1-sqrt(1-3mu), h*=(1-2r*)/(3mu r*^2). Differentiating full (r,theta) update gives J11=1+mu(1-2r)/(1-r), J12=mu r/theta, J21=-3eta theta r^2, J22=1-gamma-eta r^3. Fold forces eigenvalue 1; other is trace J minus 1, greater than 1 iff gamma<mu^2(1-2r*)/[r*(1-r*)^2]. Independent exact SymPy calculations checked the rational fold mu=11/108,gamma=1/100,eta=216/275,r=1/6,theta=11/15, J=[[146/135,5/216],[-6/125,217/220]], spectrum {1,6343/5940}. gamma+eta=35/44<1. For h just below h*, two simple positive branches have multipliers continuous near >1; implicit function theorem persists them into beta<1, while disease-free eigenvalues 1-mu,1-gamma are <1. No stochastic/global-attractor claim is inferred.

## originality

PASS

Original model paper examines stationary polynomial, epidemic threshold and bistability narratives but does not supply the derived full two-variable transverse multiplier and stable-free/both-endemic-unstable open regime. Related Resultary SIS findings concern different mean-field laws, contagion parameters or graph structures and do not imply this Jacobian counterexample. Because the exact original full-text comparison was unavailable, O is best-of-knowledge with a named material risk, not an unconditional priority claim.

## value

PASS

The finding exposes a dynamical gap in reading folds as bistability in adaptive epidemic closures: existence of two endemic stationary branches need not produce an attracting endemic equilibrium when an activity variable is retained. An explicit admissible rational witness and open-set persistence correct a substantive stability interpretation without claiming global stochastic dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
