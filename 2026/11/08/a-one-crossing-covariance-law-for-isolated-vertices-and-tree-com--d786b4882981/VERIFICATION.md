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

For uniform G(n,m), a particular labeled k-vertex tree component consumes k-1 internal edges and forbids all crossing edges; outside is conditional G(n-k,r) with r=m-k+1. This directly proves E T_k=choose(n,k)k^(k-2)choose(Q,r)/choose(M,m) and Cov(I,T_k)=E T_k[(n-k)rho(B,Q,r)-n rho(A,M,m)]. Ratio of conditional-to-unconditional isolate means obeys R_{m+1}/R_m=(B-r)/(Q-r)*(M-m)/(A-m) when numerator positive. Independently expanded cross-product (Q-r)(A-m)-(B-r)(M-m)=(n-k-1)(k(n-3)+2)/2+kr>0 for all meaningful steps; subsequent numerator vanishes permanently. Thus signs positive, optional zero, negative over feasible m, with k=2 initially zero. For k/n->alpha in(0,1), at m=k-1 rho(A,M,k-1)->e^-2alpha yielding unique interior positive root alpha≈0.79681213 of 1-alpha=e^-2alpha; no boundary-alpha claim. Fresh SymPy zero residual in cross-product and exact sign-order tests for 4<=n<9 confirmed algebra, not used as all-n proof.

## originality

PASS

Important close prior (Resultary Oct 26 Universal macroscopic-tree covariance threshold) gives the same macroscopic constant and shape independence for isolates versus NON-INDUCED tree copies, with sign independent of m. Audited T_k counts connected tree COMPONENTS and forbids external/extra internal edges; its covariance changes sign as m varies, a different observable not implied by the prior noninduced theorem. Pittel's 1990 fixed-edge sparse tree census concerns asymptotic joint fluctuations, but full primary text inaccessible: exact all-m finite inequality remains best-of-knowledge original subject to this explicit risk.

## value

PASS

Finite-exact one-crossing monotonicity for two canonical component-count statistics across the full feasible edge budget is a meaningful structural sign law, including shape independence and a macroscopic initial threshold; it is not a tiny graph calculation or a relabeling of the earlier noninduced-copy theorem. The positivity/negativity transition is not simply monotonic stochastic coupling of G(n,m), because covariance may have either sign.

The dated certificate retains the supplied scientific assessment, sources and limitations.
