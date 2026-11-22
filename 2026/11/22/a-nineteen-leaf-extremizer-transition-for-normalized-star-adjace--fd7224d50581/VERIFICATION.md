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

# Reproducibility and verification

Execute `python3 check_normalized_star.py` with Python 3 from the extracted artifact directory. Reference output: `PASS 14202 supplementary checks`, followed by seven representative sharp constants and extremal ratios.

The code checks exact rational polynomial identities and the nineteen-leaf sign witness; the exact Jacobian against finite differences; randomly sampled Jacobian row sums under the global proposed bound; randomly sampled two-input global Lipschitz inequalities; and asymptotic sample values. The check uses fixed pseudorandom seed `230734` and only the Python standard library. Input conductances in tests are strictly positive.

The all-dimensional threshold, optimization and limiting constant are proved symbolically in RESULT.md; neither random testing nor finite enumeration proves the universal statements. The results concern a worst-case supremum and need not be achieved by a pair of distinct input vectors. No independent external mathematical audit has been performed.
