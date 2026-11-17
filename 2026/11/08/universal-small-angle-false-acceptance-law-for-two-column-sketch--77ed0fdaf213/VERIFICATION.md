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

For the coefficient vector (-cos θ,1)/sqrt(1+cos²θ), the smallest singular value is at most sin θ||Y||/sqrt(1+cos²θ), while the largest is at least ||X||. Thus κ<=K forces ||X||<=K θ||Y||. Set X=θ z. Event indicators converge a.e. to κ([z,z+Y])<=K, since the boundary for fixed nonzero Y is a proper algebraic null set. The integrals have envelope ||f||∞ Vol(B_k(K||Y||)), integrable by E||Y||^k<infty. A right orthogonal two-column rotation reduces the matrix to [r,Y/sqrt2]; the Jacobian produces 2^-k||Y||^k times the volume for [r,e1]. The latter has Gram determinant b² and trace 1+a²+b², so condition κ<=K is b∈[1/K,K] and a²<=(K-b)(b-1/K), yielding V_k by polar coordinates. Independently checked exact k=2/3 Gaussian constants via symbolic integration for K=3/2 and 5/2. Gaussian X f(0), χ_k moment give stated Gaussian specialization. The limit is fixed k,K only and finite numerical experiments are supplementary.

## originality

PASS

Best-of-knowledge original final claim after direct statement/implication comparison; earlier general frameworks, alternative rules or smaller families are credited, with access and historical priority risks explicitly retained.

## value

PASS

The quantitative probability of falsely accepting a nearly dependent raw two-column basis is a natural risk in randomized sketch conditioning. The exact power k and sharp non-Gaussian universal coefficient (only f(0) and one moment of Y) are structurally informative and distinguish the result from standard iid Wishart singular values or generic subspace embeddings; does not pretend to analyze the full adaptive algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
