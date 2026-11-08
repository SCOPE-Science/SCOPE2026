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

# Reproduction and limitations

Execute `python3 verify_cyclic_three_runs.py` using Python 3 with no external dependencies. The script directly enumerates every rotation of every prefix and every possible start of a factor, constructs the full covered-position bitmask, counts distinct actual factor strings, and checks all equal-size block factorizations. It then compares the outputs to the stated closed-form spectra for every \(1\le a,b,c\le10\), plus 250 seeded random larger triples with each parameter between 1 and 25. The run passed 1,250 triples and 26,029 candidate-length tests. This also exercises boundary parameters outside the theorem's required \(b\ge2\) range; the known \(b=1\) cases are not part of the new claim.

Independent audit: not performed. These finite tests cannot establish an unrestricted theorem or comprehensive bibliographic novelty; the unrestricted mathematical justification is the proof in `RESULT.md`. The source for the single-middle-letter special case and all general algorithmic results is credited. The publication-priority assessment is limited to the sources actually inspected.
