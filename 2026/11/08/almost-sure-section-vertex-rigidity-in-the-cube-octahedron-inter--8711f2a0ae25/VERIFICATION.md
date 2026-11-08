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

# Verification notes

The analytic theorem is proved by counting strictly crossed edges for generic normals, and by constructing explicit open direction sets for each nonrigid parameter. Proof validity does not depend on finite sampling or external code.

## Reproducibility

Run `python3 cuboctahedron_section_checker.py` in any ordinary Python 3 installation. The script uses only the standard library and exact rational arithmetic to intersect the fourteen facet inequalities in each central plane. It enumerates feasible vertices by pairwise constraint intersections and forms the planar convex hull with an orientation predicate. It does not reuse edge-sign counts, providing a distinct finite check.

The local test printed `OCTAGONAL_RIGIDITY_EXACT_RATIONAL_CHECK_OK 1915`, after representative checks at nine parameter values and further rational normal samples. These tests are a finite corroboration, not exhaustive proof for all real parameters or viewing directions.

## Scientific limits

The central-plane and Haar-uniform hypotheses are essential. Nongeneric normals can have fewer vertices. No distribution for nonrigid parameters, stability under perturbation of the body, or global uniqueness among all three-polytopes is asserted. Independent review remains not performed.
