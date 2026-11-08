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

The two attached Python 3 checkers use only the standard library. `verify_exhaustive.py` directly computes three synchronous updates, tests least temporal period three, and compares the mass distribution for every bounded state for \(k=1,2,3,4\). It checks 1,099,840 configurations, reproducing the formula at each mass. Every immediately primitive-three state is included in this bounded enumeration since each vertex waits at least once in the three-round orbit and thereafter cannot accumulate \(2\deg(v)\) chips.

`verify_patterns.py` independently enumerates all one- and two-firing phase words at each peripheral pair, solves the corresponding three-time firing inequalities, combines triangle contributions with a generating-function dictionary, and compares exact mass distributions for \(k=1,2,\ldots,12\). Both programs passed; their captured standard outputs are attached. The displayed verification is finite; the arbitrary-\(k\) proof is in `RESULT.md`.

Reproduce with `python verify_exhaustive.py` and `python verify_patterns.py`; neither command requires a network connection. Independent auditing remains unperformed.
