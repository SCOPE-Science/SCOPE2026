---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

An ordered product is nonempty exactly when some image point of the first applied map is in the domain of the next. Thus all products, including equal pairs, vanish exactly when the aggregate domain and image sets are disjoint. Every nontrivial such family lies in one described cut family. The latter contains every permitted singleton arrow, so both aggregate supports are saturated and cannot be enlarged; the zero-only family is not maximal for n>=2. A map of domain size k and rank r is specified by choosing the domain, image and ordered list of r positive consecutive fiber sizes summing to k. This gives the displayed coefficient, including the constant 1 for the empty map. Summing over rank by weakly increasing words gives B(d,e)=sum_k binom(d,k)binom(e+k-1,k). Summing in e first gives y/(1-y) times ((2-y)/(1-y))^d, so the bivariate formula follows by the geometric sum in d. Setting x=y yields the even Fibonacci series. Removing d=0 removes one, not a binomial multiplicity; labeled cuts have separate multiplicities binom(n,d). The supplied check is bounded through n=5; the independent direct-composition maximal-clique check at /workspace/branches/independent-finite-checks.py recovered 2,6,14 families at n=2,3,4 with exact rank/domain coefficients and profile sums 3,8,21.

## originality

FAIL

The classification and family count are the m=2 case of Ganyushkin–Mazorchuk's Theorem 5.15 and Corollary 5.16, after checking their hypotheses on this noninjective semigroup. OEIS A208341 already has the exact unweighted table, its rational generating function after reindexing, and its Fibonacci row sums. Moreover A049600 has a bijective path model for the table in which the rank/domain refinement is just a choice of interior abscissae, distinct heights, and positive multiplicities. The remaining attachment of this routine refinement to the covered cut classification does not establish a distinct scientific claim of the required scope.

## value

FAIL

The exact cut sizes are a natural statistic, but the ambient-family structure and count are a direct instance of a broader theorem and the full unweighted profile is an existing array with known row sums. The added weighting is immediate from choosing the domain, ordered heights and a composition. This provides no substantive surviving gap for a repair as a standalone finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
