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

PASS: for all p,q>=1 with N>=3 and theta in [0,1], M-matrix positive resolvent makes every off-diagonal T entry positive for h>0. Spectral projectors give min part diagonal r_m(t)=(1+Nt+Mt²)/((1+Mt)(1+Nt)), t=theta h. Diagonal sign is exactly theta+[m theta+M(2theta-1)]t - M(N-1-Ntheta)t². For 0<theta<(N-1)/N it has one positive root and yields exact radical step frontier; theta=0 Euler gives h<=1/M; theta>=cutoff all steps safe. At fixed N, F_{m+1}(t)-F_m(t)=(1-theta)t+(N-1-Ntheta)t²>0, giving strict balance ordering. Checked symbolic identities and 60 direct inverse matrix instances; infinite statement from algebra and M-matrix proof.

## originality

PASS

PASS best-of-knowledge with a clearly known Crank-Nicolson slice: full inspected complete-multipartite Crank-Nicolson theorem already implies theta=1/2 horizon and balancing. The submitted theorem extends to every theta including unconditional theta=(N-1)/N and all finite regimes, not deducible solely from theta=1/2. Consistent-mass metric-wire-network K_pq theorem differs fundamentally from combinatorial Laplacian; its positive-step lower bound, absent here, confirms models cannot be equated. General theta positivity/diagonal resolvent literature checked; Bonnans-Tan full report unavailable, risk documented.

## value

PASS

PASS: exact all-theta positivity region of a natural complete-bipartite graph heat network is a meaningful sharp positivity-preserving integrator classification, providing step horizon, unconditional parameter cutoff and geometry-order theorem; does not merely recite prior theta=1/2 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
