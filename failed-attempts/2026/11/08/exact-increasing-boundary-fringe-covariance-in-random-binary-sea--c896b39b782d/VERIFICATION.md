---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Root split K is uniform in {0,...,n-1}, L_n=1+L_K for n>=1 and Z_n=Z_K+Z_(n-1-K) for n>=2, with exceptional b_0=0 and b_1=1. The four boundary corrections to b_k=(k+1)/3 produce conditional covariance (n-2)/(3n(n-1)); total-covariance recursion gives v_3=1/18 and v_n-v_(n-1)=1/[3n(n-1)(n-2)] for n>=4, yielding the stated rational formula and limits. Independent exact enumeration of all n! priority permutations for 2<=n<=7 reproduced all covariances, including base n=2 and n=3. Variance normalization uses record-count variance H_n-H_n^(2) and fringe leaf variance 2(n+1)/45 for n>=4. A finite check is not the all-n proof.

## originality

FAIL

FAIL: The October 12 2026 published Resultary theorem already gives the IDENTICAL covariance, increment, boundary mechanism and correlation asymptotic for the root-to-maximum right spine. Reflection of ordered keys sends its rightmost path to this leftmost path without altering leaf counts or the uniform tree law. The November 2 2026 published theorem additionally gives exactly this minimum-key depth/leaf covariance, and node-count path length differs from depth by the additive constant 1. Thus the entire final result, not merely its numerical value, is covered.

## value

FAIL

FAIL: The submitted exact identity is mathematically natural but not a distinct unknown fact: reflection of the published maximum-key spine theorem or the published minimum-key depth theorem yields it unchanged. Re-presenting the same boundary-root recursion and increasing-to-1/12 behavior adds no motivated surviving mathematical information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
