---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For smooth char2 cubic X with nonzero squarefree tensor and canonical point p not on X, alternating Hessian has ker span{x,p}; the polar derivative in direction p is a square L^2 and p off X makes L transverse. Coordinates reduce F to C(x0,x1,x2)+u^2M+u^3, with C smooth ordinary ternary cubic. Tangent linear algebra gives differential rank 2 off R=X intersect {u=0}, rank 0 on R. In local smooth coordinates every differential entry is divisible by u^2 and its divided two columns are independent on R, forcing maximal-minor ideal exactly I_R^4, degree 12. Inspected verify.py: one smooth sample over F2/F4/F8 and a symbolic local minor u^4/t^3; additionally independently checked this local minor algebraically. These finite tests do not establish the global scheme identity; proof rests on local division and transversality.

## originality

PASS

Characteristic-two canonical point and square polar were already established by Dolgachev–Duncan. The surviving contribution is the *scheme-theoretic fourth power* of the differential maximal-minor ideal for the original smooth cubic embedding, with exact zero/two rank jump. Older Gauss-rank-zero papers discuss existence of alternative embeddings, not this intrinsic critical thickening. Highly relevant Fukasawa–Furukawa–Kaji (2010) full text could not be inspected; priority is qualified, not falsely certified.

## value

PASS

An exact fourth-order scheme-theoretic Gauss degeneracy is a nontrivial wild-ramification invariant invisible to reduced rank loci; the uniform degree-12 thickening on smooth char2 cubics is structurally motivated by the canonical-plane geometry, beyond a routine Hessian rank check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
