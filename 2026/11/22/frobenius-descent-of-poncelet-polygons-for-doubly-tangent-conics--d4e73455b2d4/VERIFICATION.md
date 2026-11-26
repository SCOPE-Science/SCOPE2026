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

The numerical and period conclusions agree with the proof. The original's natural torus wording is corrected: every scale of the contact-complement parameter preserves the conic pair and induces a translation on cycles, so the pair cannot distinguish an identity cycle. The canonical quotient is the torsor U/T[n], with T the connected contact stabilizer, and over a finite field choosing any rational origin identifies it with T/T[n] ≅ T. To verify the rest, the square of the contact chord cuts out 2P+2Q on C and hence D lies in the claimed pencil. Diagonal and anti-diagonal binary coordinate changes scale the two split monomials equally, proving uniqueness of the parameter. Substitution in the dual conic gives (s+t)^2=4cst; excluding c=0,1 removes exactly steps ±1 and ensures simple coset cycles. The split parameter has Frobenius t→t^q; in the nonsplit norm model it is t→t^(−q), as the two contact coordinates exchange. The n-th-power quotient has the same descent and exactly q^m−epsilon^m rational parameters. For representative z^a with order(z)=n(q−epsilon), Frobenius acts by k→epsilon*a+epsilon*q*k mod n. Counting fixed k gives uniform rotations or the parity classification of reflections, and the argument applies to powers including even degrees, when both signs agree. Independently computed the chord discriminants on actual projective points over quadratic fields, including F81/F9; these corroborate complete reflection counts and the rotation portion visible in those fields (python3 /workspace/branches/independent_finite_fields.py). The frozen script was inspected, not executed. The proof, not bounded computations, gives all prime powers and extension degrees.

## originality

PASS

PASS is for the repaired torsor and the all-extension setwise-cycle counts stratified by vertex rationality. The frozen class/step and fully rational-vertex counts substantially overlap a distinct same-date catalogue theorem and no ordering is inferred from the date. The repair explicitly credits those counts, does not foreground them as novel, and distinguishes setwise descent from rational-vertex descent geometrically and numerically.

## value

PASS

For the whole double-contact stratum the quotient answers whether the polygon itself descends and how much of its vertex set is individually defined, two distinct geometric-arithmetic questions. A rational tangent graph can be empty yet every invariant odd cycle has one rational vertex; even reflection gives a different equal split. The torsor and exact extension distributions distinguish these natural regimes rather than merely recounting known rational polygons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
