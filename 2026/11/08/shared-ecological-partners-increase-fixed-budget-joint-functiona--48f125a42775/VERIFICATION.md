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

# Reproduction and scope

Run `python3 verify.py` from this directory with Python 3. No third-party libraries or external data are required. The checker enumerates **every** size-\(k\) survivor subset for all \(2\le n\le9\), all legal partner-set sizes, overlaps and quorums. For each adjacent overlap comparison it computes the two empirical joint-count distributions by direct set enumeration and compares their joint quorum-survival count difference with the algebraic binomial formula. Its reported output is:

```
parameters 2838 threshold identities 45078 strict identities 6270
OR covariance c 0 : -16 / 1225
OR covariance c 1 : -16 / 1225
OR covariance c 2 : 19 / 1225
OR covariance c 3 : 124 / 1225
```

The code asserts equality of the direct-enumeration difference and the symbolic increment for all 45,078 instances; no probabilities are approximated or simulated. The checker also asserts the seven-species covariance numerators exactly. The machine computation is finite and does **not** certify the all-parameter theorem. That conclusion follows from the exchange-of-one-exclusive-partner proof and the nonnegative four-cell mixed differences in `RESULT.md`. The analysis relies on uniform fixed-size survival; no claim is made for other sampling designs or observed ecosystems.
