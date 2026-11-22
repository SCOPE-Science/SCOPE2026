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

The all-length theorem is established in the proof by (i) a complete local legal-swap criterion including boundary cases, (ii) forced two-template classification, (iii) explicit path adjacency with no other edges, and (iv) Eulerian enumeration. `checker.py` is a standalone standard-library diagnostic, not an infinite proof. It enumerates every one-descent permutation for lengths three through nine and compares exact edge sets, component sizes, degrees, and counts. Complete internal path distances by BFS are checked for every ordered pair at lengths three through eight. For length two the unique one-descent state is isolated.

Reproduction command: `python3 checker.py` in the directory containing this document and the source file. No external assets or libraries are required. An earlier result under another terminology is not excluded by searchable literature.
