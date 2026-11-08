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

## Finite verification

The embedded `verify_gp.py` and `verify_incidence.py` run on independent combinatorial models, one given by generalized Petersen edges and one by the Levi-incidence relation. The incidence verifier checks a bijection carrying all twenty-four generalized Petersen edges to the incidence edges. The two implementations use different enumeration representations and independently establish that the exact secure-set counts are zero at sizes zero through six and 336 at size seven. Every single-vertex replacement is tested; both programs reproduce 1392 undirected jump edges, 528 slide edges, one connected jump component, and the exact 288-plus-twenty-four-pairs slide decomposition, degree distributions, and all component eccentricities.

To reproduce, run `python3 verify_gp.py` and `python3 verify_incidence.py` in a directory containing the scripts; compare their standard output with `gp_output.txt` and `incidence_output.txt`. Computations are exhaustive for the stated sixteen-vertex universe, not proofs of analogous infinite-family statements. Bibliographic comparisons provide a qualified originality assessment, not an exhaustive historical-priority guarantee. External independent audit has not been performed.
