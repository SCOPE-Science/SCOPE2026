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

# Reproducible verification

The all-size proof derives the exact conditional binomial output distributions, mixed-triple sampling probability, total conditional variance, quadratic eigenfunction, and two-sided hitting-time survival bounds. These are algebraic steps valid for any population size divisible by three; finite enumeration is additional evidence, not an infinite verification certificate.

Run `python check.py` in the directory containing this file and `check.py`. The program enumerates all unordered partitions of the labeled population into triples and uses exact rational arithmetic for each possible one-step configuration and post-update binomial count at sizes 3, 6, and 9. It checks the stated conditional first and second moments and the global-complement one-step kernel, plus the deterministic density-map corner substitutions. The observed output was:

```
n=3: exact kernels, conditional means, variances, and heterozygosity checked for all 4 counts
n=6: exact kernels, conditional means, variances, and heterozygosity checked for all 7 counts
n=9: exact kernels, conditional means, variances, and heterozygosity checked for all 10 counts
PASS: exhaustive rational finite tests
```

The script depends only on the Python standard library. The finite tests do not address any other population size, alternative interaction mechanism, or near-corner parameter perturbation. No independent scientific audit has been performed.
