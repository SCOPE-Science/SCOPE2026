---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Each side-foot condition is a strict convex strip; chord unit tangent differs from arclength tangent by at most κh. For any z in the kernel, |<z-γ(s),τ(s)>|≤2(1+Dκ)h uniformly in s, yielding Δ bound. Compactness and derivative of squared radius prove Δ=0 precisely for circles. On ellipse, maximum tangential residual at origin is a-b and antipodal pairing shows no translation can lower it. For even n central symmetry of the entire strip kernel permits z=0 when nonempty; direct midpoint/chord dot product gives the precise bound a²/b²<tan((2j+2)x)/tan((2j+1)x) for restrictive j, equality excluded. Minimize continuous f_x at π/4-x/2 and sample within x to get R_n=1+π/n+O(n^-2). n=4 admits all positive ellipse aspect ratios. Limits of smooth and finite regimes explicitly separated.

## originality

PASS

Existing regular-polygon maximal-normal chamber formulas cover only circular vertex configurations and area fractions; an odd-polygon radial/support inverse-uniqueness theorem assumes all feet internal rather than characterizing when existence persists. Zwierzyński pedal-iteration formula concerns projections to supporting lines, not finite segments. Neither implies exact anisotropic even-ellipse thresholds or fine-mesh smooth circle rigidity. Best-of-knowledge novelty survives with historical geometry risks.

## value

PASS

A complete and sharp aspect-ratio feasibility classification for a natural family of polygonal approximations to ellipses, together with a smooth rigidity and mesh obstruction that singles out circles, is a structural geometric result of independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
