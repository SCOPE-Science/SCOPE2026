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

# Reproducibility

With Python 3 and no third-party packages, run `python3 checker.py`. The checker independently enumerates matching-swap target orders and breadth-first-searches all possible candidate supersequence prefixes (quotiented by target-progress vectors) for path sizes one through six. It validates 255 consecutive-edge overlap masks through size eight, all 1,930 corresponding total orders, the exact word lengths, and the Fibonacci order counts. Run output begins `VERIFY_OK`.

The general minimum-length statement rests on the explicit induction and projection proof in `RESULT.md`, not on finite enumeration. No computational independence or external certification is claimed. Historical priority comparisons are described in `REVIEW.md` and `AUDIT.json`; an independent audit has not occurred.
