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

Run with a local Python 3 interpreter from the directory containing these files:

```
python check_factors.py
python check_contexts.py
```

Observed outputs:

```
PASS direct finite factor-set checks: 11747 cases
PASS independent context checks: 4567 cases
```

The first program enumerates all contiguous substrings and minimal absent words using prefix/suffix membership; its exhaustive parameter ranges are binary primitive periods through length eight, ternary through length five, and four-letter through length four. It checks every prefix length from \(\max\{1,2d-2\}\) through \(3d+2\). The second program uses a different left/right-context construction: exhaustive binary periods through length seven, ternary through four, four-letter through three, and 500 reproducibly seeded random cases, with length varying beyond full-period boundaries. Both implementations independently compute periodic forbidden components and endpoint obstructions. The discrepancy tests assert exact **set** equality, not only counts.

These are finite tests. The universal result is justified by the proof using the phase-distinguishing rotation lemma, the length-\(d\) boundary case, and uniqueness of all longer phase extensions. Program execution does not constitute independent mathematical audit or publication priority certification.
