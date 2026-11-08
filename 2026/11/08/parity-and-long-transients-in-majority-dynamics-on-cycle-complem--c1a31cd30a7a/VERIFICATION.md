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

Analytic proof: cyclic-run counting for every odd \(N\ge7\) and an induction on explicitly described balanced words for every even \(N=2m\ge8\). Neither argument requires a finite enumeration.

`check_exhaustive.cpp` was compiled with `g++ -std=c++17 -O3` and run from its extracted source; its direct adjacency-vote enumerator exhaustively checks odd \(N=7,9,\ldots,19\) and the even witness through \(N=20\). The exact output is included as `check_exhaustive.out`.

`check_symbolic.py` was executed with Python 3. It checks the complete stated even trajectory for \(4\le m\le40\) and the odd run identity for odd \(7\le N\le15\). Exact stdout is included as `check_symbolic.out`. The truncated earlier exploratory checks were not relied upon.

Scientific limits: finite computations are not an all-order certificate; no even-order universal sharp stabilization bound is claimed; historical novelty is subject to the literature-overlap qualifications in `REVIEW.md`.
