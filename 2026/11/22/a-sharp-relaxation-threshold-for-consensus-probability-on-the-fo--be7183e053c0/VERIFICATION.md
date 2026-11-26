---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The nearest-point rule for two equally weighted neighbors is the median of the current opinion and its two neighbors. At each vertex the target interval contains the opinion of its partner in an adjacent pairing, so projection and convex interpolation preserve each pair's initial range. Adjacent-low configurations with distinct ranks therefore cannot reach consensus. In the opposite-low case the inner gap is multiplied by 1−2γ while this gap is nonnegative, each within-parity width by 1−γ, and the sum of the two inner endpoints is conserved. This includes γ=1/2: the inner endpoints coincide after one step and stay fixed. Hence the limit is the initial middle-rank midpoint, and two of the six equiprobable rank placements imply probability 1/3 for iid uniform opinions. For any γ>1/2, the strict inequalities (1−γ)a,(1−γ)b>(2γ−1)g give the advertised adjacent split after one step from (0,a+g,a,a+g+b). Scaling into the open unit cube and perturbing leaves a positive-probability obstruction. The three-cycle comparison follows because every vertex uses the same global median.

## originality

PASS

The closest prior uses essentially the same balanced-median ring to test consensus for every initial state under a random type assignment. It covers failure of universal consensus here, not the random-initial-state basin of a fixed all-median ring, its limiting opinion, or the relaxation threshold. The accessible primary comparisons likewise do not supply those conclusions. This is a bounded statement-level assessment, not priority certification.

## value

PASS

The smallest simple cycle that can exhibit the effect gives a controlled example where unchanged network structure and a fixed type assignment do not fix the probability of consensus. The exact plateau, critical value, and selected limiting opinion quantify that difference. The strict one-step loss witness explains why the half-relaxation boundary is not just an artifact of a numerical trial or a sufficient stability estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
