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

The proof uses only elementary independent-arc sampling, local frame correspondence, a three-event union bound, a multinomial identity, and the Efron--Stein variance inequality. The standalone `checker.py` independently checks all loopless digraphs through four vertices, all valuation assignments in the McKinsey condition, and the exact binomial baseline. Its exact arithmetic test at four vertices with arc probability \(1/10\) obtains discrepancy probability \(14139187349/500000000000\), below the proved upper bound \(183/5000\).

Checks executed: `python3 checker.py`; terminal output includes `ALL_MODAL_ROOT_CHECKS_OK` and `EXACT_EXCEPTION_PROBABILITY`. Exhaustive four-vertex enumeration is finite only. The infinite probability and concentration claims depend on the mathematical proof. The comparison to earlier work is provisional, and no independent external audit has been performed.
