---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

With characteristic 2, F=(XY+XZ+YZ)²+WXYZ has partials XYZ,WYZ,WXZ,WXY and F must be retained. W=1 chart gives reduced k[X,Y,Z]/(XY,XZ,YZ). On X=1 chart Jacobian quotient k[a,b,c]/(ab,ac,bc,b²+c²), with nilpotent ideal (b,c), independent basis b,c,b², filtration lengths 2 and 1, and support at a=0. Three symmetric points yield total nilpotent length 9, so P_J(d)=3d+1+9=3d+10 and nilpotency order 3. Independent algebraic reduction and matching published earlier chart verify the central structural lemma, not merely a logged Hilbert function.

## originality

FAIL

Decisively covered by earlier full published primary RESULT.md, without a new surviving claimed theorem.

## value

PASS

The intrinsic Jacobian singular scheme and embedded length corrections are canonical characteristic-2 invariants of a classical surface and useful for wild singularity and Hilbert-scheme comparisons; nontrivial despite known coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
