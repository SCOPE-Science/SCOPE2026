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

# Verification and reproducibility

Run `python3 verify.py` in the directory containing this document. No third-party packages, network services or external files are required. `verification_output.txt` records the exact output of the included program.

The program constructs every original open-neighborhood face from all prism vertex neighborhoods, independently constructs the categorical double-cover graph faces, enumerates the proposed pair list and checks every elementary free-face precondition at the moment of removal. It compares the complete residue face-by-face and checks the symbolic pair count against degree counts. All 613 labeled square-free graphs of orders one through five are covered exhaustively. Named higher-order cases include cycles of lengths 5 and 7, a six-vertex star and the Petersen graph.

The failure of the hypothesis is illustrated, not used as a universal converse: the four-cycle base gives a cube whose ordinary open-neighborhood complex has two tetrahedral boundaries, rather than two four-cycles.

The all-graph assertion is proved in RESULT.md by unique ownership of horizontal faces and a decreasing-size collapse sequence; finite tests cannot establish its universal quantifier. No independently performed mathematical audit is asserted.
