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

For strict total endomorphisms on a simple cycle with n≥4, a proper idempotent fixes its connected image, a consecutive path of k≥2 vertices. The complementary arc has L=n−k+1 edges, hence the admissible walks give T exactly and require k≤n/2+1 and even n. Surjective idempotents are identity. Rotation acts transitively and freely on the n possible images, and the image stabilizer consists of identity and the reversal. The reversal acts by w_j→k−1−w_{L−j}; for even L it forces the central vertex, and for odd L it forces the central edge in one of its two orientations. An arbitrary admissible first half of the stated length uniquely completes, yielding S and then S or (T−S)/2 orbits of sizes n and 2n respectively. For the asymptotic, S is bounded by 2^{ceil(L/2)} via the initial signs, and on a parity block A_4² has trace 3 and determinant 1; the endpoint count at lengths 3 and 5 is 1 and 3, so T_{n,4}=F_{n−4}. These bounds give the claimed probability and class-number equivalent. A separately written enumeration of conjugation and rank histograms agreed for n=4,5,6,7,8,9,10,12.

## originality

PASS

Credit the known labeled rank counts and the ambient all-map conjugacy census. The supported distinct result is the complete rank-refined decomposition of cycle retractions into sizes n and 2n, including the midpoint counts and asymptotic rarity of the rank-aggregated exceptional stratum; none of the inspected statements determines these restricted rank-refined counts.

## value

PASS

Ranks and labeled counts alone cannot tell whether two retractions can be conjugated or how much of the population has symmetry. The natural stabilizer refinement yields a class polynomial by rank and a quantitative answer to whether exceptional small orbits affect asymptotic class counts. The exact reflection split and rarity together supply more than re-enumerating a known labeled invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
