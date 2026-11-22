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

For p=1+a cos2theta+b cos3theta the curvature radius is rho=1-3a cos2theta-8b cos3theta>0; rho prime=12 sin theta[a cos theta+2b(4 cos²theta-1)]. Its negative cosine root enters (-1,0) exactly at a<6b, giving six vs four vertices and cubic degeneracy at a=6b. The evolute E=p prime t-p doubleprime n has symmetric local coordinates Ex even, Ey=4(a-6b cos u)sin³u odd. At a=6b-delta the closure u0=acos(a/(6b)) identifies transverse endpoints, with interior ordinary cusp and two additional cusps; coordinate turning and tangent slope tan u rule out hidden self intersections near collapse. Under u=s sqrt(delta/b), scaled limit C1 curve X=-6s²+15s^4,Y=-4s³+12s^5 and endpoints ±1/sqrt3. Independent exact SymPy integral ∫X Y prime ds = -128 sqrt3/8505 verifies the area leading coefficient and exponent delta^(9/2)/b^(5/2).

## originality

PASS

Classical four-vertex theorem and Chebyshev zero theory provide existence bounds, while Allemann–Hungerbühler–Wasem study evolute/equilibrium topology. Separate two-harmonic SCOPE cusp saturation concerns Wigner caustics and centre symmetry sets with different harmonics, not this ordinary evolute. No inspected theorem implies the precise 2,3-harmonic three-cusp loop, Jordan simplicity, or 9/2 metric area coefficient. Specialist catastrophe-theory normal forms remain a historical reduction risk.

## value

PASS

The 2,3-harmonic support family is a natural low-complexity Fourier model of convex oval vertex birth/death. Exact three-cusp evolute-loop geometry with a sharp noninteger 9/2 enclosed-area collapse quantifies a singularity not settled by the qualitative four-vertex bound, and is a motivated local invariant rather than an arbitrary coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
