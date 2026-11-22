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

The self-contained `checker.py` enumerates all ordered read sequences with exact rational arithmetic for 1,771 positive rational compositions. Run `python checker.py` from this directory. Expected outcome: a printed `PASS` marker with the number of rational community cases.

The analytical proof in `RESULT.md` covers all positive real \(a,b,c\) summing to one, establishes the \(1/3\) threshold, proves strict marginal comparisons, and supplies a high-depth bound. The code cannot replace that continuum proof. The model is an idealized read-label experiment, with no biological sample validation or independent external mathematical audit.
