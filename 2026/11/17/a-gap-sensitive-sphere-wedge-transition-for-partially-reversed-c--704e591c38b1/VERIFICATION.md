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

# Verification of the homotopy classification

`VERIFY_PARTIAL.py` uses the standard-library only, recreates the complete semisimplicial face sets for all nonempty proper and full reverse-subset choices for \(3\le n\le7\) (243 subsets total), checks their one-dimensional common intersection and gap-counted edge sets, and calculates modular chain ranks over \(\mathbb F_{101}\). It passes every case; details in `VERIFY_PARTIAL_OUTPUT.txt`.

`VERIFY.py` checks the written optimal forward-orientation matching on every face and every directed Hasse cover for \(2\le n\le11\), verifies acyclicity by topological sorting, checks the exact two critical cells and integer winding cocycle. Details in `VERIFY_OUTPUT.txt`. No computation over finite dimensions proves the all-parameter theorem; that proof is given in `RESULT.md`. Integral freeness and the homotopy decomposition follow from the all-parameter graph and winding proof rather than from modular ranks alone.

Only self-review were performed. Independent audit is not performed.
