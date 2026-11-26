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

The constrained minimizer is (0,0) and the gap is au+(u²+v²)/2 with Hessian I. On the default disk, q=0 forces precisely the face u=0, |y|≤√(a²+2ap). If q≠0, the asserted point on that face satisfies ball and halfspace stationarity with multipliers |q|/b>0 and p+a−p|q|/b≥0; the Lagrangian is strictly convex, proving uniqueness even at a=0. Then ||d||=||g|| and Cauchy–Schwarz makes the step the unconstrained line minimizer with 0<η≤1. Its final point has inner product ap with d (since (x₁+ae₁)·d=0); its transverse component has squared size p²(b−|q|)²/||d||². This gives the stated ratio. Its bracket is 2b²−2(ap+b|q|), hence R<2; substituting a=1, q=p³ gives R→2. On the tied face set w=p²+y², C=p(p+a). The ratio is (w−p²)/p² up to C and 1+(p+a)(a−p)/w thereafter on [p²,(p+a)²]. Monotonicity yields the two claimed maxima; continuity and y=0 give the full range. At a=p the second branch is constant, so y²=ap is a maximizer but not the only one; when a=0 the face degenerates and the ratio is zero. The off-tie limit is 2a/(p+a) and is strictly below a/p for a>p. With a=1, p=n⁻² and y=√p the step accepts the oracle output in full, with point-distance factor n and gap ratio (p/2)/(p+p²/2)=1/(2+n⁻²). Only the first update is covered. The source checker was inspected, not executed; its finite tests are ancillary to the exact reconstruction.

## originality

PASS

The algorithm, gradient-radius initialization and objective convergence are established. The distinct claim is the exact first-step distance envelope and discontinuity, including unbounded amplification on one fixed quadratic by exact tie selection and the sharp bound when selection is unique. The closest checked negative examples have materially different oracle or radius hypotheses.

## value

PASS

The example isolates a genuine failure mode of a documented default radius and exact oracle on a fixed condition-number-one objective. The sharp unique-oracle bound shows the blowup is tied to the permitted exact selection, not simply ill-conditioning or proximity to a tie; the gap contraction rules out conflating it with failure of objective descent. This meaningfully delimits first-step point-distance guarantees without claiming anything about eventual convergence or practical tie policies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
