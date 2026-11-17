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

Derivative of Q with respect to (a,b,c,d,e) is (d^2,cd,bd,bc,b^2), so singular support is (b,d) and D is irreducible nonnormal. Substitution of [su:sw:tu+sv:tw:tv] into Q is zero, over (b,d)!=0 [s:t]=[b:d] recovers normalization parameter; projectivity plus finite quadratic fibers yields finite birational P1xP2 normalization. On affine chart a=1, put d=b lambda with lambda^2+c lambda+e=0; R=A+bA lambda has conductor bB=(b,d) with B=A[lambda]. On w=0 inverse conductor C maps to P by [su:tu+sv:tv] = quadratic unordered-pair quotient. Its diagonal [s:t]=[u:v] maps to [s^2:0:t^2] by Frobenius. Generic repeated root r^2=d/b is a nonsquare of rational function field and so degree-two purely inseparable. Counting P1xP2 minus P1xP1 plus P2 gives q^3+2q^2+q+1. Independent GF(2^m) projective enumeration for q=2,4,8 gave exactly 19,101,649; finite counts only corroborate algebraic all-q proof.

## originality

FAIL

FAIL: already completely covered by published October 26 theorem on SAME Q and normalization. Identical conductor and generically inseparable root incidence already stated. Remaining symmetric-square diagonal Frobenius and finite-field count follow directly from prior displayed incidence/quasi-finite normalization, so the central claim is not original.

## value

FAIL

FAIL as an independently new contribution, though mathematically interesting: the earlier more extensive result already gives the same local/gluing invariants plus an additional embedded Jacobian line and normalization quotient. The newly displayed branch diagonal and rational-point count are straightforward consequences of that source and lack an independently motivated fresh mathematical boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
