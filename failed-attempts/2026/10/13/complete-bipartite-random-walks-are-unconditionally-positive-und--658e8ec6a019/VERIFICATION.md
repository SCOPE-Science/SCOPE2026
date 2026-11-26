---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The substantive theorem is correct. The scalar φ(x)=(x²−6x+12)/(x²+6x+12) is positive for x≥0, equals one at zero, and is strictly less than one for x>0. Decompose a complete bipartite Laplacian into the constant mode, both within-part sum-zero modes of respective eigenvalues q,p, and the contrast mode of eigenvalue n=p+q. The cross entry is f(n), where f(x)=(1−φ(hx))/x=12h/((hx)²+6hx+12), and the within-p off-diagonal entry is q[f(q)−f(n)]/p, strictly positive by decreasing f for h>0. Exchange p and q for the other part. The diagonals are positive by spectral positivity, and L1=0 gives unit row sums. For P4 the independent symbolic adjugate computation reproduces every entry orbit, the positive common denominator, the endpoint-neighbor factor −3h times the specified quartic, and −60/84973 at h=12. Both diagonal numerators have positive coefficients; the other three off-diagonal orbit numerators have nonnegative coefficients. Descartes’ rule and the signs at zero and infinity give the single positive cutoff, approximately 11.86637854392656. The only connected bipartite graphs of order two and three are K1,1 and K1,2; the omitted singleton has L=0 and an identity step, so four is indeed minimal. Two incidental wording slips are the classification ‘at most three’ without carving out the singleton and the description of Φ₁₂ as ‘row-stochastic’: it has unit row sums but is not stochastic. The packaged code was inspected, not executed; replay the independent factorization with python3 /workspace/branches/independent_algebra.py.

## originality

FAIL

Verified coverage in a distinct indexed theorem: the complete-multipartite October 25 record proves the K_{p,q} assertion as a special case and gives the exact same P4 interval with the identical endpoint numerator and denominator. The h=12 fraction is a substitution; four-vertex minimality is immediate from the same results plus the elementary order-at-most-three classification. A separate October 13 record already covers the K_{p,q} half via an even more general filter criterion. This is a comparison of content available in the reviewed corpus, not a finding that the October 25 record predates the frozen record or that either same-day item has priority.

## value

FAIL

The positivity cutoff is a useful invariant and the graph-structured phenomenon is substantively motivated. As a separate finding here, however, the family is a special case of the available complete-multipartite theorem and the exact cutoff is already calculated there. The numerical witness and small-order corollary add no distinct useful invariant. Wording fixes would not supply a surviving scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
