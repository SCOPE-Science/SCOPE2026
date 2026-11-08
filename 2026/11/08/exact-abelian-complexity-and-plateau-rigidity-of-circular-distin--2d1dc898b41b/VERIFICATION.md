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

# Reproducible checks

Run `python verification/check.py` with Python 3. The script independently builds cyclic run words, enumerates all phase Parikh vectors and compares them with the stated closed formula. It also checks symmetry, concavity, exact peak value and exact maximizing residue set. The sample ranges exhaust all positive run-length choices in \(q=3\) with lengths at most \(6\), \(q=4\) at most \(5\), \(q=5\) at most \(4\) and \(q=6\) at most \(3\), plus 750 deterministically seeded larger profiles up to \(q=8\). All 3344 profiles passed.

The general result does not follow from finite enumeration; the complete argument is the rigidity and phase-transition proof in RESULT.md. No independent scientific validation has been performed.
