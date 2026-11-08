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

# Verification of the terminal coverage theorem

Use Python 3 with only its standard library and execute `python3 CHECK.py`. The program independently forms projective incidences over prime fields of orders 2, 3, and 5, tests pair uniqueness and all fixed subsets of size at most four, checks pairwise avoidance covariance, verifies the multitime product by direct enumeration for small finite examples, and independently recovers the exact Fano-plane mean cover time \(163/30\).

The infinite-order conclusions depend on the analytic estimates in RESULT.md: a uniform \(O_r(q^{-2})\) one-round log-survival error, accumulation over \(O(q\log q)\) rounds, mixed factorial moment convergence, and uniform integrability from pairwise negative covariance. No finite computation proves the limit itself. The checker is not a proof assistant, external audit, or a substitute for the written proof.

The 1996/1997 general random-covering reference remained accessible only by abstract and is a residual historical-priority risk. Scientific findings have undergone self-review; independent audit was not performed.
