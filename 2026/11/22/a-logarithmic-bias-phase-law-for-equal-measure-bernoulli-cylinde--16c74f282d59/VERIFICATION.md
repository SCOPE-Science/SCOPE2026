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

# Verification and reproducibility

Run `python3 CHECK.py` in the directory containing this file. It requires only the Python 3 standard library. Direct prefix-automaton dynamic programming is compared coefficient by coefficient, in exact rational arithmetic, with an independently assembled self-overlap generating function. The checker also tests each explicit overlap coefficient, the algebraic threshold bracket, and the strict reversal of Perron-root order on either side of the threshold.

Expected output includes `PASS exact survival coefficients: 1848` and `PASS explicit overlap and crossover checks: 630`. It prints approximate threshold values for selected lengths. The displayed numerical threshold for \(k=2\) checks the previously documented example rather than claiming its discovery. All finite checks are diagnostic and do not replace the proof of the infinite statement. The analytic uniqueness and asymptotic arguments appear in `RESULT.md`.

No third-party article text is included in this package. The status in the front matter refers only to the independent-audit channel, which has not been performed.
