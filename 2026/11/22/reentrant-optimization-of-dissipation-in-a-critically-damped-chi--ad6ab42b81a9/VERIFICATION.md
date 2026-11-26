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

The stationary angular correlation and independent thermal bath yield the velocity susceptibility p/(1+p)^2, where p=d+iOmega; Itô energy balance gives Q=2(E|V|²-2T). For w>=1 the derivative numerator N is strictly concave past 1, so there is at most one interior maximum. Independently factoring the gap from the boundary gives F(w,t)-F(1,t)=(w-1)G/[(w²+t)²(1+t)²]; the cubic G has discriminant -4t(1+t)²P(t), so an interior tie for positive t requires P(t)=0. P''>0, P'(0)<0 and P(0)<0 ensure exactly one positive root. Around that root, N(1,t)<0 uniformly, so the boundary is a strict local maximum uniformly in t; G's negative cubic leading coefficient bounds competing w uniformly. The opposite strict global signs at 19/100 and 1/5 therefore force a genuine interior tie, not merely convergence of a maximizer to 1. Elsewhere a change can occur only at a tie or N(1,t)=0. At t_- the outward second derivative is positive and the boundary cannot win; at t_+ strict concavity with N_w(1,t_+)<0 makes the boundary unique. At zero the unique optimizer is w=2, and above t_+ the positive boundary derivative forces an interior optimizer. Implicit differentiation gives both local slopes. For the large-t limit let e=t^(-1/2), y=e w; the rescaled equation is 1-y^4+e(2y^3-6y)=0, whose regular root at y=1 gives w=sqrt(t)-1+O(t^(-1/2)).

## originality

PASS

The substantiated addition is the global critical-damping optimizer diagram in squared chirality (including a separated tie and continuous return), not the achiral persistence optimum, translational heat framework, or the linear susceptibility.

## value

PASS

For a physically motivated dissipation objective, this identifies when a finite angular randomization rate helps, loses to deterministic rotation abruptly, and becomes favorable again continuously. The first global switch occurs after the boundary slope has already turned negative, so testing that slope does not answer the optimization question. The thresholds and onset laws are useful exact benchmarks at critical damping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
