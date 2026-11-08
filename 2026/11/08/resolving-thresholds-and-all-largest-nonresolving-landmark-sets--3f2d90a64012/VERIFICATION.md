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

# Verification of mixed-Hamming resolving thresholds

Run `python3 verify.py` from the directory containing this report and the included standalone Python file. The program constructs vertex tuples and distance tables independently of the symbolic proof. It enumerates bisectors of every vertex pair, determines the maximum bisector cardinality, counts distinct maximum sets, and tests the allowed pair-support patterns. For graph order at most twelve it also tests every vertex subset of critical cardinality directly for failure to resolve.

The completed finite run returned `VERIFY_OK 61 profiles 82284 distinct_vertex_pairs full_bisector_enumeration=PASS critical_nonresolving_set_count=PASS pair_support_classification=PASS`. This is finite corroboration only; the proof for arbitrary numbers of coordinates and alphabet sizes is in `RESULT.md`.

There is no independent mathematical audit or external certification. Publication priority remains subject to literature comparison beyond the sources cited.
