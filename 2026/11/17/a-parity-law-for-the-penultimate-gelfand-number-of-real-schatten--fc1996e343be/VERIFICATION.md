---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For 0<p<q<=infty every rank-r nonzero matrix satisfies ||A||_q/||A||_p >=r^(1/q−1/p), including quasi-norm p<1, exponent negative. The penultimate codimension condition forces a real 2-plane. For even N, span(I,J) with J real skew-orthogonal has all N singular values sqrt(a²+b²), saturating the universal bound. For odd N the determinant of a real odd-degree pencil changes sign under (a,b)↦−(a,b), forcing a nonzero rank<=N−1 member on every 2-plane; embedding an N−1 even conformal block saturates that bound. A scalar line gives last c_(N²). Independent exact integer Gram checks N=2..15 corroborate but proof works for all N>=2 and all given exponents.

## originality

PASS

Prochno 2026 Theorem A and Remark 1.1 give broad all-index asymptotic bounds and the exact last c_(N²), but not this parity-sensitive penultimate index. Earlier Hinrichs–Prochno–Vybíral and Prochno–Strzelecki estimates similarly lack this exact last-two comparison. A published two-row rectangular theorem and complex 3×3 result cannot directly specialize to square N×N for all N. Standard real skew-complex structures and odd pencil singularity are credited ingredients; a classical matrix-pencil widths corollary remains a priority risk.

## value

PASS

Last two exact Gelfand numbers in a natural finite-dimensional Banach/quasi-Banach operator ideal are canonical endpoint invariants. The discrete parity obstruction and real-field dependence show a strict odd endpoint gap absent in even N, useful in width estimates and selection of extremal codimension-two subspaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
