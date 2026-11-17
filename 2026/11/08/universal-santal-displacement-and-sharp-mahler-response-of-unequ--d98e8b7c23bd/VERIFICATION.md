---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For centered base B, the polar of the bipyramid translated by axial z has t∈[−1/(b+z),1/(a−z)] and horizontal sections (1+zt) B°. Fubini gives J_d(z;a,b)=[(a/(a−z))^d−(b/(b+z))^d]/(dz), with continuous value 1/a+1/b at z=0. Its derivative is [G_d(T)−G_d(R)]/(dz²), G_d(u)=u^d(d+1−du). At centroid z=(a−b)/(d+1), derivative<0 by H′(r)>0; at apex midpoint z=(a−b)/2 derivative>0 by the explicit G comparison. Strict polar-volume convexity yields unique s between them. Envelope differentiation gives monotonicity; Taylor in δ and z has coefficient (d−1)/(2(d+2)). Independently verified exact Sympy differentiation and signs for d=2,3,4,6,9 with positive rational heights and Taylor coefficient. Finite tests do not replace all-d proof. d=2 valid, sign reverses for a<b; a=b centered.

## originality

PASS

Best of knowledge: qualitative shadow-system product trend, pyramid endpoint and raw polar/frustum computations are prior; surviving explicit all-dimension strict Santaló-centroid-midpoint bracket and normalized Mahler second-variation coefficient are distinct quantitative results.

## value

PASS

Quantifies a natural affine-geometric center displacement for every base shape and its sharp second-order Mahler loss, strengthening known qualitative shadow-system monotonicity. The centroid-to-midpoint interval is a structural dimension-uniform rigidity statement, and precise second variation is a motivated stability benchmark, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
