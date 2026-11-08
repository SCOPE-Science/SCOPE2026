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

# Verification record

The self-contained `verify_five.py` program, executed with Python 3, produced the exact JSON in `verify_five_output.json`, with `status` equal to `PASS`. The program tests all 983 integers in the interval \(18\le a\le1000\), recomputing their Apéry sets by shortest paths rather than using the closed form. It then identifies the complete pseudo-Frobenius spectrum from all generator conditions and compares it with the theorem, including the ten-class type vector. Ten values are additionally checked by direct integer reachability, without deriving membership from Apéry or coin lengths. A dynamic program checks the coin-length ten-shift identity through \(n=2399\). At \(a=17\), the exact pseudo-Frobenius set is \(\{33,39,42,48,49\}\), which excludes the formula's extraneous predicted value \(24\).

The proof in `RESULT.md` is the infinite-domain justification. The executable finite tests cannot establish correctness for all integers \(a\ge18\) by themselves, and the supplied review is not an independent scientific audit. Only Python's standard library is required.
