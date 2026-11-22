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

Run `python3 evidence/verify.py` with a standard Python 3 interpreter. The program verifies all \(512\) vertex subsets; both cut-complex and Alexander-dual constructions; the legality of each of \(69\) explicitly prescribed free-face collapses; and the complete integral Smith forms of the collapsed boundary maps using only unit row and column operations. The exact result is also cross-checked by independent mod-two ranks for the original ordinary cut complex. A full matching execution transcript is embedded at `evidence/verification_output.txt`.

The finite certificate is exhaustive for this nine-vertex graph. It does not prove claims about other rook-graph sizes or identify the homotopy type of the original four-cut complex. The elementary topological steps used to upgrade the integral data for the dual are written in RESULT.md. External independent audit has not been performed.
