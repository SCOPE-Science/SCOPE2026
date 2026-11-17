---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The source tricritical lambda,sigma reduce the 3-compartment ODE exactly to sdot=-eta*s+gamma*i-(gamma+eta)*s*i and idot=eta*s*i-gamma*i^2 on the invariant simplex. With r=s/i, R=gamma/eta, rdot=gamma-eta*r-eta*i*r*(r+1) and idot=eta*i^2*(r-R); every r=R crossing is strictly downward; if r0>R a crossing occurs by finite comparison, else i decreases. Eventual i decreases to 0 and r tends R. Stable-filter expansion r-R=-R(R+1)i+R(R+1)(2R+1)i^2+O(i^3) yields idot=-K*i^3+L*i^4+O(i^5) and reciprocal-square integration gives c0=(2K)^-1/2 and c1=L/(2K^2)=(2gamma+eta)/(2gamma(gamma+eta)), remainder O(t^-3/2 log t). Independently checked parameter coefficient algebra and 3 ODE peak regimes; numerical trajectories are not proof of global convergence or asymptotics.

## originality

PASS

The original 2023 Pires et al mean-field paper states tricritical parameter coordinates and 1/2 decay exponent but does not supply universal second coefficient or initial-condition one-peak phase classification in the inspected model/results sections. Related published SIRS tricritical and SEIR critical decays concern different equations.

## value

PASS

Universal finite-time correction and complete initial-state peak condition solve a natural full-simplex epidemic dynamics question, extending known critical exponents with an explicit correction and a sharp transient behavior classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
