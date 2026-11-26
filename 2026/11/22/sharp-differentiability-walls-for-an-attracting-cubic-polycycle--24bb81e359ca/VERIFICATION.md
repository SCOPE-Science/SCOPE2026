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

Taking radial and angular components gives (2) and, for V=r^2 and z=cos(2θ), the linear ODE (3). The unique solution bounded at z=1 has integrating factor M=(1-z)^β(1+z)^(-α) and is (4); the homogeneous term 1/M diverges at the horizontal saddle. Its positive analytic expansion at that saddle follows by integrating the convergent series in 1-z term by term, since β>0. The axes contain the two saddles and two sinks with the claimed eigenvalues. Each open sector has monotonically moving angle, from its horizontal boundary toward its vertical one. Compact invariant circles surrounding the origin must use this bounded radial solution on every open sector; on each axis only its nonzero equilibrium has a full orbit in a compact annulus. Logistic radial bounds give an eventual compact annulus for every nonzero orbit. Hence angles tend to the vertical sink in open sectors, radial variables converge to the matching equilibrium by trapping with the limiting radial coefficient, and axial trajectories tend to axial equilibria. Attraction here is of the punctured plane; the repelling equilibrium itself stays at the origin. For the regularity, subtraction of E=(1+εz)^(-1) gives (5), with strictly positive integrand. Put t=1+z and q=1-ε. The weighted integrand near v=0 is v^(-α) times an analytic function of v with value ε2^β/q². Integration gives a nonzero t^α term for 0<α<1, a nonzero t log(1/t) term for α=1, and a forced linear defect -εt/[q²(α-1)] for α>1. For α>1 the Taylor-integrated remainder consists of higher analytic powers and order t^α terms (t^α log t at integer resonance), with corresponding derivative bounds. Combining with E and t=2sin²u gives the three stated radial constants and the differentiated limits. For 2α<1 the normalized secants to the sink from the two arcs approach the same inward radial ray, inconsistent with a regular C¹ curve; at 2α=1 they give a corner. Above 2α=1 the tangent is transverse to the radial direction, making x a regular local coordinate. The curvature obstruction for 1<2α<=2 is then intrinsic, with logarithmic divergence at 2α=2. Replay: python3 /workspace/branches/independent_checks.py 3 (mpmath), independent differentiated endpoint diagnostics at ε=0.4 and α=0.3,0.5,1,1.5. The analytic argument, not the finite quadrature or the frozen checker, proves sharpness.

## originality

PASS

Credit only the globally matched nonzero singular amplitudes and sharp geometric C¹/C² walls for the reflected, closed cubic invariant curve. The invariant circle, its topological classification and local eigenvalue-ratio mechanism are background. No verified stronger same-family theorem establishes the matching and both boundary obstructions.

## value

PASS

The family isolates a change in geometric regularity without a topological bifurcation. The exact power and resonant logarithm identify genuine obstructions, not just sufficient smoothness estimates. The integral criterion and intrinsic tangent argument explain why the reflected global curve loses regularity at both boundaries, which cannot be read off from a local linearization alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
