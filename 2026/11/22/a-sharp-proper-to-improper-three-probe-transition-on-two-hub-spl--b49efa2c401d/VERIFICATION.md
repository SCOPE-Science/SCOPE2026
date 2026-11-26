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

With n=q+2 the Laplacian is zero on the constants, 2 on leaf contrasts and n on the remaining two dimensions. In the spectral resolvent the distinct-vertex constant contribution is c; for two leaves the contrast subtracts (1/(μ+2)−1/(μ+n))/q=1/((μ+2)(μ+n)), leaving 2c/(μ+2). Products of different unordered pairs of independent signs are uncorrelated. Each unordered same-class pair contributes 4B_ij² to the summed variance. Dividing by 4c² gives the stated class-count energy. For separate hubs with u≤v attached leaves, when u≥1 the move (u,v)→(u−1,v+1) followed by merging the second hub into the first class has energy difference −(1−β)(v−u+1) and leaves three nonempty classes. If u=0 and v≥2, simply merging gives 1−v. The leftover one-attached-leaf profile exceeds the balanced merged, zero-attached-leaf profile by β(H_q−q+1)=β(floor(q/2)−1)(ceil(q/2)−1)>0. With joined hubs, fixing x leaves in their class forces balance of the other classes by pair convexity, and ΔF=2+β[x−floor((q−x−1)/2)] is strictly increasing; this accounts for possible adjacent ties below the transition. The proper profile exceeds the balanced merged profile by βH_q−1. At β≤1/H_q the first ΔF is positive, so no further profile ties. This proves the threshold, uniqueness statements up to the stated symmetries and minimum variance for all q≥4, μ>0, including μ_c=2 for q=4.

## originality

PASS

The distinct claim is the exact transition and complete extremizer classification for the two-adjacent-hub, three-nonempty-class problem. Credit the general variance objective, the existing proper-color probing designs, and analogous switches for other specific graph families. The evidence inspected does not show this classification following from those analogues.

## value

PASS

This is an exact design benchmark at a fixed three-query cost: full proper coloring can be beaten by deliberately placing adjacent universal vertices together, and the exact parameter and equality cases determine when this happens. The competing topologies and their uniqueness are substantive information beyond a pair-sum formula or a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
