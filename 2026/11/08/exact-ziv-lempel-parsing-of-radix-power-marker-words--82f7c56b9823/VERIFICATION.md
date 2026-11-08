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

# Reproduction and verification

Run `python3 check.py` using Python 3.10+. The program generates the binary word directly from the integer-power marker positions and computes the first new factor length from its literal definition, including possible overlapping earlier occurrences. It checks every proposed complete phrase against the longest repeated proper prefix and independently tests novelty using explicit comparisons over all earlier starts.

Observed output: for bases 2 through 12, respectively, 13, 17, 13, 11, 11, 9, 9, 9, 9, 7, 7 consecutive complete phrases were tested. Total: 115 exact phrase lengths with both previous-occurrence and uniqueness tests. No discrepancies arose. Each checked phrase ends at or before position 12,000. The theorem for all levels follows from the proof in RESULT.md, not the finite tests. No independent audit was performed.
