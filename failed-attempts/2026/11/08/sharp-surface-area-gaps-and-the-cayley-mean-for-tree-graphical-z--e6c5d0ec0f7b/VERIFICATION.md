---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the zero-sum Euclidean hyperplane the tree incidence matrix has squared column volume n by Cauchy–Binet and its unimodular row deletions. The dual normal to the facet omitting a cut of size k is the centered indicator of a cut side, of norm sqrt(k(n−k)/n). The volume-to-height identity gives area sqrt(k(n−k)) for each of the two opposite facets. For each k≥2 the qualifying cut edges form a connected core: any edge between two qualifying edges has at least k vertices toward each. A core of h≥1 edges contributes h+1 vertices, with at least k−1 further vertices beyond each of two end cuts, so h≤n−2k+1, the path count. Summation by parts weights these tail counts by strictly positive increments. The leaves determine F₂; the star and path are the only first extrema. A nonstar attaining the second-minimum bound has just one nonpendant edge of smaller size two, giving the subdivided star. A nonpath attaining the second-maximum bound has three leaves and just one size-two cut; if two arms have length at least two they produce two such cuts, so the arms are 1,1,n−3. This shape loses only the size-two tail entry relative to the path, including at n=5; both exact gaps are twice the size-one to size-two increment. For the Cayley mean, the labeled trees with a specified one-edge split are counted by the product of two Cayley counts and k(n−k) choices of bridge. Double counting oriented sides cancels the factor two for opposite facets. Uniform Stirling reduces the kth mean summand to n^(5/2)/(sqrt(2π)k(n−k)) times 1+O(1/k+1/(n−k)); summing yields precisely the stated constant and O(n^(3/2)) remainder. This proof uses the specified metric and labeled law. The inspected check_surface.py is a finite floating-point replay and was not executed.

## originality

FAIL

Two distinct published Resultary findings cover the asserted scientific contributions under the same normalization: one gives the cut formula and the full first- and second-extremal ladder with equal gaps, and the other gives the exact Cayley mean and its logarithmic asymptotic. The frozen record combines these previously existing statements without an additional supported conclusion. Equivalent coverage is independent of resolving chronological priority.

## value

FAIL

The natural area invariant does distinguish shapes with identical volume, and the exact second extremes and random mean are intrinsically useful facts. This frozen record adds no independently useful invariant, parameter range, or inference beyond the exact existing geometric and probabilistic results. Collecting both known conclusions on one page is not a distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
