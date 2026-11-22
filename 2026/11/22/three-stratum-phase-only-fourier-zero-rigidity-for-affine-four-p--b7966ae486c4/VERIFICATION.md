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

# Mathematical verification

The Fourier reduction is exact because the three support differences are independent; the kernel of the dual restriction map has size \(p^{d-3}\). The four-unit cancellation lemma follows by the even self-inversive root polynomial. Pair equations are independent for disjoint matching edges. Simultaneous feasibility of all three is impossible since \(\mu_p\cap(-\mu_p)=\varnothing\) for odd \(p\). Two feasible matching lines have exactly one joint point.

`artifacts/verify.py` uses only Python 3 standard libraries. Direct exact computation in a cyclotomic Gaussian-integer basis yielded `FINITE_CYCLOTOMIC_CHECKS_PASS 5271`. The checker tests small primes and a finite coefficient alphabet; it does not prove the quantified all-prime theorem, which follows from the analytic argument.

No test for unequal coefficient magnitudes, composite moduli, other affine ranks or an independently assessed proof is claimed.
