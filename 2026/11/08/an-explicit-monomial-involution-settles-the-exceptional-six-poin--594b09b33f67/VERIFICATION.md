---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The complete lattice-point lists agree with Figure 1.4. Reducing the six exponent pairs modulo seven gives six distinct characters for each code. They are independent: a reduced polynomial of degree at most six in each variable vanishing on the 7×7 grid is zero by univariate interpolation in each variable. The coordinate map phi(x,y)=(x^(-1),x^(-3)y) squares to the identity, and the paired weights x^3 and (x^(-1))^3 multiply to one. The weighted pullback sends (a,b) to (3-a-3b,b): the four horizontal exponents reverse, (0,1) stays fixed, and (0,-1) becomes (6,-1)=(-1,-1) modulo seven. Thus it sends precisely one basis of the evaluation code onto the other. The edge-step gcd sums give four and three boundary lattice points, ruling out integral affine unimodular equivalence. Independent exact replay in /workspace/replays/4.py passed the lattice-point, area, boundary, reduced-exponent and 49-coordinate weight/permutation checks. The frozen checker and recorded output were inspected, not executed.

## originality

PASS

The explicit monomial involution proves the precise F_8 equivalence left open in the original theorem. The prior enumerator equality supplies no equivalence certificate, the known F_7 equivalence is for a different pair, and the closest later theorem located concerns dimension seven. No distinct covering result was established in the inspected evidence.

## value

PASS

This is the exact outstanding equivalence in the dimension-six classification, not an arbitrary small code calculation. The explicit coordinate involution resolves the enumerator ambiguity and shows how finite-field exponent reduction can identify codes from lattice-inequivalent polygons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
