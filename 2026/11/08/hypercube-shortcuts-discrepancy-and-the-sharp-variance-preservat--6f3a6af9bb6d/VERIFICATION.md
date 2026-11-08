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

# Reproducible verification and limits

Execute `python check_hypercube_chord.py` with Python 3.8 or later. The checker uses only the standard library (`fractions`, `itertools`). Expected final marker:

```
ALL_HYPERCUBE_CHORD_PRESERVATION_CHECKS_OK
```

Actual replay checked all anchored integer Lipschitz functions on Boolean cubes of dimension 1, 2 and 3 (respectively 3, 19 and 495 assignments), then checked the three-dimensional case with an added full diagonal (457 assignments) and verified sharp variance \(3/4\). It also checked every possible single-chord support through dimension 8, 21 distinct point pairs across the seven Fano lines, absence of a valid Fano two-coloring, complete-triple-system examples, and the exact Fourier deficit identity for a test function. These are finite sanity checks. The universal upper and equality bounds, the quantitative gap, and NP-completeness are established by the written proof and external classical NP-completeness theorem; they are not certified by enumeration.

This document reports no independent mathematical audit.
