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

# Reproduction

The standalone `checker.py` requires Python 3 and uses only the standard library. From the extracted package directory, run `python3 checker.py` and check for `VERIFY_OK 867`. The checker derives the conditional sampling distribution by finite binomial sums with exact rational arithmetic, covering \(2\le m\le12\), every admissible odd \(h\), and odd \(s\) up to eleven. It also checks \(m=5,h=s=3\), plus illustrative asymptotic cases.

The proof in `RESULT.md` independently covers every allowed integer dimension, every positive iteration, all fixed quantile fractions in \((0,1)\), and the claimed binomial rate through the law of large numbers and Stirling's formula. The finite tests are necessary consistency checks but are not an independent certification or an exhaustive computation of the infinite family. A genuinely independent mathematical audit has not occurred.
