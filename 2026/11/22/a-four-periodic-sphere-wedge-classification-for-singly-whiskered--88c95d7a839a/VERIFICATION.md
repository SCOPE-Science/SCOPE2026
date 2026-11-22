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
# Reproducible verification

Run `python3 verify.py` from this directory and compare its stdout byte-for-byte with `expected_output.json` (including its trailing line feed). This is a finite, exact standard-library computation, not an exhaustive proof for every \(n\).

The verifier enumerates all subsets of the \(n+1\) graph vertices for each \(n=3,\ldots,16\), filters by all forbidden connected three-vertex induced subgraphs, rechecks accepted faces via independent component-size searches, constructs all toggle matching pairs, checks their face-poset cover relations and ensures each nonempty face is paired once or critical. It then reverses matched Hasse covers and uses topological sorting to prove acyclicity for every tested instance. Expected critical dimensions are taken from the theorem and compared exactly. For arbitrary \(n\), the constructive proof's two independent path families and four-base recurrence establish the result.

Limitations: this program does not independently prove the all-parameter path reduction or database priority. No independent mathematical audit has been performed.
