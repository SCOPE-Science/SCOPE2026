---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The ring normals have vanishing Fourier modes 1..3 for n>=4, opposite vertical pairs and isotropic second moments 1/3; fourth vertical moment 1/9 differs from sphere 1/5. Minkowski prescribed area construction is balanced/full-span. Cauchy projection formula yields b_n(v)=pi/n sum_{x in X}|x·v|=2pi/n sum_j max(c sqrt(1-z²)|cos(theta_j-phi)|,hz). Second-moment Cauchy-Schwarz proves b_n<=2pi/sqrt3 with equality only poles except four horizontal n=4 diagonal directions. Uniform azimuth Lipschitz midpoint discrepancy gives |min b_n−rho*|<=pi²sqrt(2/3)/n. Continuum integral separates at t=hz/(c sqrt(1-z²)) and its derivative has sign arcsin(t)−2t sqrt(1−t²), whose unique interior zero u=sin(2u) determines an oblique global minimum; strictly larger t>=1 branch. Centering of symmetric projection body justifies global radii. Independently recomputed normals, polar brightness and 4 sample finite-n profiles; original code with all generator cross products and 1948 assertions inspected, universal proof analytic.

## originality

PASS

Earlier same-ring original-body theorem explicitly computes the regular bipyramid P_n radii, volume and Hausdorff distance, not its projection body Pi P_n or the absolute cosine-transform minimum. Earlier ring covering result solves nearest-site spherical cap radius, not average absolute projections; neither implies the oblique least-bright latitude equation or exact n=4 outer contact change. Congpei An 2026 establishes general projection-body discrepancy O(t^-1) as design strength t increases; fixed strength t=3 with n→infinity is not covered. Full primary text of An was inaccessible from arxiv and OA; institutional source returned vpn_disconnected (not an originality failure), preserved as an explicit priority risk.

## value

PASS

A sharp counterexample to cardinality-driven sphericity at fixed spherical design strength, with normalized equal-area Minkowski existence, complete outer contact geometry, a nonalgebraic sharp least-bright limiting latitude and uniform finite-size convergence. The projection body rather than the original polytope is a geometrically natural distinct functional.

The dated certificate retains the supplied scientific assessment, sources and limitations.
