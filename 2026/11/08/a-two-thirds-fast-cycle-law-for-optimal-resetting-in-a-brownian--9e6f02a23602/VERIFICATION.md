---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The variance ODE vdot=-(2k+r)v+2T implies a contracting two-stage affine map. Solving yields the displayed exact mechanical quench-work formula. Its normalized expression g(r)H_tau(r), with g=alpha/2-K/[2(2r+a+b)] and H<1 via z coth z>1, has uniform small-r tau expansion H=1-(r+a)(r+b)tau²/12+O((r tau)^4). Benchmark r=c tau^-2/3 yields loss K/(4c)+alpha c²/24; a global optimizer must have r→∞ and r tau→0 and is trapped at c tau^-2/3 with c bounded away from zero/infinity. The strictly convex loss has c³=3K/alpha. Independent moment-equation evaluation agrees with exact formula to 10^-17, and optimized-rate ratios for tau=.04,.01,.002 approach 1.

## originality

PASS

Lahiri–Gupta study Poisson resetting in a driven four-step Stirling engine with linearly varied k(t), not the two fixed-stiffness isochoric contacts with instantaneous Otto quenches. Published resetting papers on finite-time returns, quantum engines and reset entropy do not imply the exact classical all-global-maximizer tau^-2/3 law in located text. Mathematical optimization method is classical, concrete asymptotic claim appears distinct.

## value

PASS

A sharp optimizer-scaling boundary for a specified quench-work observable supplies useful optimal-control mathematics and explains competing relaxation/reset losses. Reset-actuator costs are explicitly excluded, so this is not inflated into a general net-engine efficiency claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
