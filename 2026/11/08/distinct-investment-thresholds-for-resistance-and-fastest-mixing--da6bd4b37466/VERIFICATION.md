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

For connected network L, trace (L+P0)^-1 is strictly convex in edge conductances because off-diagonal Laplacian entries identify them and inverse trace has positive-definite second variation; disconnected assignments have divergent Kirchhoff index. Therefore the unique global Kirchhoff optimum is invariant under full community-preserving automorphism group, giving two orbit weights a (cross) and b (internal). Lambda2 is concave in L and symmetrization preserves an optimum. On community-difference vector lambda=2ma; community-internal zero sums eigenvalue m(a+b), multiplicity 2(m-1). Thus K=1/a+4(m-1)/(a+b), lambda2=m min(2a,a+b), budget m^2 a+c m(m-1)b=B. With r=b/a, scalar K derivative sign is c(1+r)^2-4[m-c(m-1)], giving r_R=2 sqrt(m/c-(m-1))-1 if c<4m/(4m-3), else 0. Scalar lambda2=B min(2,1+r)/[m+c(m-1)r] maximizes at r=1, r=0, or interval [0,1] according to c compared with m/(m-1). Strict averaged support argument extends all-optimum decisions beyond symmetric allocations. Threshold difference = m/[(m-1)(4m-3)], and substitution c=1+kappa/m gives .75 and 1. Independent Laplacian eigensolvers for m=2,3,5 and positive rational prices reproduced formulas, including m=3,c=1.4 giving K=81, lambda2=1/3. Experiments are not all-m proof.

## originality

PASS

Ghosh–Boyd–Saberi establish general convex effective-resistance optimization and analyze graphs with a single bridge; Sun–Boyd–Xiao–Diaconis give generic fastest continuous-time Markov mixing SDP, and Ellens et al. discuss resistance vs spectral objectives. The joint exact price-window/all-optimum support classification for a fully connected two-community graph is not furnished by these statements. Resultary includes related priced clique bouquets, tripartite designs and D-optimal two-community networks, but they have different topology or objective and cannot dominate these joint Kirchhoff/lambda2 thresholds.

## value

PASS

Two-community complete graphs with distinct internal/cross pricing are a natural resource-allocation model. An explicit nonempty price range in which two important objectives force opposite presence/absence of entire edge classes is a structural Pareto design fact with exact finite-size and critical-scaling boundaries, beyond a routine Lagrange multiplier exercise. Closed formulas provide concrete optimization benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
