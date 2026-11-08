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

Run `python verify.py` with Python 3 and no external packages. Recorded output is `verification_output.txt`. The program enumerates every unrooted tree with 0 through 8 internal vertices (the zero case is the two-vertex tree), expands every maximum-degree-three internal tree, checks degree incidence, recovers the tree, decomposes biconnected blocks, and directly compares all paired joint refinement profiles. It finds exactly 1,1,1,1,2,2,4,6,11 types at consecutive admissible sizes. It also verifies explicit nonisomorphic equivalent pairs for internal sizes 4 through 29. `witness_edges.txt` gives both 40-vertex examples.

The symbolic proof verifies the unrestricted classification, not just the computed instances. The finite program is corroborative and does not establish historical priority or supply an independent external audit.
