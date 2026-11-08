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

The theorem follows from an exact finite residue-orbit identity modulo \(14\), a bound on the digit sum of a positive multiple of \(e\) below \(q^3\), and explicit three-digit witnesses for \(2e\). The only finite case distinction in the proof is the sequence of thirteen residue-orbit sums. The check does not substitute for the symbolic argument.

Run `python3 artifacts/verify.py` using Python's standard library. The checker calculates the full \(14\)-multiple base-digit spectrum and exact witness triples for all admissible \(t\leq800\), and independently finds shortest nonempty zero-sum returns by full-state breadth-first search for all admissible \(t\leq68\). The actual executed output was:

`VERIFY_OK residue_parameters=228 exhaustive_bfs_cases=20 complete_residue_states=1061940 exact_full14_spectrum=yes 3_witness_orbit=yes`

The breadth-first search explores every residue class reachable under additions by \(1,q,q^2\) and returns the first positive return to zero, so it is exact on the tested finite rings. The implementation uses no external datasets or libraries. Unbounded parameters require the mathematical proof; the checker alone does not establish them.
