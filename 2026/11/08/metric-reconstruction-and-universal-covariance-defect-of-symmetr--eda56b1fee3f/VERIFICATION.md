---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification and limits

The included `verify.py` was executed as `python verify.py` in a clean standard-library Python environment. It completed successfully for 19 oriented triangulations, checking exact ridge incidence and orientations, all entries of the boundary-column Gram matrix, the antipodal distance graph, and both covariance identities with `fractions.Fraction`. It includes two 14-facet triangulated spheres from the motivating paper and finds different triangle counts for their dual graphs while agreeing on the exact covariance defect.

The proof covers all finite connected closed orientable simplicial pseudomanifolds of dimension at least one, without restrictions on the number of facets beyond those implied by these assumptions. The executable test set is finite and does not independently establish the infinite assertions. Literature-priority searches do not certify global novelty. The unitary-equivalence theorem for ordinary symmetric edge polytopes and the standard graph Laplacian formulas are acknowledged inputs/close comparisons. No independent mathematical audit has been performed.
