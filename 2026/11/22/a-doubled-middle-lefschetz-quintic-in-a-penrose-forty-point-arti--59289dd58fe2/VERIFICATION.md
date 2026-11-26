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

After w=−x−2y−3z I independently span each J_d by monomial multiples of the five quartics and take rational ranks, obtaining (1,3,6,10,10,6,3,1,0) in degrees 0–8. All degrees above 8 vanish because the quotient is standard graded. The joint x,y,z multiplication kernel modulo J is zero below degree 7 and is one-dimensional in degree 7, giving the Gorenstein socle independently of the cited Pfaffian description. The original dimension-one Gorenstein ring is Cohen–Macaulay, so the finite-dimensional quotient proves regularity of h. The ordered quartic quotient basis extended by the printed five relations gives a full degree-four matrix of determinant −108 in the same ascending exponent order. Using its inverse to project the ten cubic products gives 27 det M=Q² by 66 exact rational checks on i,j≥0 with i+j≤10 at W=1: this is a unisolvent grid for degree ≤10, since evaluation in the falling-factorial basis has triangular order and nonzero diagonal. Homogeneity recovers the entire identity, including W=0. Exact ranks are (8,8,8,8,10) at the four claimed directions and (2,3,5), respectively. Rational factorization gives one quintic factor of multiplicity one and gcd(Q,Q_U)=1, not merely a nonzero gcd; the reduced divisor remains reduced after characteristic-zero base change. No absolute irreducibility or claim about other sections is needed. Replay: python3 /tmp/opencode/penrose-private-review.py (SymPy 1.14, independently written exact linear-algebra check); the uploaded checker was inspected but not executed.

## originality

PASS

Qualified PASS for the exact scheme-theoretic middle determinant in the specified regular section, including its multiplicity and named rank drops. The Penrose generators, Gorenstein property and Hilbert function are antecedents, and a general weak Lefschetz existence result would not settle this determinantal scheme.

## value

PASS

The middle rank-drop scheme is a natural invariant of a Gorenstein section of a canonical highly symmetric point configuration. A doubled quintic rather than a reduced decic is substantive scheme information, with explicit corank witnesses and a generically invertible map. The section is a reproducible regular rational witness to that behavior, not a claim that one choice settles the generic-section problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
