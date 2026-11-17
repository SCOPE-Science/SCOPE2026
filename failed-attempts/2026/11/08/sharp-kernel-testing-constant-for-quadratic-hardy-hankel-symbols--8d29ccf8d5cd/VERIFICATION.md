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

Matrix of H_{overline{az+bz²}} is [[conj(a),conj(b)],[conj(b),0]], so operator norm L=(A+sqrt(A²+4B²))/2 and the kernel test squared maximizes (1-r²)((A+Br)²+B²). With u=B/L, testing r=u/2 yields K²/L²>=(1-u²/4)(1+u^4/4); polynomial identity minus 25/27 equals (8-3u²)(3u²-2)^2/432>=0 for 0<=u<=1 (independently algebraically verified). At a=1,b=sqrt6, the radially optimized kernel function is strictly concave, attaining 25/3 at r=1/sqrt6, and L=3. Equality requires u²=2/3 i.e. B=sqrt6 A; pure monomials covered. Code was inspected; analytic proof establishes universal claim.

## originality

FAIL

FAIL: the October 26 Resultary prior exactly proves sharp kernel fraction 5/(3sqrt3) and equality |a|=|b|/sqrt6 for every quadratic Hardy Hankel symbol az+bz², with unique extremal kernel radius; November 1 prior independently gives the identical reciprocal 3sqrt3/5 bound and full equality cases. Complete primary RESULT.md texts read. Same operator, coefficients, normalized Szegő kernels, and equality parameters: the present final claim is fully covered.

## value

FAIL

FAIL: a mathematically correct but already published sharp two-parameter norm ratio and equality classification is a recomputation, with no new natural invariant or structural remainder claimed. Source package preserved without cosmetic certificate-based salvage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
