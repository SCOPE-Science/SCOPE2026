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
# Verification

The exact proof in RESULT.md treats every integer \(n\ge5\) and uses only finite-field linear algebra and Walsh orthogonality. The embedded standard-library checker `check.py` independently constructs every time-shift derivative, evaluates its polar rank by binary Gaussian elimination, and computes its complete Walsh transform for every shift and modulation at dimensions three through nine. It checks the rank, multiplicities, nonzero absolute values, Parseval, and condition number. Run `python3 check.py` from the extracted package. Expected final marker: `CUBIC_SYMMETRIC_GABOR_SPECTRUM_PASS`.

A separate direct complex projector-Gram numerical singular-value comparison was performed at dimensions three and four. At \(n=3\), its approximate singular groups were \(8\sqrt8\) once and \(4\sqrt8\) 28 times. At \(n=4\), they were \(64\) twice and \(32\) 56 times. This independently confirms the chosen unnormalized lifting convention; the exact standard-library checker does not require NumPy. Finite tests and numerical tolerances do not establish the theorem beyond their ranges. No independent external mathematical audit has been performed.
