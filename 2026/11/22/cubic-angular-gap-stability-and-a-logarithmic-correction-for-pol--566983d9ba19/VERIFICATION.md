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

A side with half-gap a and angular displacement t from its midpoint has radius cos(a)sec(t) and arclength Jacobian cos(a)sec²(t). With u the radial defect and v the defect of the normalized angular density, both sup norms are O(δ²), the mean of v is zero, and the radial function is globally O(δ)-Lipschitz across the vertices. At separation β let s=|sin(β/2)| and A=1+(u+u′)/2. The exact squared distance is 4s²A²+(1−s²)(u−u′)². The relative second term is uniformly O(δ²) by Lipschitz continuity, so its square-root correction is led by h(β)(u−u′)² with h=(1−s²)/(4s), up to a relative O(δ²) error in that term. For |β|≤δ its integral is O(δ⁴) by Lipschitz continuity, and for δ<|β|≤1 it is bounded by Cδ⁴/|β|, yielding the uniform logarithmic error. The linear density correction vanishes because the circle kernel has constant angular marginal; the linear radial correction to the mean is (4/π) times the mean of u. The side integral is −2a³/3+O(a⁵), the perimeter is 2π−(Σa³)/3+O(δ⁴), and Σa⁵≤(δ/2)^4π, independently of the gap list. Dividing by the actual perimeter gives +ΣΔ³/(24π³) in the defect. For a regular n-gon a=π/n, the quadratic profile a²(z²−1)/2 on uniform z in [−1,1] has variance a⁴/45, up to O(a⁶). The averaged squared radial difference H(β) is periodic with period 2a and mean 2 Var(u). A primitive after mean subtraction is O(a⁵); integrating against 1/β between a and 1 therefore changes the integral by only O(a⁴). Using the even kernel h(β)=1/(2|β|)+O(|β|) gives the mean-distance contribution Var(u) log(1/a)/π. Density multipliers of this term cost O(a⁶ log(1/a)); remaining radial or density corrections are O(a⁴) after the linear terms. Division by 2π+O(a²) and subtraction from the circle ratio gives −π² log(n)/(90n⁴). The cubic term gives 1/(3n²); strict Jensen equality concerns only the leading energy. Neither limit depends on quadrature.

## originality

PASS

The global circle bound is prior. The supported distinct claim is the sharp leading energy and error uniform over arbitrary vanishing angular meshes. The same-law finite regular formula stated on MathBench is a material overlap; the record expressly does not claim independent originality for the regular coefficient relative to that formula. Its proof or provenance is not established by the problem statement. A fixed-window tail theorem on regular polygons, a local small-distance law, and a stadium log correction do not determine this polygon-wide upper-bound expansion.

## value

PASS

This quantifies the sharp disk inequality for general inscribed meshes and identifies the exact leading dependence on how the vertices are spaced, even with arbitrarily disparate gaps. The leading Jensen conclusion is useful without asserting finite-order optimality. The regular refinement explains why the next term is not just an ordinary power correction: the near-diagonal angular kernel integrates the radial variance over a logarithmic range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
