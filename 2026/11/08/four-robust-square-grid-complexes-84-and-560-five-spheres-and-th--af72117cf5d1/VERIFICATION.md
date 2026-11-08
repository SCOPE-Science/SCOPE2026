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

# Reproduction

Run `python3 verify.py` with standard Python 3.10+; no third-party modules are needed. The saved execution result is `verification_output.txt`. The verifier enumerates all subsets up to size 6, independently tests forbidden independent four-sets, builds the matching and every Hasse incidence, topologically sorts the directed graph, and compares all 16 rational character values with the signed permutation character on triples of unit square faces. A checker passing is a complete finite proof only because every possible face has size at most six (bipartite pigeonhole bound).

The run recorded 4,811 and 27,597 nonempty faces; 2,363 and 13,518 matching pairs; critical cell vectors (one degree-zero cell, 84 or 560 degree-five cells); and 21,992 and 130,886 Hasse incidences checked acyclic. It does not verify an infinite-family conjecture, an integral equivariant basis, or the absence of equivalent unindexed work. Independent audit has not been performed.
