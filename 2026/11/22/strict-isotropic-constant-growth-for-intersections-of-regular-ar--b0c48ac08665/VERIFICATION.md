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

For n≥3 the rotation representation forces zero mean and scalar covariance. The farthest-center constraint along a ray reduces to r²+2atr+a²≤1 with t the maximum antipodal dot product. Implicit differentiation gives ∂t log r=−a/d; differentiating this in a gives −1/d³ since d²=1−a²(1−t²). Put q=r² and tilt angular measure by q/Eq. The logarithmic derivative of E(q²)/(Eq)² is 2 Cov(q,∂a log q)/E(q) under the tilted measure. Both functions decrease strictly in t for a>0 and t is nonconstant under a positive density, so the independent-copy covariance identity is strictly positive. The disk value follows by continuity; r/(1−a)→1/t uniformly because t≥cos(π/n)>0. The polygon sector integral of sec⁴ has primitive tan φ+tan³φ/3, confirming the stated upper constant. The arc flux at half-angle β is 1−a cos u, and its product with 1+a²−2a cos u integrates to the stated J; differentiating the proposed antiderivative in β and checking its zero constant also gives the identity. At a=0 the nominal arcs simply partition the disk. The exact algebra replay is `python3 /workspace/checks/independent_01_05.py` (check 1). The frozen 151-assertion run is author-reported corroboration, not an independent rerun or proof of the continuum statement.

## originality

PASS

The supported distinction is the strict normalized polar-moment order at every radius and fixed order, with the sharp limit, not priority for the same-family radial root, area formulas or static polygon moments. A literature lookup and local published-record comparisons yielded relevant partial overlaps but no established equivalent or dominating monotonicity result.

## value

PASS

The regular-center deformation is canonical and orders an affine invariant from disk to polygon, something inclusion or area ordering cannot do. The strict covariance identity supplies a useful way to compare radial moment ratios beyond this explicit profile; the exact limits give a calibration for every order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
