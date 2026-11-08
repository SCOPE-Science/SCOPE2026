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

The rank-three classification is checked by the exact orbit/type recurrence implemented in `checker.py`. The source can be run with Python 3 standard library. The computation covers \(n=0,1,2,3,4,5,6,7,8\) without sampling; the independent direct-game check covers all ten pairs among \(n=0,1,2,3\).

The extension to arbitrary \(n\ge8\) is proved by a separate three-round threshold strategy on atom-Venn-cell sizes, not inferred from the finite computation. The finite certificate determines that \(n=6\) and \(n=7\) join the stable class. A direct list of characteristic distinguishing formulas was not supplied: the recurrence is a finite construction of them in principle.

External historical coverage and independent validation have not been completed. The relevant sections of the primary 2026 products-of-chains preprint and the closest published Boolean-algebra result were read as full text; broader historical priority remains unverified.
