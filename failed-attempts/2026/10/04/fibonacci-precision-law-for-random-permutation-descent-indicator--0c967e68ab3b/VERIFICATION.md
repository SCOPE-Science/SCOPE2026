---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a uniform permutation, each descent indicator has variance \(1/4\), adjacent descents occur with probability \(1/6\), and nonadjacent indicators are independent, so \(12C\) is exactly the Jacobi Toeplitz matrix with diagonal three and off-diagonal minus one. Its continuant determinants satisfy \(d_r=3d_{r-1}-d_{r-2}\), hence \(d_r=F_{2r+2}\). The standard tridiagonal inverse cofactor formula then gives the stated Fibonacci entries. Normalizing negative precision entries gives the stated full-order linear partial correlations, and Binet ratios give the bulk limit. Fresh exact enumeration of all permutations through \(N=7\) reproduced the covariance matrix. No correctness defect is present.

## originality

FAIL

The same-object descent process is already published as a stationary one-dependent determinantal process, with exact finite descent-set probabilities. The local covariance matrix follows immediately from the standard one-, two-, and one-dependence probabilities. Explicit inversion of a general Jacobi tridiagonal matrix is classical and published; the audited inverse is its constant-coefficient Toeplitz specialization, while the Fibonacci form is just the solution of the resulting second-order continuant recurrence. The partial-correlation formula is the standard negative normalized precision entry. Thus every novelty-bearing clause is mechanically implied by known same-object second-order data plus classical matrix inversion, even though the combined formula was not located verbatim.

## value

FAIL

The sign reversal between marginal independence and negative linear partial correlation is a neat statistical observation, but after the known descent covariance is written as a Toeplitz tridiagonal matrix, the determinant, inverse, Fibonacci simplification, and partial correlations are standard linear-algebra consequences. Under the common value bar this is a textbook-level specialization rather than an independently motivated mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
