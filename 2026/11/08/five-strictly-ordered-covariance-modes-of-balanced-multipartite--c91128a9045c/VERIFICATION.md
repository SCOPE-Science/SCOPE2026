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

For balanced complete k-partite graph with n per part (k>=3,n>=2), reconstructed L+ pseudoinverse from within-part zero sum and between-part contrast eigenspaces. Transfer-current determinant gives offdiagonal Cov(X_e,X_f)=-(b_e^T L+ b_f)^2 and variance r(1-r). The orthogonal block tensor decomposition gives zero plus L,A,T,H and for k>=4 B spectra with stated multiplicities; explicit positive differences yield strict order and condition number 2 at k=3 and 2+2/[k(kn-2)] for k>=4. Independent Laplacian pseudoinverse and numerical diagonalization for (k,n)=(3,2),(4,2),(3,3) matched all eigenvalues to 5e-16. Finite matrices corroborate, while general algebra establishes all parameters.

## originality

PASS

Existing transfer-current determinantal laws and complete multipartite spanning-forest containment formulas imply individual covariance entries, not the simultaneous exact eigenspace/multiplicity hierarchy or the sharp condition number stated here. The derivation adds a nontrivial k,n-dependent representation decomposition, although an implicit equivalent association-scheme spectrum remains possible.

## value

PASS

Uniform spanning-tree indicator covariance is an intrinsic natural second-moment metric for the graphic-matroid base polytope. The full orthogonal mode/multiplicity decomposition, strict hierarchy and sharp dimension-independent conditioning for all balanced multipartite graphs are not just marginal probabilities and provide a reusable structural example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
