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

# Reproduction and limits

Run `python3 verify_pfaffian_fibers.py` in the directory containing the two verification artifacts. It uses standard Python only. Its stdout should match `pfaffian_output.txt` exactly, ending with `PFAFFIAN_PENCIL_COMPLETE_BRACKET_FIBERS_PASS`.

For each of eleven explicit field/pencil configurations, the program enumerates every pair of vectors in the four-dimensional quotient, computes its original alternating bracket, and tabulates all targets. Separately it row-reduces each nonzero alternating form in the pencil and determines the singular projective lines. It then checks the target-specific prediction without invoking the proof's character sums. Prime fields of orders two, three, and five are tested, with all possible binary-Pfaffian root profiles represented. The total original pairs are \(q^8\) per configuration; full Lie-algebra counts acquire the factor \(q^4\) from the central coordinates.

The computation does not enumerate all pencils in a given field or all finite fields. The all-field result follows from the fully stated character-sum proof, not from these tests. No independent mathematical audit is claimed.
