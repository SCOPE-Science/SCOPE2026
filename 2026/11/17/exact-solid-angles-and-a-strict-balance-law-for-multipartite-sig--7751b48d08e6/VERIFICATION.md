---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: The negative sign coordinates cannot occupy different classes, since their cross-class sum would be negative. Given k negatives in a single class A_i, their magnitudes must precede all n-a_i outside magnitudes in an iid continuous symmetric sample, with exact probability 1/binom(n-a_i+k,k). The identity binom(a_i,k)/binom(n-a_i+k,k)=binom(n,a_i-k)/binom(n,a_i) yields the stated F_n(a_i). Uniform cube and Gaussian share this sign/rank probability, but only the Gaussian is the Euclidean solid angle; cube volume is 2^n times the probability. The k=1 term a/(n+1-a) is strictly convex and remaining factorial-ratio terms are convex; integer Robin Hood transfers then prove Schur-convex extremizers. A geometric-tail majorant at balanced a/n->1/r<1/2 and binomial symmetry at a=n-r+1 justify the distinct asymptotics. I independently recomputed exact angles 3/80 and 31/480 and all discrete second differences for 4<=n<=30. These computations corroborate—not replace—the unrestricted proof.

## originality

PASS

PASS (qualified): Beck–Hlavacek define signed type-B order cones and general chamber triangulations but the inspected text does not evaluate this complete-multipartite all-positive pair-sum family or strict integer part-size majorization. Two full earlier comparators have apparently similar imbalance conclusions but distinct defining inequalities and ambient dimensions: signed-chain |x_i+y_j|<=1 is bilateral, while anchored Lipschitz dual bounds are cross-part differences, not one-sided positive-root constraints. No checked stronger prior theorem algebraically specializes to the new F_n(a) formula or its fixed-r extrema; the bipartite sign-change case is classical and excluded. Prior coverage through a differently named type-B chamber enumeration remains a material risk.

## value

PASS

PASS: Signed-order cone angle and full-dimensional cube-section volume are natural invariants for the complete-multipartite type-B family. Their distribution-free equality, exact all-composition formula, strict balancing order, and exponential-versus-polynomial extremal angle regimes are a structural classification in a genuinely nonbipartite root system, not a textbook substitution or isolated table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
