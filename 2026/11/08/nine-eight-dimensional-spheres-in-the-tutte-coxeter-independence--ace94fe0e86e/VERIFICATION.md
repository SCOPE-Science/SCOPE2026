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

Run `python3 verify.py` with Python 3. The checker generates the specified duad–syntheme graph, confirms degree three and girth eight, enumerates every independent face, checks the independent binomial count, constructs an exact vertex-toggle matching, orients every Hasse incidence, and exhaustively topologically sorts the directed face-poset graph. The output `verification_output.txt` is a record of the checker run. The finite proof applies only to the explicitly defined 30-vertex graph; numerical invariants, matching counts and entire acyclicity are checked from the provided standalone file. The formal deduction to the sphere wedge uses the standard discrete-Morse CW theorem and the absence of cells in intermediate dimensions.
