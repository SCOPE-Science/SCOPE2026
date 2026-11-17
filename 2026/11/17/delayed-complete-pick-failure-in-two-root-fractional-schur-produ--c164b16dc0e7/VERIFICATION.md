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

# Reproduction and verification

Unpack the single finding row, preserving the file names, then run `python CHECK.py` with a standard Python 3 installation. The checker requires no nonstandard packages. It independently computes exact rational Taylor coefficients using binomial convolution and a differential-equation recurrence, checks the signs through the reported first negative indices, and verifies the expected leading asymptotic trend for two small rational perturbations.

The actual packaged-source execution reported `PASS: 2551 exact coefficient/sign and scalar asymptotic checks`. Its first negative indices were \(403\) at \((a,b)=(1/2,1/100)\), \(1603\) at \((1/2,1/200)\), \(121\) at \((7/10,1/200)\), and \(3\) at the Hardy endpoint \((1,1/10)\).

Analytical checks independent of finite tests: the normalized kernel criterion, positivity of both factors, the exact two-singularity expansion with a uniform \(b\)-weighted remainder, the parity scaling profile, and lower and upper localization of the first negative coefficient are supplied in `RESULT.md`. Finite arithmetic does not establish eventual negativity, the uniform remainder, or the asymptotic first-index equivalent. An independent audit was not performed.
