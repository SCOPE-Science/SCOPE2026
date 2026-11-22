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

Direct differentiation gives sdot=2t s y²(x+y), so unit circle invariant and its theta flow is rotation period2pi; normal Floquet integral vanishes. In polar s=r²-1, expanding exact ds/dtheta gives L=2t sin²(theta)(sin+cos), Q=3t sin²(theta)(sin+cos)-2t²sin³ cos(sin+cos)², and first variation h=e^(tH). The L part of quadratic return integrates to zero, yielding K(t) formula. Independent symbolic integration gives ∫sin³cos(sin+cos)²=pi/4 and fresh numerical quadrature K(0.2)=-0.08276477, K(1)=-7.37659, K(12)=+1.206e14. Global max H*=4/3+sqrt2 at 3pi/4 with H''=-sqrt2 and nonnegative amplitude with quadratic vanishing establishes positive strong-coupling Laplace constant. Origin rreturn=r-(pi/4)t²r³+..., hence attracting, and circle interior attracting when K>0; invariant disk with two disjoint attracting basins has an equilibrium-free compact invariant separator, forcing another periodic orbit via Poincare–Bendixson. Existence is for sufficiently large t only, not a computed finite threshold or unique cycle.

## originality

PASS

The 2022 Mujica primary paper studies EXACT same three-parameter vector field xdot=-y,ydot=x+y(r²-1)(ax+by+c). Its Theorem 4.7 asserts exactly one limit cycle when ab≠0 and c=0, based solely on second-order perturbative Melnikov; that is a conflicting global uniqueness assertion, NOT a stronger theorem implying the current claim. The independently reconstructed strong-t inner periodic orbit gives a finite-coupling parabolic return coefficient absent from the original source. Its isolation is not proved; therefore existence of this periodic orbit does NOT formally refute the 2022 assertion of uniqueness of isolated limit cycles, although it prevents interpreting that assertion as uniqueness of all periodic motion. A 2026 general polar-Dulac rigidity theorem covers a different angular/radial normal form, so cannot transfer sign definiteness. A relevant 1987 Gasull–Llibre–Sotomayor work is accessible only bibliographically, priority risk recorded.

## value

PASS

The exact nonlinear parabolic multiplier-one return coefficient and strong/weak coupling sign reversal exhibit a meaningful nonhyperbolic stability transition. At strong coupling the coexistence of the stable origin and attracting invariant circle forces an interior periodic orbit; its possible non-isolation is left open. This reveals nontrivial global recurrence beyond the observed circle and cautions against extrapolating a perturbative Melnikov count, without claiming to disprove published uniqueness of isolated limit cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
