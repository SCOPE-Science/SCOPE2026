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

The claim has an explicit all-parameter discrete-Morse proof in `RESULT.md`. It uses the sequential element-matching acyclicity lemma and the critical-face recurrence for path two-independence complexes. The independent-basepoint convention is handled by pairing the empty face with triangle vertex \(a\), or, equivalently, retaining \(a\) as the sole critical zero-cell in the ordinary face poset.

To replay the finite corroboration, run `python3 code/verify.py` from the package root and compare stdout byte-for-byte against `code/expected_output.txt` (UTF-8, LF). The program covers every \(n\) from three through sixteen; tests every admissible vertex subset rather than samples; reconstructs every Hasse cover; checks global matching acyclicity by a topological ordering; and validates that two matching implementations coincide. For the first eight lengths it also computes homology ranks directly from the mod-two simplicial chain complex. The full scope of the theorem is proved symbolically, not by extrapolating the tests.

The computation does not establish that no equivalent theorem has previously appeared, and there has been no independent mathematical audit.
