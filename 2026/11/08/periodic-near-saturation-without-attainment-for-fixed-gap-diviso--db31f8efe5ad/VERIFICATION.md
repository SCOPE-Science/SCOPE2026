---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For fixed M, writing tau(n)=sum_{uv=n}1 and partitioning u modulo M gives each residue mass W_M(a)=M^(-2) sum_{u mod M} gcd(u,M)1_{gcd(u,M)|a}, positive and summing to 1. Squarefree primorial CRT gives local weights (p-1)/p² and (2p-1)/p². Remove the lower-weight endpoint of every circular forbidden edge 1<=d<=h to obtain an h-separated periodic independent set. Hellinger affinity factors H_p for p∤d; H_p=1-(3-2sqrt 2)/p+O(p^-2), so Mertens gives missing weight O_h((log Y)^-(3-2sqrt 2)). Every nontrivial periodic spacing pattern omits a positive-mass residue, proving no attainment. Independently verified exact CRT weights and circular independence for moduli 6,30,210; prime-product proof is analytic and not inferred from tests.

## originality

PASS

Chatterjee establishes the unrestricted maximum divisor-sum asymptotic for suitable separations but does not show that one fixed X-independent periodic pattern captures arbitrarily nearly all XlogX coefficient; the submission constructs it with an explicit primorial Hellinger convergence rate and strict nonattainment. No previously inspected source or Resultary comparison proves this structural refinement.

## value

PASS

A prescribed arithmetic-periodic set repeated at every scale is a meaningful structural strengthening of an adaptive unrestricted extremum. It supplies an explicit quantitative approximation rate, a constructive modular packing method and a nonattainment theorem; these are not automatic consequences of classical divisor summatory asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
