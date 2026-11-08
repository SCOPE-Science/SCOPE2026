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

The standalone `verify_biclique.py` executes with Python 3 only. It enumerates every mapping of each individually labeled chore to one of the agents or to the unallocated category, checks same-bundle conflict edges directly, tests unit-cost chore EF1 by maximum-minus-minimum bundle size, and tests insertion maximality for every unallocated chore and every agent. It compares exact counts of complete and incomplete allocations and largest allocated cardinality to the formulas in `RESULT.md`.

Command: `python3 verify_biclique.py`.

Observed success: 63 complete parameter cells; 726261 entire labeled assignment states; two larger formula-only examples and 67 further parameter values in the sharpness family. These experiments do not establish the general theorem; the symbolic proof in `RESULT.md` does. The computation uses no third-party packages. No independent external audit or validation has been performed.
