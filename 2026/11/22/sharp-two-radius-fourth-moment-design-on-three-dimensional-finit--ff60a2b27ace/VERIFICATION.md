---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At Q(x)=s≠0, the dot-product constraint fixes the x-component of y and leaves a binary form of determinant class s, so the two distinct slice counts differ by qχ(−s) exactly when the discriminant vanishes. At nonzero isotropic x, use a hyperbolic pair and a third vector whose norm is in the class −1 (the full determinant is a square): unequal radii fix a nonzero hyperbolic coordinate and leave q solutions, while equal radii reduce to counting square roots times q. This same splitting gives q²+qχ(−s) vectors at norm s≠0 and q²−1 nonzero isotropic vectors. Mixed roots, when present, are a(1±√(b/a))², both in the class of a. Substituting 4a and 4b into the mixed discriminant gives exactly the two ninefold collisions for distinct nonzero radii; both must be counted if both occur. Squaring the convolution gives the three energy polynomials: the linear correction uses (q−σ)(q²+qσ)=q(q²−1); the squared correction includes the overlaps. After normalization the two displayed difference polynomials are strictly positive for q≥11; the additional H term is nonnegative. The exact small-field comparisons and all equality counts follow, including characteristic three and the double collision at q=5. Orthogonality and S=−S give the claimed fourth-moment/return identity. Independent replay: python3 /workspace/branches/independent_checks.py 1 exhausts 95 pairs over orders 3,5,7,9,11 using direct ordered sums, agrees on all energies and winner counts 1,1,9,6,25; this replay did not cover order 25 or replace the symbolic all-field proof. Frozen checker inspected, not executed.

## originality

PASS

Credit the established intersection-number theory and the common sphere-count machinery. Best of available evidence supports the sharp odd-3D radius-pair comparison and its full equality classes, not a claim to the underlying convolution or a general Fourier-operator optimum.

## value

PASS

Choosing the support of a prescribed uniform two-shell walk to minimize its exact return probability is a motivated discrete design problem. The dimension-three classification yields all optimal radii, two genuine exceptions and an arithmetic mechanism to handle small fields; it is not a table lookup or an isolated sample calculation. It does not address weights or general extension extremizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
