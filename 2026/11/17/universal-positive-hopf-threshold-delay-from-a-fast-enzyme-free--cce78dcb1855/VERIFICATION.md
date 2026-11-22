---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Independent reconstitution of the five-by-five rational limiting Jacobian yields the exact stated degree-five characteristic polynomial (symbolic determinant equality). First-order expansion of the two-fast-state Schur complement gives Q=1+tau_f eps z+eps²z²/(alpha gamma) and determinant perturbation -153000(400z-1)(s+5) tau_f eps, checked symbolically, not inferred from finite-K fits. The positive isolated large quartic root t=116.3626739461 leads to s_H(∞)=13.016079814889247 and omega=10.7871531900729. The eigenvalue implicit derivative gives c=670.0071181534648>0 and frequency d=4.00432112186999; fixed alpha,beta,gamma>0 and matched conserved total 91+50tau_f/K are essential. The result is local near the specified simple Hopf point, not a global assertion about all Hopf bifurcations. The paper also supplies rational sign intervals and transverse stability; finite spectral samples alone would not establish this conclusion.

## originality

PASS

Qualitative inheritance of oscillations under reaction splitting is known, but the local quantitative, rate-universal positive shift of the Hopf parameter is a narrower exact perturbation theorem not entailed by persistence. The displayed calculations were independently checked; literature priority is best-of-knowledge only.

## value

PASS

In enzyme-sharing reaction networks, introducing a fast intermediate is a natural model refinement. The sign, explicit nonzero leading sensitivity and reduction of three arbitrary fast rates to a residence-time factor distinguish qualitative Hopf persistence from a useful parameter recalibration. A model-specific exact perturbation is motivated by the benchmark and is not merely a restatement of persistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
