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

# Verification

The direct proof uses the greedy-arch characterization, a recurrence for the indexed runs in which arches end, and an exact comparison with the factor's right endpoint. The calculations are symbolic and apply for every permitted alphabet size, positive run lengths, positive repetition count and cyclic phase.

`verify.py` is independent of the proof's endpoint recurrence: it scans the actual repeated word and counts greedy arches. It tests phase-level values and maximizing-phase multiplicities for \(q\in\{3,4,5,6\}\), run lengths from \(1\) to \(4\) or \(3\), and repetitions through \(9\), \(8\) or \(7\) as specified in the code. A second test enumerates all shorter candidate subsequence words directly to independently check the arch-count characterization on smaller examples.

Run `python3 verify.py` from the folder containing this file and the script. The recorded result was: `PASS 9671 parameter/repetition cases; 105476 phase-index comparisons; 678 direct full-spectrum cross-checks`.

Limits: no finite verification is an exhaustive check of the unbounded domain; no independent mathematical audit or independent publication-priority certification has been performed.
