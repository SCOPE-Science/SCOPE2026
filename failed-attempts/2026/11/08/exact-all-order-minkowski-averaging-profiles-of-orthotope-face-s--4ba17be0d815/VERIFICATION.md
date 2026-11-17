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

For arbitrary positive side lengths, n>=1, 0<=k<=n and N>=1, each of N k-skeleton points has <=k interior entries; hence an averaged off-grid coordinate requires at least one of Nk available free slots. Conversely assign each off-grid coordinate a slot among N rows of capacity k, choose the free coordinate from its adjacent grid interval, and use endpoint rows elsewhere. This proves M_N={offgrid<=Nk}. The distance is obtained by rounding the cheapest m=max(n-Nk,0) coordinates, giving sums of m smallest grid distances. Choosing each coordinate at a grid-cell midpoint maximizes these distances and gives sorted shortest side lengths in the Hausdorff formula. Saturation, dimension and deep-hole loci follow from coordinate strata. Independent exact half-grid sumsets n<=3,N<=3 agree. No n-dimensional volume claim is made below saturation.

## originality

FAIL

An earlier November 1 full published result for every orthotope cubical skeleton and every N proves the identical grid-stratum equality, the identical exact pointwise coordinate-order-statistic distance, every l_p Hausdorff radius and the same sharp Nk>=n threshold. Its half-width a_i=ell_i/2 and centered interval [-a_i,a_i] are affinely isometric to the new [0,ell_i]. It additionally calculates the stronger integral homotopy type. New unit-cube farthest-point characterization follows immediately from equality in the already published coordinatewise delta_i<=ell_i/(2N) bounds. Exact earlier coverage defeats originality.

## value

FAIL

The scientific content here is a recomputation of a known, stronger complete cubical-skeleton profile. The maximal-distance midpoint locus and Hausdorff-dimension observation follow by elementary equality and cell counting from the older complete subdivision theorem; they are not distinct motivated open invariants. Hence no surviving independent mathematical contribution qualifies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
