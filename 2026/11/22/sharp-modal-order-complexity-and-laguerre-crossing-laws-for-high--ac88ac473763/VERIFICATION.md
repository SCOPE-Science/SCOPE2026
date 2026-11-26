---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the stated Gaussian measure, angular integration and the radial substitution t=|z|^2 give the normalized Laguerre densities; for k<q the negative-parameter reduction converts to the ordinary positive-parameter norm with min(q,k)!/max(q,k)!. Writing A=L_q^(k-q), B=L_q^(k+1-q), the finite sums give A'=A-B and xB'=(k+1)A-(k-q+1)B. Differentiating e^(-x)x^(k-q+1)AB gives the negative of the density difference times (k+1)!/q!. The boundary expression is O(x^(k-q+1)) for k>=q and O(x^(q-k)) for k<q, so integration gives the exact formula for all k. Each factor's finite positive roots are simple by Laguerre orthogonality after the negative-parameter reduction; the contiguous first-order system prohibits a common positive zero by uniqueness on x>0. Thus the number of simple sign-changing positive roots is min(q,k)+min(q,k+1). For fixed x, the index polynomial is [t^q](1+t)^y exp(-xt), of degree q and leading coefficient 1/q!. Averaging the product of two generating functions under Poisson(x) gives exp(xst), proving orthogonality to all lower-degree polynomials. If fewer than q roots changed sign in (0,infinity), multiplying by the product of those distinct factors would give an integrand of one sign on the nonnegative support and nonzero on infinitely many atoms, contradicting orthogonality. Thus the q index roots are all positive and simple. A strict ascent uses a disjoint open integer interval containing a root. Each maximal finite local-maximum run except a possible initial one has a preceding strict ascent. The eigenvalues are positive and tend to zero for fixed x (the factorial dominates the radial power times the polynomial-in-k density factor), so the infinite tail supplies no further plateau. With y=x+u sqrt(x), t=v/sqrt(x), expanding the logarithm gives locally uniform generating-function convergence to exp(uv-v^2/2); coefficient and simple-root convergence give the stated Hermite scaling. The gaps between index roots tend to infinity, so use separation >2, not just >1, to ensure an intervening descending step between rising unit intervals. At large x all roots are also away from index zero. Off the countable set of integer index roots the steps have no ties, the ascents are isolated, and there are exactly q+1 strict local maxima including the left endpoint.

## originality

PASS

Pass for the complete sharp higher-order spectral census and its all-index ascent application, not for the disk diagonalization, Laguerre recurrences, Charlier orthogonality, or Charlier–Hermite limit. The exact product follows rather quickly from classical relations once the disk marginal is written in Laguerre variables; the new content supported here is how it yields the all-level crossing and modal bounds together. Earlier q=1 and q=2 laws and exact classical root results are credited. Priority is provisional.

## value

PASS

Exact crossing counts and a sharp global limit on spectral turns give useful information about disk concentration modes that diagonalizing the operator alone does not reveal. The bound is independent of disk area and the number of modes inspected; the Hermite-scale root locations explain its eventual attainment through a structurally different index variable. This is a natural all-order invariant of the disk-localization problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
