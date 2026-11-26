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

Invertibility gives smoothness from the gradient AᵀX^[2]. In the tangent plane at u write X=tu+w with w in a complement of u. The t³ and t² terms of F vanish, and the t term is w^[2]ᵀAu. It vanishes on the whole tangent plane precisely when Au is proportional to Aᵀu^[4], by taking the square of the tangent linear form. Then the residual homogeneous binary cubic splits into three lines through u; a repeated line would force a singular point since the normal derivative, of degree two, has a zero on that line. Conversely a concurrent triple forces the t term to vanish. Rescaling projective coordinates reduces proportionality to u^[4]=Bu with B=(Aᵀ)⁻¹A. All normalized solutions lie in the splitting field F_(2^(2 ord B)) by iteration, and those on the surface give the geometric Eckardt set. I independently constructed a basis for the normalized vectors using a twisted trace, verifying nonsingularity, then used FLINT to enumerate projective points and row-reduced 2-subspaces in this transported F4 geometry. Each of the 27 surviving subspaces lies on the surface because the cubic restriction vanishes at all five distinct F4-points, and the geometric total is 27. Plücker coordinates and Frobenius fixed counts of powers give the line cycles without constructing five-star subsets or using the packaged verifier. Independent full binary change-of-basis enumeration gives precisely the disjoint matrix orbits listed, of total size 20160. Matched all ten rows in every numerical column, in particular the equal-Eckardt/different-line pair and the three degree-12 Eckardt places of 128d. The zeta formulas follow from the cycle partitions.

## originality

PASS

Credit existing geometric counts, the prior binary surface setting and rational counts, the general Weyl-class line types, and the exact Clebsch row. The supported distinct content is the complete marked assignment of joint Eckardt and line cycles to these ten binary matrix forms, in particular the same Eckardt spectrum for the two stated binary forms with different line spectra. A list of possible line types without the marked assignment or tritangent action is not this table; an inaccessible potential table remains a priority risk, not negative evidence.

## value

PASS

These are two intrinsic finite arithmetic configurations on a natural complete family. The joint assignment gives exact extension degrees of definition and separates two forms with the very same complete Eckardt zeta function by the arithmetic of their lines. The complete marked table, including actual degree-twelve places, is useful when the input is an explicit binary form and a general abstract Weyl list or counts of rational lines cannot directly give the answer. The known possibility of an abstract line type and the already solved Clebsch example are not counted as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
