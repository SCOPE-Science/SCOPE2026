---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Explicit contour maps Phi_0 and Phi_1 are continuous homeomorphisms from c>0,t∈R onto plane minus fixed ray R={(u,u):u>=0}. Matching branches at t=1,2 (b0) and t=1,2,3 (b1) give exhaustive foliation by level sets c_0=max{|x-y|,-x-y}, c_1=max{|x-y|,-x,-y}. Direct substitution in every time interval verifies F_b Phi_b(c,t)=Phi_b(c,t+1) even at seams. Each piece has oriented Jacobian c giving d(c²/2) wedge dt. The outgoing/incoming formulas give two-sided positive-elapsed-time drift (c,c) and exact threshold N_b=max(0,ceil(3+b-t)). Independent Fraction computations checked 402 chart/time/height cases across b=0,1 and 3 c values, including 7 translated integer times per sample. Analytic branch checking, not finite testing, proves all-real result.

## originality

PASS

Older Lagarias–Rains papers address the same two-branch plane map family, rational circle rotation, and invariant circles, and Roberts–Saito–Vivaldi study critical curves. The inspected published abstracts and source's detailed mathematical discussion do not supply this specific pair of all-plane height/time homeomorphisms, piecewise canonical identity, exact cone-entry or explicit transport velocity. Distinct from trivial local shear normal form: the global contour foliation and exact matching at seams are essential. Full primary historical plane-map papers not entirely accessible; priority remains conditional.

## value

PASS

Global exact integrability and canonical coordinates for two natural parabolic boundary maps give an entire orbit phase portrait and explicit finite hitting-time and transport asymptotics for every nonfixed initial condition, not merely numerically determined rotation number. A motivated explicit normal-form fact for a classical dynamical family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
