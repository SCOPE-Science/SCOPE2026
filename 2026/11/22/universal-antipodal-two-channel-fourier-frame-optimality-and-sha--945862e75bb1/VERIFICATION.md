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

The proof in `RESULT.md` supplies the quantified conclusion; the accompanying `CHECK.py` provides supplementary numerical finite-size tests and is not a substitute for the proof. It requires Python 3 and NumPy, and can be executed in the same directory with `python CHECK.py`.

The checker was run from the complete saved source and returned `CHECK_OK assertions=161085`. It tests exact matrix/spectrum agreement, weighted bounds and the heat profile over finite examples, but does not exhaust all cycle sizes, times or windows. No independent mathematical audit has been performed.
