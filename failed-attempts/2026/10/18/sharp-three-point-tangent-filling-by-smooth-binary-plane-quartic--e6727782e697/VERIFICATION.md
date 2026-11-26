---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Two distinct Fano lines cover five points and three cover seven if and only if concurrent. I independently solved affine binary systems rather than inspecting every form: for each three-point zero set and each bijection to the three lines of a rational pencil incident with the assigned contacts, impose all seven quartic values and the three gradients. A form contributing to the minimum satisfies exactly one such system. The resulting 448 distinct forms split by the transposition, coordinate cycle and a transvection (generating GL_3(F2)) into masks 4114,4115,4306,4309,4383 with sizes 84,84,84,28,168. Smoothness was checked algebraically: for F1 and F2, F_y=z³ and the equation force z=y=0, where F_z=x³≠0. For F3, z=0 would force y=0 and F_z=x³≠0; z≠0 and F_y=xz²=0 give x=0, and then F_x=0 gives y=0 or y=z, both off the curve. For F4, its gradients have no common projective zero on z=0. On z=1 their vanishing forces x²=y³, y²(x+1)=1, and the equation reduces to y⁴+y³+y²+y+1=0. Thus y⁵=1 but y≠1, which gives x²=1+y; substitution of y³=1+y into the reduced equation yields y⁴+y²=0, a contradiction. Mask 4306 is singular at [1:ω:1] with ω²+ω+1=0 by direct substitution. The four surviving orbits have noncollinear rational triples; centers are [1:0:0] for 4114 and [1:1:0] for the other three. The respective membership tests are yes, no, no, yes. This gives 364 smooth equations, stabilizers 2,2,6,1, and the 252/112 split.

## originality

FAIL

Exact coverage in a distinct indexed Resultary record: 206b3755df02 explicitly states the same sharp minimum, count and orbit sizes as part of a larger census, and lists the identical four defining masks and stabilizers in its TSV. The ancillary center split and noncollinearity follow by a four-representative incidence test, not a new surviving classification. This is a finding of demonstrable coverage at review, not a claim about historical precedence or attribution between the records.

## value

FAIL

The sharp extremal question and exact incidence census are naturally motivated. However, the actual frozen claim does not supply a stand-alone new result relative to the complete tabulation: the minimum and four equality forms are already listed, and the remaining center and collinearity data are a direct evaluation on those four forms. The evidence supports a correct finite check, not a separately valuable narrow advance beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
