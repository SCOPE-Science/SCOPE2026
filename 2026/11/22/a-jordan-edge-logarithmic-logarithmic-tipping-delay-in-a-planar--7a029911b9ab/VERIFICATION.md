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

The exact-recurrence and Jordan-factor derivations are in `RESULT.md`. From the directory containing the files, run `python3 CHECKER.py` with the standard Python 3 library. The checker iterates the exact planar map with rational arithmetic at \(lpha=1/4\), \(\delta=4/25\) and \(\delta=1/4\), and \(\mu=10^{-5},10^{-10},10^{-20},10^{-40}\). It confirms the first border crossing, one-sided monotone flight, all evaluated recurrence identities, the exact critical Jordan solution and bounded differences from the two-term clocks. Eight tests completed successfully.

These tests are finite diagnostics; they cannot establish all-parameter estimates or novelty. The analytical proof in `RESULT.md` establishes the quantitative limits. Literature priority has not been independently verified.
