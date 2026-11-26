---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the admissible c,d the Gram matrix is positive definite by its antisymmetric eigenvalue 1−d and the positive definite two-by-two block of determinant 1+d−2c². Swapping rows two and three is implemented by an orthogonal change of coordinates since the row matrix is invertible and the Gram matrix is invariant under the swap. Convexity of the error norm permits averaging the two weights without loss; it does not prove all optimizers symmetric. At w=τ(z,1,1), the nonzero spectrum of the weighted row outer-product sum is τ times the spectrum of the congruence by diag(√z,1,1). Its eigenvalues are 1−d and the two eigenvalues λ± of the block with diagonals z,h=1+d and off-diagonal c√(2z). Given extremes m,L, scale 2/(L+m) uniquely balances endpoint errors and gives (L−m)/(L+m). Here L=λ+>h and m=min(1−d,λ−). The crossing λ−=1−d is equivalent to (d−c²)z=d(1−d), so exists only for c²<d; λ− is initially zero in the limit z↓0 and tends to h−2c². In the block-controlled region, squared contrast is 1−4z(h−2c²)/(z+h)² with a strict minimum at h. After any crossing the larger eigenvalue is strictly increasing with z while 1−d stays fixed. Therefore the unique symmetric minimizer is h or the crossing if it occurs first; the latter lies at or below h exactly for c²≤2d²/h. At the crossing L=z+2d, m=1−d, reproducing the rational branch; at h the block endpoints are h±c√(2h), giving the second branch and scale 1/h. At the boundary both coincide, and the contrast lies strictly between zero and one. The criterion z=1 reduces to c=d. At (c,d)=(1/4,1/2) the crossing occurs at 4/7 and gives unscaled extremes (1/2,11/7), hence weights (16,28,28)/29 and norm 15/29. Equal relative weights have unscaled extremes (1/2,(5+√3)/4) and the asserted strictly larger best contraction. Replay via RESULT.md Steps 1–6. The attached script and VERIFICATION.md were inspected, not executed; sampled competitors are not needed for the global statement.

## originality

FAIL

The previously dated windmill record 8c423dd752b2 covers the complete pointwise result by an exact reduction within that record's stated k≥2 range. Use k=2, pair correlation s=d and hub–leaf correlation t=c/√2. Its effective coupling kt² equals c², so for every symmetric scale the same three extreme-mode candidates occur; the only additional eigenvalues are another copy of 1−d and a nonextremal 1+d. The published windmill optimum and equal-weight criterion therefore give both branches here, with the contraction norm a monotone rescaling of the optimal condition number. This decision does not depend on recovering the inaccessible Kolotilina primary text or assigning priority from the later isosceles catalogue result.

## value

FAIL

The motivation for optimal simultaneous reflection weights is legitimate, and the numerical-size witness could be useful exposition. However the frozen mathematical contribution is exhausted by the earlier endpoint-identical scaling family, the elementary optimal common scale, and a parameter substitution. No new contraction-norm phenomenon, blocker to the reduction, or independently useful unknown exact invariant remains. This is a mechanical application rather than a substantive new gap filled by the three-row claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
