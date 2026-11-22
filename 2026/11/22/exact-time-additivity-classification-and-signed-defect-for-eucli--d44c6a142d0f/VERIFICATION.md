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

Run `python3 CHECK.py` with a Python 3 standard-library interpreter. On the packaged source this prints `PASS 6360 checks, including all three positive semigroup cases and nonzero signed second-order defects`.

The script tests exact \(p=1,2,\infty\) composition formulas for seeded random data and checks the signs, proximal stationarity residuals, and small-\(h\) convergence to the stated signed coefficient for selected finite \(p\) and \(n\). It supplies finite computational diagnostics only. The analytic proof in `RESULT.md` is necessary for the universal all-parameter theorem; no test list is exhaustive. Historical novelty, publication priority and independent audit are not computationally certified.
