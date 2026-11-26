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

On each retained subset the surviving simple cycles are exactly the fully retained original cycles. They are edge-disjoint and independent in the cycle space, and span it since every cycle-space element is a sum of simple cycles. Thus the Euler component identity gives the expected count. Differentiation of each subset probability gives the score (|S|−np)/(p(1−p)), proving the covariance formula for the fixed component-count statistic. Write b for the number of bridges and c for the number of cycle blocks. For f=μ′, f″≥0 and f(1)=1−b−c by the block counts. If b+c≥2, there is an interior root from the endpoint signs, and there cannot be two, since the secant slope from any second root to 1 would have to be nonnegative by convexity. A pure cycle of length ℓ≥4 has f(1)=0 and f′(1)=ℓ(ℓ−3)>0, giving a negative value just to the left of 1 and the same unique-crossing argument; the triangle and edge give 3(1−p)² and 2(1−p). For g_ℓ=ℓ−1−2ℓp+ℓp^(ℓ−1), independent exact rational evaluation gives g_4(2/5)=7/125 and g_4(41/100)=−4316/10^6; g_3(41/100)=443/10^4 and g_5(41/100)=4128805/10^8. The latter two decrease up to 41/100 and g_ℓ(ξ)>2/25 when ℓ≥6, so f(ξ)≥1. At 3/4 the bridge contribution is −1/2, g_3=−13/16 and each g_ℓ for ℓ≥4 is less than −1, proving f(3/4)≤0 with equality only for the path with two bridges. For a bouquet of t squares, the derivative is 1+t g_4; on [ξ,3/4], g_4′≤−5/4, so the unique root differs from ξ by at most 4/(5t). This proves the unattained lower infimum and sharp attained upper bound without relying on sampled roots.

## originality

PASS

The prior subgraph-component polynomial gives the general distribution framework, and an adjacent one-crossing result covers stars and the square via complete bipartite graphs. The supported distinct claim is the cactus-wide one-crossing classification and sharp extremal interval with square-bouquet infimum and the unique upper equality case, not the idea of a first moment or a covariance derivative identity.

## value

PASS

The expected number of surviving fragments and the density at which it peaks are natural induced-subgraph statistics not captured by a connectedness probability. A single-crossing law and a sharp density interval independent of the size and arrangement of the blocks explain how squares, rather than triangles, control the low-density extreme, and identify the sole upper extremizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
