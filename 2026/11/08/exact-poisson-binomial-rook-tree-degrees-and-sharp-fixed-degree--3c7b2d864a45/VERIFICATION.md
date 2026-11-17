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

On L=m P_m tensor I_n+n I_m tensor P_n, the three nonconstant eigenspaces yield its exact pseudoinverse. Incident-edge transfer-current matrix has zero-sum eigenvalues (m+1)/(m(m+n)) and (n+1)/(n(m+n)), and the constant two-sector eigenvalues 1 and 2/(m+n). The determinantal tree-degree PGF therefore factors exactly. The second derivative of f_s =((4s-5)t-2)/[t^2((s-1)t-1)^2] is positive on [2,s-2], so the symmetric leaf factor minimizes at a balanced pair and maximizes at the endpoints. Le Cam plus elementary upper bounds gives TV <=17/(4s). Independently computed exact weighted-Laplacian cofactors for (2,2),(2,3),(3,3),(3,4), agreeing as complete polynomials, and symbolically differentiated f_s.

## originality

PASS

General UST transfer-current methods and strongly-regular graph results already yield some square rook-graph degree formulas, and the generic large-degree Poisson limit is known. For all rectangular factor sizes, the evaluated 3-class PGF and sharp fixed-original-degree leaf extrema survive comparisons; a square-case finite formula must not be claimed as novel.

## value

PASS

Uniform rook trees are natural symmetric UST examples whose vertex counts and root degrees vary independently at fixed original graph degree. Exact full local law plus strict factor-balance extremizers gives reproducible finite-size tree-shape comparisons and a uniform quantitative Poisson approximation; these exact structural statements have intrinsic use beyond the previously known limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
