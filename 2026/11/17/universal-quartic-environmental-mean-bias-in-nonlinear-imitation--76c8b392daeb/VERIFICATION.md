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

The logit substitution u=log(x/(1-x)), v=log(n/(1-n)) gives the canonical separable Hamiltonian H=∫h du-∫f dv. Each term is strictly convex and coercive because h is increasing and f decreasing with nonzero boundary limits. Thus every positive energy level is one compact smooth periodic oval, proving the global interior foliation. Integrating vdot and udot over physical time yields mean x=1/(1+theta) and mean F(a(t-n))=0, not mean n=t. The second-harmonic calculation yields the cubic environmental moment (1-2t) A^4/(4t(1-t))+o(A^4); independently simplifying C0=-p2/(4p), C2=p2/(12p) confirms its coefficient. Odd Taylor expansion of F gives mean n-t = -a²F^{(3)}(0)(1-2t)A^4/(24 F'(0)t(1-t))+o(A^4). Fermi derivative ratio is -1/2, giving +a²(1-2t)/(48t(1-t)). For t=1/2, H is even in v and reversal symmetry forces exact mean 1/2. This uses original-time period averages and assumes strictly monotone C5 g.

## originality

PASS

Existing payoff-feedback literature derives neutral cycles and the cooperation mean; its approximate environmental-mean statement under nonlinear imitation is not a rigorous zero-bias identity. The candidate supplies an explicit leading environmental-mean discrepancy absent from the closely related primary model, with the valid symmetric t=1/2 boundary credited.

## value

PASS

The physical-time mean environment is an experimentally interpretable observable in coevolutionary strategy/environment feedback. A nonzero fourth-order correction, controlled by imitation-response curvature and environmental asymmetry but independent of population feedback speed, is a substantive quantified distinction from exact cooperation averaging and repairs an overstrong inference in the original literature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
