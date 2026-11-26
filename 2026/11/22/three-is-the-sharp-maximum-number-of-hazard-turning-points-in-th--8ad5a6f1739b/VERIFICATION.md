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

Direct differentiation gives positive derivatives for theta>=1. For a=theta in (0,1), the Chen derivative before x0=((1-a)/a)^(1/a) is -beta G; after and at x0 the total derivative is positive. G diverges at zero and Q stays finite, giving the initial negative sign. For K=Q/G, (log K)'=R-lambda*tanh(log(u)/2), with R=-G'/G>0 since xR>2-a-a*x^a>1. Independently, let A=1-a, w=1-a*x^a/A and T=x^(a-1)/(A*w). Applying the Euler derivative E=x*d/dx gives ET/T=-1+a/w, Ew=-a*(1-w), and x^2*T''/T=2-(3a+a^2)/w+2a^2/w^2. Its numerator quadratic has discriminant a^2*(a-1)*(a+7)<0; the remaining part of R'' is (2-a)*(2-a*A*x^a)/x^3>0. Thus (log K)' is positive for u<=1 and strictly convex on u>=1 because the second derivative of -lambda*tanh(log(u)/2) is nonnegative there. It has at most two zeros. Rolle bounds intersections K=beta by three even with tangencies, and if there are three, none is multiple (otherwise an extra zero of (log K)' would be forced). For fixed a, centering Q at x0/3 sends its height to infinity and its value at 2*x0/3 to zero as lambda grows, while G at both points is fixed positive. The four strict checkpoint signs force three roots and persist on a nonempty open set. Independent exact range-reduced rational Taylor inequalities (python3 /workspace/chen_perks_rational_replay.py) gave -,+,-,+ at x=y^5 for y=1,7/2,19/5,399/100 at the stated rational parameters. That replay certifies those signs, not the general root bound or the optional decimal root locations.

## originality

PASS

The four-parameter distribution and graphical hazard flexibility are prior. The supported distinct result is the sharp stationary-age bound for its exact hazard, counting even degenerate stationary ages, and attainability at every fixed subunit theta. The inspected earlier results do not give that bound or attainment. This is a bounded literature comparison, not a priority guarantee.

## value

PASS

This resolves a natural shape question for an existing reliability law that was illustrated by plots, not settled by them. It tells users which numbers of stationary ages can or cannot occur, proves a genuinely present but bounded three-turn mechanism at each eligible shape, and handles tangencies without equating them with density modes. The curvature bound is structural rather than a fit to test cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
