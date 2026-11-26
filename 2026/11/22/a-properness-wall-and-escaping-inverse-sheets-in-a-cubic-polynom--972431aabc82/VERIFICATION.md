---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The target coordinate u fixes y. At u=0 the equation is bx=w, so b≠0 gives one regular inverse and b=0 gives the collapsed line only for w=0. For u≠0 write h=1-b/(3u²); the derivative is 3u²(x²-h). The critical values at x=∓sqrt(h), h>0, have w=±2u²h^(3/2); the remaining simple root at w=E is 2sqrt(h) and the negative-height case is its sign reversal. The h=0 case has one root, triple only when w=0. Since det DF is minus the cubic derivative, at a critical point x≠0 the derivative of that determinant along the kernel is nonzero, giving a fold. For b>0 the two x=0 critical points have a critical-image parametrization with independent second and third jets in the two coordinate directions, giving ordinary cusps. The |x|≥2 sign bound implies properness for b>0 and onto follows from the cubic and exceptional linear slice. The regular value (0,M) has a single inverse with determinant -b, fixing the oriented degree at -1. For b<0, at fixed w=0 the escaping roots are exactly ±sqrt(3-b/u²). For general bounded w set s=|u| and solve z³+(b-3s²)z-ws=0 with z=sx. The three simple zeros at s=0 have derivatives in z of b,-2b,-2b; smooth implicit branches near these zeros and bounded w give the claimed uniform expansion, including the finite limit w/b. Substitution in the height formula gives the stated 1/|u| coefficient. At b=0 the two fold curves for u≠0 extend to w=±2u², tangent at the collapsed value. Counts refer to distinct real affine inverse points and no stronger forward dynamics follow.

## originality

PASS

The source family, depressed-cubic discriminant, and ordinary fold and cusp tests are known. The independently supported novelty is the combined sign classification across the singular slice u=0, with the global properness, finite fiber and quantitative real escaping-sheet laws for this specialization. The available same-family primary excerpts and other comparisons do not settle the claim by an existing statement, though the original article body could not be re-inspected independently in this run.

## value

PASS

The simplest normalized odd polynomial with two turning points in the source family gives a natural, explicit whole-plane inverse benchmark. The useful distinction is between a sheet count changing at a finite fold and two sheets disappearing to infinity over a line of regular values. The exact phase diagram and constant-order displacement make that distinction quantitative; neither a textbook cusp example nor an isolated numerical root calculation establishes it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
