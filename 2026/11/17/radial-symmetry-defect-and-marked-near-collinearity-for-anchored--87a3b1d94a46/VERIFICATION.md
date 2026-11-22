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

For compact planar convex K of area A with strictly interior anchor z, the continuous positive bounded radial function ρ has A=(1/2)∫ρ². Conditioning on X−z=r eθ, the Y−z strip |det|<t has first-order area 2t[ρ(θ)+ρ(θ+pi)]/r. Its upper bound 2t diam(K)/r cancels the polar density r dr dθ and permits dominated convergence at r=0. Integrating yields slope 2H/A for D=|det|/A, H=2A+I, I=∫ρ(θ)ρ(θ+pi), equivalently 8−(1/A)∫(ρ−ρ_pi)². Strict 4<C<=8 follows from 0<I<=2A; equality at 8 iff ρ=ρ_pi continuously, so K centrally symmetric about z. As z approaches any boundary point, antipodal radial-product integral tends to zero by a supporting line and dominated convergence; lower bound 4 is sharp. Affine invariance uses equal scaling of det and area. For the marked law, φ=θ+b pi+σ arcsin(A eps q/(rs)) has Jacobian A eps/[rs sqrt(1−(A eps q/(rs))²)]; cancellation against polar rs density gives a pointwise limiting conditional density 1/(2H) on the two radial intervals, 0<q<1 and two equally likely signs. Both densities integrate to one, so Scheffé gives total-variation convergence and the claimed branch probabilities/uniform radial marks. Own independent analytic oval check ρ=1+a cosθ at a=0,.2,.4 reproduced slope 8−4a²/(1+a²/2) and parallel probability 1/2+a²/4. The checked finite simulation source supports rather than proves the asymptotic.

## originality

PASS

PASS, qualified: exact first-order slope for the TWO-point anchored determinant and its radial antipodal symmetry characterization, plus marked total-variation disintegration, were not implied by inspected random determinant expectation/zonoid or three-random-vertex triangle theories. Broader generic small-volume results are a priority risk, but their different model and uninspected details do not themselves demonstrate full coverage.

## value

PASS

PASS: the anchored determinant lower tail is an exact natural invariant of convex-body geometry, with the sharp upper equality characterizing central symmetry and the sharp limiting lower value for boundary anchors. The marked TV limit identifies the actual rare-event geometry, substantially beyond a generic volume-moment computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
