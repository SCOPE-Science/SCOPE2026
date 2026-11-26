---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a uniformly chosen forced r-subset let m=n−r be the number of unforced positions. Two unforced endpoints contribute half their probability at each edge. For an ordinary consecutive pair (i,i+1), the cases with exactly one forced position combine to r(m−1)/[n(n−1)]: conditional on an unforced image differing from its own position, the eligible lower and upper ranks in the two orientations sum to (i−1)+(n−i−1)=n−2. Two forced endpoints make no ordinary descent. For the wrap comparison any forced endpoint gives a descent; otherwise its probability is 1/2. Thus the summed mean when r<n is n/2−r(r−1)/[2(n−1)] (r=n−1 gives the identity directly), and for r=n the actual mean is 1. Multiplying by the factorial moment, which has expectation 1, gives the claimed covariances. Fixed-class inclusion–exclusion then yields the quadratic plus alternating derangement correction; the r=n mixed-moment value must be used rather than the quadratic extrapolation of zero. For m≥2, D_m≥m−1 and the correction term h_m=(m−1)(−1)^m/D_m has absolute value at most one. For n≥4 the classes k=1,2 are feasible and the selected positive correction strictly separates them, beats all other nonidentity classes, and yields mean greater than one. The written comparison to h_(n−2) does not apply at n=3, where k=2 is infeasible: direct means of 1,2,1 at k=0,1,3 prove the theorem there. This is a proof boundary clarification, not a change to the claim. Independent exact replay in branches/11d352fe-6a50-4928-bfad-a6c7c0ac07a6/independent_check.py checked 46,230 permutations through n=8 and 279 assertions, including the joint first moments, conditional means, factorial covariances and unique maxima. The all-size argument rests on counting and inclusion–exclusion.

## originality

PASS

Pass for the all-order factorial mixed covariances, exact wrapped conditional first moment and parity selection. Cov(F,C)=0 is established in earlier indexed results, one of which covers all cyclic consecutive patterns, and the usual linear descent/fixed-point enumerator is stronger for the linear part. The linear data omit the conditional wrap event. No inspected prior statement supplies the full new wrapped regression or the corresponding hierarchy; this is not a priority certification. The Foata–Han citation should not be read as identifying its modified descent statistic with ordinary descents.

## value

PASS

The regression quantifies dependence invisible to the known zero covariance and settles, for all sizes, a natural fixed-class extremum. The competing leading conditional means for k=1 and k=2 tie, so the alternating derangement term, though small at large n, is mathematically decisive. The higher factorial moments supply exact testable information about the dependence without purporting to give the full joint law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
