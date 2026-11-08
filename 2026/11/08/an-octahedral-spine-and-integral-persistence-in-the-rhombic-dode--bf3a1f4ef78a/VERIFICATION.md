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

# Reproducibility and scope

The self-contained script `verify_rhombic_cech.py` and the exhaustive ordered certificate `collapse_pairs.tsv` are included with the result. Execute `python3 verify_rhombic_cech.py collapse_pairs.tsv` using Python 3; the script requires no packages outside its standard library. An actual successful run is recorded in `verification.log`.

The verifier checks graph vertices, edges and distances, all graph Čech generating facets at scales two and three, complete simplicial face sets and face vectors, and every one of the 626 free codimension-one collapse pairs. It checks that the remaining complex is exactly the 27-face octahedral boundary, including the empty face. It independently checks two complete acyclic scale-two Morse matchings through full directed Hasse-graph topological sorts, binary simplicial boundary ranks, and all 48 symmetry actions on the graph and the octahedral orientation cycle.

These checks are exact and exhaustive for this graph and the stated scales; they are not computations over arbitrary graph families. The integral homotopy conclusion uses the verified collapse and Forman's theorem. The integral persistence conclusion follows by naturality of the inclusion of the octahedral sphere into both nerves, rather than a field-only rank calculation. The finite proof does not determine additional scales or supply independent external validation.
