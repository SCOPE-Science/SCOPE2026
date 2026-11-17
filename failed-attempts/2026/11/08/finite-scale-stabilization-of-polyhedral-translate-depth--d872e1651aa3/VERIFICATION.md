---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For an irredundant full-dimensional compact polytope, the facet-interior point p_i has strict slack against all other facets, so s>0. A closed translate excluding query y must be contained in some strict facet halfspace, giving one inequality. With compact support in an R-ball, t>=2R/s, a facet-aligned translate at h< <u_i,y> contains exactly the support halfspace slice <=h; continuity from below handles positive atoms on the query plane and yields all-y equality with closed halfspace survival mass. For continuous everywhere-positive densities, a bounded maximizing translated polytope has strictly less mass than its containing halfspace, so no finite t matches the limit. Independently verified facet-slack algebra and inspected rational-coordinate witness checker; tests are corroborative, not all-measure proof.

## originality

FAIL

Two full earlier published results dated 2026-11-01 establish the identical full-dimensional all-polytope, all-compact-law, all-query finite stabilization including atoms. One gives the exact same eta=s normal-unit cutoff t eta>=2R and box optimality, while the other gives the stronger directional support-width threshold T=max_{i neq j} W_j/(b_j-<a_j,p_i>), often below 2R/s. Their strict-halfspace complement is precisely the submitted closed upper-tail formula. The Gaussian nonstabilization observation follows by ordinary positive-density strictness and is not an independently motivated substantial remainder.

## value

FAIL

The compact-support all-polytope stabilization theorem, finite facet-depth formula, and even stronger/sharper stopping thresholds were published earlier. Re-expressing the prior theorem with Euclidean-ball radius and reporting easy unbounded-support strictness is not a new natural classification or unknown invariant. No independently valuable corrected theorem is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
