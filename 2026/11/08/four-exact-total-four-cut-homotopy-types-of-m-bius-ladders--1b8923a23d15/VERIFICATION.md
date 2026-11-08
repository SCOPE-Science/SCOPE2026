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
# Reproducibility and limits

Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier independently reconstructs the exact list of all independent four-sets and the entire face poset for each \(n\in\{6,7,8,9\}\), performs the deterministic dimension-sorted vertex-toggle matching, verifies every matched cover relation and every unmatched cell, and checks acyclicity using a topological sort of the complete reoriented Hasse graph. It separately calculates reduced simplicial boundary ranks over \(\mathbb F_2\).

The four expected independent-four-set counts are \(48,154,384,810\); the counts of critical cells beyond a single vertex are \(30,64,93,130\), concentrated in dimensions \(4,6,8,10\). The largest verification enumerates 254,369 nonempty faces and 2,255,346 Hasse incidences. The supplied `verification_output.txt` is the recorded stdout from the actual standalone verification execution and terminates with `ALL_VERIFY_OK`. Matching fingerprints in that output detect changes to the deterministic matching generation.

Acyclic Morse matching and critical-cell counts imply the integral wedge homotopy types by Forman's theorem. Reduced mod-two ranks alone would **not** prove the integral assertion; they are included solely as an independent consistency check. Only four finite width values were checked, so no unbounded family statement follows. There is no independent external validation.
