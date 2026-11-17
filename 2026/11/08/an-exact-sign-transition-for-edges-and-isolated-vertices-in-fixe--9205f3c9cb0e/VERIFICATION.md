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

For r,m>=2 uniform k-subset of G=r K_m, put N=rm, B=(r-1)m, Q=k*C(B,k-1)/C(N-1,k-1), Q=0 outside range. E[E]=(m-1)k(k-1)/(2(N-1)); marking an isolated selected vertex removes its entire clique and leaves uniform k-1 subset of r-1 other cliques, yielding E[E|isolated v]=(m-1)(k-1)(k-2)/(2(B-1)). Cov(E,I)=Q times their difference, exactly Q*(m-1)*(k-1)*(m(k-2r)+2)/(2(B-1)(N-1)). Q>0 iff 1<=k<=B+1. This yields sharp sign negative 2<=k<=2r-1 and positive 2r<=k<=B+1 for m>=3, with remaining zero and m=2 exceptional. Bernoulli per-vertex retention yields blockwise E*I identically zero and covariance -r C(m,2)m p^3(1-p)^(m-1)<0. Fixed-r,k,m->infty limits derive from product ratios. Independent exact hypergeometric weighted occupancy enumeration verified all allowed k for 2<=r<=4, 2<=m<=5. These are corroborations of an all-integer algebraic argument.

## originality

PASS

Same objects rewritten as capped occupancy vector and singleton/pair collision counts; compared true sampling mechanism and statistic to with-replacement richness/frequency, random graph motif covariance, and foundational finite-urn distributions. No inspected prior theorem states or dominates this sharp all-parameter sign law. Restricted-occupancy 1981 source is particularly plausible, but only abstract readable; retain explicit access risk rather than pretending full noncoverage.

## value

PASS

Edges and isolates are natural induced-subgraph counts. The sharp k=2r threshold (independent of clique capacity for m>=3), capacity-two exception, boundary m^-1 correction, and reversal relative to independent vertex percolation make a motivated complete finite-population correlation phase diagram. Raw multivariate hypergeometric moments are classical, but the exact threshold and contrasting sampling law are a useful precise result, not an arbitrary unmotivated table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
