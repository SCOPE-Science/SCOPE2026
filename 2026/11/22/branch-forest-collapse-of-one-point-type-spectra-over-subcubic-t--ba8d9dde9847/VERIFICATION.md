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

Run `python3 verify.py` with the two files in the same directory. No third-party Python packages are required. The checker directly evaluates admissible neighborhoods by testing triangles in the line graph, independently evaluates the symbolic inclusion–exclusion sum, and exhaustively classifies the subcubic tree cases through six vertices by Prüfer codes and center-rooted canonical forms. It also checks coefficient recovery, larger random trees with a fixed seed, and an explicit infinite pair construction at the first 25 eligible orders. See `verification_output.txt` for the observed deterministic output.

The exhaustive statement is limited to trees of order at most six. Random samples and the finite spider checks are not proofs for arbitrarily large trees. The infinite theorem follows from the exact inclusion–exclusion proof, and uniqueness at the first failing order follows from the explicit four-form tree classification.
