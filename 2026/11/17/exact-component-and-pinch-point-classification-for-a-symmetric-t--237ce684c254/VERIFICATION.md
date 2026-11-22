---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Cost expansion Q_j=|z|²+κ+(κ−1)t_j²−2κt_j with t1+t2+t3=0 gives Q_i−Q_j=(t_i−t_j)[−(κ−1)t_k−2κ] exactly. In X,Y with z=(X,√3Y), factoring sign inequalities into u=X−Y,v=X+Y gives exhaustive two-component decomposition for κ<1, single wedge at 1, and three convex regions with two single-point intersections for κ>1. Directly checking all equality axes closes sign cases. Separation is achieved between (0,0) and (−2c,0) in X,Y (minimum 2c); core vertices (0,0),(c/2,±√3c/2),(2c,0) give area √3c². A tree of convex full-dimensional pieces touching only at two points is contractible with exactly two cut points and three distinct interior components. Independently evaluated exact rational quadratic costs and membership for 26047 sample coordinates and κ values, only corroborative; algebra establishes all positive real κ.

## originality

PASS

Foundational Labelle–Shewchuk 2003 and Canas–Gortler 2011 describe site-fixed quadratic anisotropic cells, orphan configurations and sufficient net conditions to exclude orphans, but no theorem in inspected material gives the exact radially aligned equilateral three-site one-parameter global partition. Published Resultary Loewner-orphan two-site theorem handles two sites; published three-collinear-site sharp visibility thresholds concern scalar metrics and collinear sites. Neither algebraically implies the noncollinear rotated-matrix pinch decomposition. Venkovic–Anzt 2026 abstract restricts tensor formulas to star-convex cells; full text unavailable, explicitly an originality residual risk. Best-of-knowledge PASS.

## value

PASS

This equal-spectrum rotated-ellipse triple is a natural minimal symmetric anisotropy test case. Its complete sharp transition from a separated orphan to a connected but pinched non-star-shaped cell exposes geometric limits of star-convex diagram methods, with explicit globally meaningful gap, cut-point and area constants. It is not a generic reminder that anisotropic Voronoi regions may be disconnected.

The dated certificate retains the supplied scientific assessment, sources and limitations.
