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

Choose image dimension r, kernel dimension n-r, and a quotient-to-image isomorphism to obtain [n r]_q^2 |GL_r| choices of A. Fix this A: B maps onto all maps V to im A via B↦AB, with q^(n(n-r)) preimages per map. In a splitting V=im A ⊕ W, the blocks (C,D) of AB into im A satisfy (AB)^2=0 exactly when C^2=0 and im D⊆ker C. Surjectivity of A onto its image proves rank ABA=rank C, not generally rank AB. Square-zero C of rank s is specified by its s-dimensional image, an (r-s)-dimensional kernel containing that image, and a quotient isomorphism; these give the two Gaussian coefficients and |GL_s| in the formula. The allowed D contribute q^((r-s)(n-r)); this gives all strata including r=0, s=0 and r=n, with neither factor restricted to be nilpotent. The lower and upper normalized Gaussian and general-linear factors are uniformly bounded by powers of the positive product ∏_(j≥1)(1-q^(-j)), independently of n,r,s. The resulting exponent is -n^2+2nr-ns-2r^2+3rs-2s^2. With x=r-5n/7, y=s-2n/7 this is -3n^2/7-(x^2+y^2)/2-3(x-y)^2/2. The optimum is interior by linear margins; feasible rounding gives a bounded-penalty term (the finitely many small n are absorbed into the constant), and translated lattice sums are bounded uniformly in the shift. Reserving a quarter of the squared Euclidean penalty for the tail and summing the other quarter gives the stated conditional estimate. Single-matrix rank weights have exponent -n^2/2-2(s-n/2)^2 with s≤floor(n/2), giving matching constant bounds and hence the ratio. The stated rarity even within nilpotent products follows already from taking A invertible and AB regular nilpotent, a subevent of probability at least a q-dependent constant times q^(-n), by the size of the regular-nilpotent conjugacy class. The frozen direct four-case rank check and its output were read, not rerun; universal correctness is from the count and estimates, not the reported pass marker.

## originality

PASS

Pass for the exact internal (rank A, rank ABA) census under the square-zero product condition and its two-dimensional conditioned localization. Prescribed-target factorization covers the marginal event; the 3/7 exponent can be extracted by optimizing the corresponding target-rank sum and does not depend on access to the new internal rank statistic. Credit those overlaps, and the standard single-matrix formula, rather than treating the unconditional census or ratio as standalone originality.

## value

PASS

Within the natural index-at-most-two event for an unrestricted random product, the exact joint law distinguishes the rank of the first factor from the rank of the product restricted to its image. It reveals an order-one rank localization at two distinct linear scales, not determined by a target-rank distribution. This is a structural, reusable refinement of the existing product law, rather than a table of small cases or the marginal comparison alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
