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

Send a semicircle with endpoints u<v to the imaginary axis by (z−u)/(v−z), then take |Re|/Im to obtain the claimed hyperbolic sine of distance. On the designated side z=iy, set x=y/√λ. The distance envelope in these units is min{x,x⁻¹,(x+x⁻¹)/(λ−1)}. By reciprocity restrict to x≤1, where the first neighbor suffices and the opposite side becomes active only for x>(λ−2)^−1/2 when λ>3. The envelope increases to this switch and then strictly decreases to x=1, making its reciprocal pair the only maxima. For λ≤3 the maximum is only at x=1, where all three contacts tie exactly at λ=3. The half-turn exchanges opposite sides. Relabeling cyclically via λ(z−1)/((λ−1)z) gives the other side type with τ=λ/(λ−1). At κ=max(λ,τ), the larger-type value dominates the smaller-type value κ/(κ−1), strictly unless κ=2, where all four sides share it. Thus the two pieces of sinh²δ meet at κ=3 and respectively increase and decrease, giving the unique extremizing shape and the limiting value. Independent checks using the minimum of a direct cosh-distance function verified sampled side peaks and contact multiplicities; replay with python3 -I -B branches/frozen_review_checks.py from /workspace.

## originality

PASS

The supported distinct result is the all-shape side-slimness envelope, the sharp nonregular class and the change in side-point maximizers. The regular ideal-square case and the general notion of side slimness are credited overlaps. The strongest available comparisons concern either a restricted regular shape, interior clearance, a different contact condition, or infimal opposite-side distances; none yields this side-restricted envelope in the material inspected.

## value

PASS

The slimness of ideal geodesic polygons is natural, but a regular-square calculation does not predict even the extremizing quadrilateral shape. The full one-dimensional profile reveals a sharp nonregular maximum, contacts with all three other sides exactly there, and two maximizing points per active side beyond it. That is a useful exact benchmark for shape dependence and nearest-side geometry, beyond a coarse slimness bound or an opposite-side separation formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
