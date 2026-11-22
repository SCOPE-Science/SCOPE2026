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

# Exact computation checks

Extract `CHECKER.py` and `CHORD_SPECTRUM.csv` into the same directory and run `python CHECKER.py` with Python 3; this is a full exact finite enumeration, not a floating-point test. The checker builds 120 collision-order vectors, finds 108 distinct vectors with coordinate sum 27, tallies all 5778 unordered pairs, verifies every one of 174 squared-distance frequencies against CSV, and classifies four diameter pairs as two three-vertex paths and 102 isolated vertices. A separate implementation using a union-find scheme agreed on the complete vertex set.

The completeness step relies on the proven normal-fan refinement/vertex-coordinate correspondence in the cited Bottman–Poliakova paper, rather than assuming that a finite sample of vertices must be exhaustive. The separate 108-vertex census in Chapoton–Pilaud Table 10 agrees. No statement about arbitrary affine realizations or higher dimensions is verified.
