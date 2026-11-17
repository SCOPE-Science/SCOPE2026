---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS. Uniform random perfect matchings of 2n ordered endpoints are exactly reproduced by ranking n independent continuous chord pairs. The crossing and nesting indicator kernels have conditional projections p_X=2ℓ(1-ℓ), p_N=ℓ²+2u(1-v). Direct symbolic exact integration with density 2 on 0<u<v<1 independently produced means 1/3, raw second moments 2/15 each and cross moment 1/9, hence first-projection covariance zero, variance 1/45 each. Same-pair X/N indicators are disjoint and disjoint index pairs independent; summing shared-index covariances yields Var=n(n-1)(n+3)/45 and Cov=-n(n-1)/18. Bounded degenerate order-2 Hoeffding remainders have variance O(n²), so n^-3/2 vector CLT has independent N(0,1/45) limits. This is an infinite proof rather than an inference from finite n.

## originality

FAIL

FAIL. At least two earlier fully published SCOPE results prove the *identical* finite covariance and joint independent-Gaussian pair-count limit on exactly the same uniform perfect-matching model: 2026/10/13 'Asymptotic independence of crossing and nesting counts in uniform chord diagrams', and 2026/10/18 'Asymptotically independent crossing and nesting pair counts in random matchings'. Both use the identical first-chord orthogonal projections and n^{3/2} scaling, with variances 1/45 and covariance -n(n-1)/18. The target's alignment component A=binom(n,2)-X-N is a deterministic corollary, not a surviving original theorem. Full October 18 source and October 13 principal statement/proof passage read at immutable Git commit.

## value

FAIL

FAIL as a distinct mathematical contribution. Although the independent Gaussian limit is useful and correct, it is already covered verbatim by October 2026 prior theorems; adding a deterministic third-class component or different labels does not produce a new invariant. No substantive original motivated extension remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
