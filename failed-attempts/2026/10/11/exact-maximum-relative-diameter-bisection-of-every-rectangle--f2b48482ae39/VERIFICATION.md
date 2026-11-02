---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Under the conventional simple-arc bisection definition, Cañete–Segura Gomis Proposition 3.1 validly reduces arbitrary curved cuts without an equal-area constraint to a central segment. For R=[−A,A]×[−B,B], A≥B>0, a central cut hitting horizontal edges at (t,B), (−t,−B) has a piece containing (−t,−B) and (A,B), forcing squared diameter ≥(A+t)^2+4B^2≥A^2+4B^2 (reflection makes t≥0). A cut meeting vertical edges at (A,u),(−A,−u) forces squared diameter ≥4A^2+(B+u)^2≥A^2+4B^2. Equality in the first class forces t=0; in the second forces A=B and u=0. The vertical midline produces two A×2B rectangles, diameter sqrt(A²+4B²)=sqrt(L²/4+H²). For square there are exactly two orthogonal central optimum cuts. Analytic inequalities were independently algebraically expanded; no finite computation is taken as an all-parameter proof.

## originality

FAIL

Decisive published prior implication: the 2018 primary paper already proves the very same midpoint cut is optimal for every rectangle, not just squares. The claimed exact value follows immediately from the Pythagorean diameter of either resultant half-rectangle. The present center-line uniqueness clause may not be stated verbatim there, but its strictness is a two-case elementary inequality and does not give an independently substantive discovery. Earlier self-review PASS and a mistaken old statement that the 2018 paper had no rectangle reference were not used.

## value

FAIL

The rectangle family and max-diameter invariant are natural, but the published 2018 theorem already solves the actual optimization on all rectangles: it explicitly shows that the inradius midline is minimizing (Section 5/Figure 12). Evaluating the two resulting rectangle diagonals is an immediate textbook Pythagorean calculation. The only additional detail, strict uniqueness of the center-passing direction, is two elementary positivity inequalities and is not a motivated substantial independent exact classification once the optimizer is already known. This is a failed novelty/value contribution, not a challenge to the correctness or intrinsic importance of the fencing problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
