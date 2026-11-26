---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For n>=3 the diameter is two and any edge extends to a distance-two path by changing the other coordinate. Every maximal geodesic is therefore a three-vertex L. The vertex bound is n; in any packing attaining it, each column supports at most one two-cell pivot and hence exactly one. Its residual cell must be a wing, forcing the wing mapping to be a derangement. If f(i) is the wing row at i, the path pivoted at i has center row f(pi(i)) and must avoid f(i). Conversely inequality of those colors specifies the center, the unique other pivot row and the wing, occupying every cell exactly once. No orientation or ordering factor occurs. A properly colored n-cycle proves attainment. The three-color adjacency matrix has eigenvalues 2,-1,-1, so the trace of its ell-th power gives 2^ell+2(-1)^ell including ell=1,2. The labelled cycle exponential formula gives the stated EGF; extracting coefficients by partial fractions yields the scalar count. Independently checked all displayed distributions by recursively choosing the labelled cycle containing column 1, weighting its j possible positions by the factor (j-1)!(2^j+2(-1)^j) for a selected j-set. This check is supplementary to the all-n bijection.

## originality

PASS

Pass applies to the canonical graph-geodesic bijection and cycle refinement of every optimizer, not to the already known maximum cardinality, coefficient array, bivariate EGF or row sums. The strongest inspected indexed cardinality and polynomial results do not identify the three-row optimizers with properly colored derangements. Historical priority is provisional.

## value

PASS

The result identifies every optimizer and gives a canonical graph interpretation and refinement of a preexisting triangle, rather than recomputing a tabulated number. The sharp size alone is already covered, but the all-n pivot/wing inverse construction allows one to generate and distinguish all maximum packings in the natural three-row family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
