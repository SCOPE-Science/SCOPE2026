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

For a fixed displacement the source coordinates are independently uniform on S and [0,H], so the two loss fractions add minus their product. The preimage of a road can contribute at most the part of its translated interval outside that road itself, of length min(|u|,w); at most |u| is lost beyond the hull. Discarding the nonnegative product term and applying Jensen to the angular average of min(r cos(theta),w), which is concave in r, gives the stated mean-only result. If w<mu the integrand clips on a positive-measure set and the comparison to the perimeter bound is strict. For fixed distance mu with every viable strip and H longer than mu, the displaced road preimage outside its own road is all viable and the hull bound is exact. The product term integrates over one quadrant via x=cos(theta), giving integral of min(x,t) from 0 to 1 equal to t-t^2/2, and the claimed correction including the outer term. This proves exactness in the separated small-displacement regime and first-order sharpness as the widths scale. The numerical SciPy checker and VERIFICATION.md were read, not executed; the approximations are supplementary and not the proof.

## originality

PASS

The inspected prior work identifies the narrow-road weakness and supplies general overlap machinery. It does not give the road-resolved mean-only cap and fixed-radius second-order coefficient for this geometry.

## value

PASS

Resolves a specific stated deficiency of a widely applicable perimeter bound in a natural geometry without assuming a known radial kernel. Captures the first-order improvement at every positive width-to-dispersal ratio and quantifies the exact second-order loss product for fixed radius, rather than merely observing that old bounds can overcount.

The dated certificate retains the supplied scientific assessment, sources and limitations.
