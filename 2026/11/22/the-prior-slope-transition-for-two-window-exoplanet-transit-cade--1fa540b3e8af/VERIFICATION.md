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

# Reproduction and limitations

The mathematical derivation is given in `RESULT.md`: (i) two uniform-phase windows yield the triangular phase-overlap probability normalized by orbital period, (ii) differentiation yields two nonnegative side integrals, (iii) strictly monotone reweighted period priors make that derivative sign-definite in the central region and strictly decreasing on the appropriate edge, and (iv) two elementary equations yield the closed forms. Critical conditions are \(a+2w\le b\) and \(b+2w<2a\), which prevent the second-orbit alias within the explicitly allowed lag range.

The accompanying `CHECK.py` runs with Python 3 standard-library only, verifies 55,922 finite diagnostic conditions over several sizes and prior exponents, checks the exact explicit roots and the neutral-prior plateau. It prints illustrative optimal lags 3.188194301613 and 3.809987531153 for \(a=3,b=4,w=0.2\). The experiment is not an exhaustive numerical certification of continuous inputs; general validity comes from the displayed proof. No external independent audit or empirical instrument calibration has been performed.
