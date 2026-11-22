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

Run `python3 verify_gillis.py` using Python 3 and only the standard library.
The checker computes the exact discounted neighbor-hitting recurrence with a distant finite truncation, locates both threshold roots by bisection, checks the order for five outward-bias values, tests stationary ratios and the site-one stationarity equation, and compares the invariant-mass formula with independently iterated finite-window Markov kernels. It also compares against the unbiased exactly geometric stationary law.

Observed output: `PASS: 162 deterministic tests; exact identities and finite-kernel dynamics agree.`

As one representative parameter case, for an outward bias of negative one quarter the two computed boundaries are approximately 0.007403435880 and 0.030997297563. The complete proof of strict ordering, uniqueness, and existence of outer peaks does not rely on these decimals. The finite truncation and bisection code cannot certify infinite-dimensional theorems or exhaustive literature novelty.
