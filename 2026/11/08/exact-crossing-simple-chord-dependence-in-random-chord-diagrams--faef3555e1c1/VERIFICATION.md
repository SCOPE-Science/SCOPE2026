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

# Reproducibility

Run `python3 verify.py` in the extracted directory. The script uses only the Python standard library and does not fetch data. It enumerates every fixed-point-free matching on \(2n\) labelled cyclic endpoints for \(2\le n\le7\), independently computes the number of alternating chord pairs and adjacent endpoint pairs, and checks the exact coefficient-by-coefficient deletion identity with rational arithmetic. It also checks the crossing mean and variance, simple-chord mean and variance, cross-covariance, and exact squared correlation.

The recorded invocation returned:

```
VERIFY_OK 494 exact assertions; n=2..7 complete matchings
```

The finite checks do not prove the infinite family. The proof for all \(n\ge2\) is the specified-chord deletion bijection and cycle-edge matching count in `RESULT.md`. The Gaussian marginal theorem is taken from Flajolet–Noy (2000), with its normal-approximation refinement in Paguyo (2021). No independent audit has been performed.
