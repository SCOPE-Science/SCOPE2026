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

Run `python3 verify.py` with a standard Python 3 interpreter. No external packages, datasets or network resources are required. The script enumerates all multisets of nonempty ballots for \(n=1,2,3,4,5,6,7\) and all present-ballot deletions, explores every seqPAV tie branch, compares the before/after committee sets by Kelly's exact strict criterion, and asserts the precise profile count and one candidate-permutation orbit.

Expected output profile totals are \(15,120,680,3060,11628,38760,116280\); paradox totals are \(0,0,0,0,0,0,12\). The check handles 170543 complete anonymous profiles and 813960 distinct ballot-type deletions. Independent exact rational scores agree in 5075 selected cases. The displayed seven-voter witness has before-set \(\{abc,abd,acd\}\) and after-set \(\{abc\}\) when one \(ab\) or \(ac\) ballot abstains. The program terminates with `PASS` if and only if its assertions succeed.

The exhaustive enumeration is finite and not a theorem about arbitrary electorate sizes or arbitrary numbers of candidates. The independent rational implementation checks only a subset; its role is cross-implementation corroboration, whereas completeness follows from the exact all-multiset/all-deletion loops and the integer greedy recurrence. The result is inherently set-valued and tied; no tie-breaking-independent phenomenon is claimed. Literature-priority uncertainty remains. No independent audit has been performed.
