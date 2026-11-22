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

The precise claim and proof appear in `RESULT.md`. The supplied `check.py` is standalone Python 3 and requires only the standard library. Run it from the directory containing the embedded files:

```sh
python3 check.py
```

The recorded output in `check_output.txt` is from that script. The checker generates all partial bijections explicitly for the labeled sets of sizes \(0,1,2,3,4\), generates every partial identity, compares the two compositions, and independently computes the right-hand finite coefficients. It also checks the elementary Laguerre-number recurrence against direct rank enumeration. All asserted finite identities in those cases passed. The largest case examines \(2^4\cdot209=3344\) pairs.

The program separately evaluates centered conditional second moments and ratios of the exact finite probability to its asymptotic equivalent at dimensions \(100,400,1600,6400\). Those numerical diagnostics support the stated constants but cannot establish convergence, tail control, or a central limit theorem. The infinite argument uses the published negative-argument Laguerre asymptotic and an explicit local quadratic expansion, with tightness inferred from the normalized limiting density; it does not rely on numerical experiments.

The historical finite centralizer decomposition is credited, not counted as a novel result. A complete prior-publication priority determination and independent mathematical audit have not been performed.
