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

# Reproducibility and limits

Run the included standalone `verify.py` with Python 3.10 or later. It implements exact rational correlation recurrences and directly counts ones in adjacent finite factors of the digit-parity sequence. It checks the exact local characterization for block lengths \(1\) through \(128\) at the first \(2048\) starting positions and compares frequencies at the first \(65536\) starts with the predicted rational limits to an explicit tolerance of \(1/1000\). It also checks the bounded correlation-extremizer implications through offset \(8192\).

Observed output:

```
VERIFY_OK local_and_density_tests=295046
first_16_densities=1/3,1/2,1/6,1/2,1/4,3/4,1/4,1/2,5/24,5/8,7/24,3/4,7/24,5/8,5/24,1/2
```

The checks reproduce the elementary identities on finite samples. They do not themselves prove convergence of natural densities, all-period bounds, completeness of extremizers, or novelty. Those infinite claims use the mathematical proof in `RESULT.md`; originality is supported by the stated source comparisons subject to their listed residual risks.
