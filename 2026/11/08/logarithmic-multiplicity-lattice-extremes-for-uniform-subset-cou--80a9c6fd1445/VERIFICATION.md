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

# Verification record

Run the included `verify.py` with standard Python 3:

```sh
python3 verify.py
```

The checker returned `PASS: 3326 finite exact and numerical assertions`. It enumerates all fixed-subset inclusion patterns in small universes, checks the one-type binomial recursion, checks nonpositive covariance of two under-collected types using exact rational arithmetic, and checks the entropy saddlepoint and tail ratios numerically at several growing sizes.

The infinite theorem is proved analytically in `RESULT.md`; the finite checks do not establish uniqueness of literature priority or any asymptotic limit. The statement assumes a positive limiting fraction of coupons per batch and multiplicity \(\lceil\alpha\log N\rceil\); no generalization to different growth regimes is verified. Independent review has not been performed.
