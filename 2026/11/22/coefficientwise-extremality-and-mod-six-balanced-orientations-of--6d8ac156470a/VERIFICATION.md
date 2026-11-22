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

# Reproduction and limits

Run `python3 CHECKER.py` with a stock Python 3 installation. The checker verifies the exact polynomial formulas and the complete minimizer/maximizer characterizations against every \(3\times b\) binary matrix for \(1\le b\le6\), and compares direct admissible ternary type assignments with the separate rectangle method for \(1\le b\le3\). The saved `CHECKER_OUTPUT.txt` is the output observed from the included script, not an independent certificate.

The infinite coefficientwise extremality and the mod-six classification rely on the proof in `RESULT.md`, especially discrete convexity and equality conditions. The checker does not resolve the historical originality question. Independent mathematical audit has not been performed.
