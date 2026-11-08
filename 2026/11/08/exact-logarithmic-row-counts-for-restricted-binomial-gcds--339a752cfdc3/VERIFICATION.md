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

The symbolic proof gives the all-parameter theorem. Reproduce finite checks with `python3 verify.py` using Python 3.9 or newer and no nonstandard dependencies. The program calculates digitwise Lucas nondivisibility, an independent minimal-zero-sum criterion, complete small-order zero-sum word enumeration, exact finite-profile sums and direct row counts, and selected larger sparse exact counts. It does not prove all \(L\) or replace the proof. No outside certificate or independent audit was used.

Observed results:

```
DIRECT_LUCAS_VS_MINIMAL_ZERO_SUM 11866
MAXIMAL_LENGTH_CYCLIC_WORDS 763424
COUNT 3 2 8 44 leading 21.33333
COUNT 3 2 10 75 leading 41.66667
COUNT 3 2 12 118 leading 72.0
COUNT 3 2 14 175 leading 114.33333
COUNT 3 2 16 248 leading 170.66667
COUNT 4 3 6 47 leading 6.75
COUNT 4 3 8 104 leading 21.33333
COUNT 4 3 10 200 leading 52.08333
COUNT 4 3 12 349 leading 108.0
COUNT 5 2 8 36 leading 1.06667
COUNT 5 2 12 121 leading 8.1
COUNT 5 2 16 311 leading 34.13333
COUNT 5 2 20 678 leading 104.16667
VERIFY_OK finite_checks_only=True
EXACT_PROFILE_REPLAY 3 2 2 L=2..10
EXACT_PROFILE_REPLAY 4 3 2 L=2..10
EXACT_PROFILE_REPLAY 5 2 4 L=2..10
EXACT_PROFILE_REPLAY 5 3 4 L=2..10
EXACT_PROFILE_REPLAY 7 2 3 L=2..10
ALL_EXACT_PROFILE_TESTS_OK
ORDER_FOUR_BRANCH_POLYNOMIAL_CERTIFICATE_OK six_points_per_branch=True
```

The comparisons of observed counts with main-term approximations show visible lower-degree corrections at modest cutoffs, as expected; this is not evidence of a failure of the asymptotic. The exact finite-profile comparisons, not the approximations, are required to agree identically.
