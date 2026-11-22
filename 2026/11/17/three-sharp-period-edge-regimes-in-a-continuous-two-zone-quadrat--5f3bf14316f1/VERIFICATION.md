---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

The diffeomorphism q=-log(1-y) gives qdot=x and potential U_c(q)=(1-c)q+(1-2c)(exp(-q)-1)+(c/2)(exp(-2q)-1), Uc derivative=(1-exp(-q))*(1-c*(1-exp(-q))). Left side q<0 is strictly restoring and tends to infinity for h>=0. Right potential increases without bound for k<1, tends to 1/2 for k=1, and has a unique maximum at q_s=log(k/(k-1)) with barrier E*=1-1/(2k)+(k-1)log(1-1/k), curvature -(k-1)/k, for k>1. Period quadrature sqrt(2)*integral dq/sqrt(E-V(q)) gives linear-tail sqrt(E), exactly integrated critical potential gives inverse-square-root and the outgoing qdot gives t^2(1-y)->2 and t*x->2, and nondegenerate saddle curvature gives the logarithmic coefficient 1/sqrt((k-1)/k). The left contribution is lower order/bounded in all edge limits, so leading terms do not depend on h. Independently checked numerical potential derivatives for multiple h,k and exact saddle height; finite checks do not prove edge asymptotics. No period monotonicity claimed.

## originality

PASS

The exact local center condition belongs to da Cruz–Torregrosa Theorem 1.4; it does not imply maximal global annuli or their physical-time boundary coefficients. Marín–Villadelprat treat smooth Loud-center outer critical periods, not complete two-zone h/k classification. Rezende et al. 2026 Theorems 1–2 analyze local isochronicity and critical periods. An unrelated two-zone linear crossing theorem has different vector field and spectral edges.

## value

PASS

The explicit global transition between an unbounded linear potential, a limiting finite-height barrier at infinity, and a finite saddle is a natural complete classification in a motivated quadratic center family. Exact three different physical-time period exponents, escape coefficients and independence from the lower-zone parameter provide sharp dynamical boundary information beyond textbook local center tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
