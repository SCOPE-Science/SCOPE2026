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

The `check.py` file uses Python's standard library and may be executed using `python check.py`. It generates all set partitions with at most eight labels and checks the Bell counts, expected numbers of fixed-size blocks with prescribed minimum range, and two-count mixed/factorial moments by independent candidate-set enumeration. The performed run reported 520 exact assertions passing for sizes two through eight.

The infinite statements use Dobiński's Bell-number formula, a fixed-order saddlepoint ratio, precise candidate-set counts and a mixed factorial-moment argument. The checker cannot establish vague convergence or historical originality. The independent audit has not been performed.
