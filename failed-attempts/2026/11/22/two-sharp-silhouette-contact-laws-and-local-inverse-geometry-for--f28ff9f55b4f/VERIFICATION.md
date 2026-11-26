---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For 0≤θ<π/2 the projection is the hull of two homothetic ellipses; dividing the compressed coordinate by cos θ makes disks with center distance D=H tan θ. Containment holds exactly for D≤δ=R−r. Above it, the small rim contributes a genuine exposed arc between two exterior tangent segments; at π/2 the exposed small rim projects to the shorter parallel segment of the trapezoid. With γ=arccos(δ/D), Green's integral gives (π−γ)R² from the large arc, r²γ+Dr sinγ from the small arc, and DR sinγ from the two tangent segments combined. Multiplying by cos θ gives the claimed area. For perimeter the support difference is the positive part of g=H sinθ cos t−δ sqrt(1−sin²θ cos²t); the boundary of its positive interval is β=arccos(δ/(L sinθ)). At contact g has angular derivative L and quadratic normal-angle term −δL t²/(2H). Rescaling t=√η z integrates the parabolic cap to the asserted C_P. For area, the derivative of sqrt(D²−δ²)−δ arccos(δ/D) is sqrt(D²−δ²)/D, so its integral from δ yields (2√2/(3√δ))(D−δ)^(3/2) at leading order; D'(θ_c)=L²/H and cos θ_c=H/L give C_A. In both cases the rescaled excess is η^(3/2) times a function analytic from the right at zero, positive there, which justifies differentiating the asymptotics and proves C¹ but not C². The axial disk and side-on trapezoid give the stated perimeters; the inversion using C_P follows from δ/L=sin θ_c, and the side inverse has the strictly positive denominator 2(1−sin θ_c). Uniform unoriented viewing gives a uniform absolute axial cosine, hence H/L. I inspected, but did not run, checks/frustum_checker.py; the frozen 156 finite checks do not prove these continuum statements.

## originality

FAIL

The principal mathematical content is covered by a reduction to exact cone profiles, not merely by a shared silhouette analogy. Fix δ=R−r and H, and let A_cone and P_cone be the known orthographic profiles of that radius-δ right cone. The frustum perimeter excess over the larger ellipse is identically the cone perimeter excess over its base ellipse; the frustum area excess is identically (R+r)/δ times the cone area excess. These identities hold for the full angle domain and carry the branches and leading contact coefficients over by elementary expansion. The inverse is then an algebraic consequence of those coefficients or of the already-conceded contact geometry and trapezoid perimeter. The October cone area record and the distinct indexed November cone perimeter record supply the exact profiles, not just angle extrema. The November records have the same catalogue date; equivalent coverage is established, order or historical priority is not. The decision is based on substantive coverage, not on a failed source retrieval.

## value

FAIL

Contact behavior and reconstruction from projections are useful questions. Here both excess functions are inherited exactly from radius-difference cone profiles, and extracting the leading terms and solving for one positive scale is routine once those profiles are given. No separate noise-stability result, nontrivial inverse obstacle, or independently needed previously unknown invariant remains to justify this formulation as a new mathematical finding. This does not detract from its usefulness as an explanatory exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
