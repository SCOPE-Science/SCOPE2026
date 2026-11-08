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

# Mathematical verification and reproducibility

Run `python3 verify_two_marks.py` using Python 3 and its standard library only. The observed output from the actual embedded script was:

`EXACT_TWO_MARKS_OK 3600 parameter pairs; all half-length type sets`

The checker loops over every pair \(0\le p,q<60\). For each word \(a^pba^qb\), it directly enumerates cyclic windows of each even length not exceeding the word length, counts \(b\) independently in the two halves, and records the exact set of equivalence types \((m,\text{number of }b\text{ in one half})\). It compares those sets to the two explicit indicators, verifies the closed total, and checks every odd-length partial-sum lower bound. These are finite regression checks; the unrestricted all-parameter theorem follows from the constructive argument in `RESULT.md`.

The two critical unbounded steps are: (i) there cannot be any type having two marked letters in each half because the whole circular word contains only two, and (ii) an oriented pair of marks separated by \(s\) can be placed into opposite halves of a factor of length \(2m\) if and only if \(s\le2m-1\), with the placement given explicitly in the proof. The self-review passed. No independent mathematical audit or external certification was performed.
