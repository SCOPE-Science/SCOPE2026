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

# Reproducibility and scientific limits

Run `python verify.py` and `python construct.py` with Python 3.9 or later. Both programs use the standard library only. `verify.py` exhaustively enumerates the constrained arcs for \(2\le n\le12\), checks the potential differences and degree balance, constructs the exact required cyclic word via an Eulerian traversal, and compares its full window multiset with the specified multiplicities. `construct.py` independently builds Eulerian tours and brute-forces all shorter cyclic binary words for \(2\le n\le5\) to check minimality in those ranges.

Expected terminal markers: `VERIFY_OK` and `CONSTRUCT_OK`.

A separate minimum-cost flow cross-check gave exact extra-edge counts \(0,1,2,4,7,12,20,33,54\) for \(2\le n\le10\), corresponding to the Fibonacci prediction. This external cross-check is not a package dependency.

Finite runs do not constitute an infinite proof. The general proof consists of an all-length potential lower bound plus an explicit balanced augmentation and Eulerian circuit. There is no independent mathematical audit; historical-priority limitations are noted in `RESULT.md` and `REVIEW.md`.
