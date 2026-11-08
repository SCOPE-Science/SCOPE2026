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

# Verification and limits

`python verify.py` prints `PASS 14 literal host configurations; 65958 candidate strings; 136 independent dynamic configurations`.

The first test explicitly constructs each host word and checks, for every candidate within bounded ranges, whether it is absent and whether every one-letter deletion embeds. It compares that direct result with the local weak-descent characterization and the predicted longest length. The second test uses a finite-state dynamic recurrence indexed by the last two letters and weak-descent count, with a different search path from the literal matcher, to compare the longest length for all tested parameters.

The theorem for unbounded \(q\) and \(k\) rests on the mathematical proof in `RESULT.md`. The tests do not prove it, cover all cases, establish priority, or provide an independent scientific audit.
