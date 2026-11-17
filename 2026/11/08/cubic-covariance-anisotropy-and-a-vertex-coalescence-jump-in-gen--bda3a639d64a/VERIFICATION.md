---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The actual source RESULT.md (blob 5075f5...) reconstructs the entire extreme-vertex set, including the only orbit coincidence v0=v1 at a=1, and n!/j! orbit multiplicities. Sampling a layer with probability proportional to 1/j! and then a uniform permutation is therefore exactly the uniform distinct-vertex measure. The orbit total S=T_n-D_j and squared norm Q=U_n-A_j yield by permutation invariance C=alpha I+beta 11^T; Var(S)/n and the trace recover the two displayed eigenvalues with correct normalization and multiplicities. Positive weights on distinct layer sums and on nonconstant permutations establish both strict positivities. Factorial tail domination justifies convergence of all needed moments to Poisson(1) or its conditioning J>=1; E[J(J-1)]=1, Var[J(J-1)]=6, and the conditional moment ratio produce the interior and boundary constants. U_n=b^2 n^3/3+O(n^2), T_n=b n^2/2+O(n), so lambda_perp=b^2 n^2/12+O(n), while lambda_parallel=V/n+o(1/n). The source correctly distinguishes fixed a>1 from a=1; no simultaneous parameter/dimension limit is asserted. Independently enumerated distinct vertex sets and exact rational covariance matrices for n=2..5 and parameter pairs (1,1),(2,1),(3,2): all 12 two-eigenvalue formulas matched. These bounded checks are corroboration, not the all-n proof.

## originality

PASS

Known 2023/2024 and 2025 parking-polytope full papers establish the orbit structure and face/facet and volume theory; the source claim deliberately does not reassert their novelty. No covariance eigenvalue or asymptotic uniform-vertex anisotropy formula occurs in these inspected theorem statements. The rank-two S_n representation is a straightforward symmetry tool, but the exact factorial-mixture variance, Poisson-conditioned boundary and discontinuity are new conclusions rather than an immediate implication of a quoted covariance identity. Related covariance of distinct matching or wheel polytopes has different vertex measure spaces; extreme ellipsoid and width results are not second moments. This is best-knowledge, with residual equivalence risk.

## value

PASS

The eigenstructure of uniform vertices is a natural metric statistic for a canonical generalized permutahedral family whose face and volume enumerations are known. The sharp n^-1 versus n² spectral scales produce cubic anisotropy, and the discontinuity of the vertex measure under a continuous polytope deformation exposes nontrivial geometric/probabilistic behavior. The entire parameter family and asymptotic law supply mathematical content beyond a routine single finite calculation; neither exact enumeration nor novelty alone is the reason for passing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
