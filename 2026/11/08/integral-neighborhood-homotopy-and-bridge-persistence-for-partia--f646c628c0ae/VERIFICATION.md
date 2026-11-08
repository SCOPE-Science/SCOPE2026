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

The general proof uses explicit simplicial covers, private-apex collapses, homotopy pushouts, and a natural integral Mayer–Vietoris diagram. It proves every stage and every induced integer homology map for all parameters, not merely the finite cases.

Run `python3 verify_filtration.py` using Python's standard library. The script independently builds the graph neighborhoods and the entire face sets, checks nesting, and calculates both simplicial mod-two homology and persistence by boundary-matrix reduction for every integer parameter pair with \(4\le m\le8\) and \(0\le t\le m\). The results should exactly match `verify_filtration.out`; the last line is `ALL_MATCHED_CLIQUE_NEIGHBORHOOD_CHECKS_PASS`. No external data files or dependencies are required.

Finite-field computations cannot establish the claimed integral homotopy or integral persistence in general; those assertions follow from the explicit all-parameter argument. The stagewise wedge splittings are not asserted to be coherent equivalences of filtered spaces, and equivariant homotopy types are not computed.
