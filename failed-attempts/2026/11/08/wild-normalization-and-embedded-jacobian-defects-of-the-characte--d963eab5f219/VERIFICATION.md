---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

F is linear in W with coefficient XYZ coprime to (XY+XZ+YZ)^2 and so geometrically integral. Four quadrics [a²+b²+c²:bc:ac:ab] have no common projective zero, provide finite birational normalization by recovering parameter [YZ:XZ:XY] where XYZ!=0. The Jacobian in char2 has partials XYZ,WYZ,WXZ,WXY; in chart X=1 it reduces to J=(yz,wy,wz,(y+z)^2). Its radical is (y,z), module quotient (y,z)/J has basis y,z,y²=z² annihilated by w, length 3; at W=1 Jacobian ideal is (XY,XZ,YZ), three reduced axes. On a normalization coordinate edge the map lambda=t+t^-1 has one wild branch point at t=1 (separable quadratic field extension, index 2, characteristic 2). Duality of finite normalization from plane P2 to quartic surface yields conductor O_P2(-3). For each GF(q), q=2^m, (q-1)^2 points on XYZ!=0 plus 3q+1 boundary points yields q²+q+2, zeta [(1-T)^2(1-2T)(1-4T)]^-1. Independently enumerated q=2,4,8 with counts 8,22,74; this does not replace the proof.

## originality

FAIL

FAIL: October 25 published SAME Steiner polynomial, same P2 normalization and one-wild-branch/length-three defects, and same q counts/zeta. The submitted results reproduce its central assertions exactly; the conductor twist is an elementary duality consequence.

## value

FAIL

FAIL as separate new mathematical finding because exact branch/embedded-defect and all-q arithmetic classifications were established in full earlier work; the additional O(-3) conductor computation is a standard dualizing-sheaf deduction, not enough mathematical motivation to rescue the covered package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
