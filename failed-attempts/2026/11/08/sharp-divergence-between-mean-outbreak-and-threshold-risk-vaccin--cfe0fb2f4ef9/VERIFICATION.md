---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The deterministic percolation run identity h N_h-(h-1) N_(h+1) exactly counts vertices in open path components of length at least h. Taking expectations gives F_m=h(m-h+1)p^(h-1)-(h-1)(m-h)p^h for m>=h and zero otherwise. For a single deletion a+b=n-1: tail-minimum profiles have one small gap of h-1 and one residual large gap, or both <h; strict excess of having two active gaps is (h-1)p^h/(n-1). The mean follows from H_m=sum_(d=1)^(m-1)(m-d)p^d and strict discrete convexity, hence balanced splitting. Boundary n=2h checked. Independent exact state-enumeration verified 156 parameter cases. C PASS is for the entire claimed theorem, not for logs alone.

## originality

FAIL

The earlier October 25 published multi-vaccine path-layout theorem has the identical formula for the threshold-counted tail contribution and balanced-mean criterion, with complete minimizers for b=k+1 gaps. Its explicit paper states k>=2 and h>=3, but its proof is purely a deterministic gap argument valid unchanged for b=2 (one vaccine): specializing b=2 gives exactly n<=2h compatibility, gaps (h-1,n-h), and excess (h-1)p^h/(n-1). The h=2 case is a direct special case of its same run identity, supported by a separate earlier first-transmission path theorem. No novel calculation beyond parameter-boundary substitution remains.

## value

FAIL

The two epidemiological criteria are meaningful, but this particular exact one-vaccination classification and cutoff follow mechanically from previously published, complete gap-optimization proof and earlier first-transmission results. Thus there is no distinct valuable new mathematical contribution, although the old result itself is useful. This rejection is for coverage/derivative value, not correctness or lack of access.

The dated certificate retains the supplied scientific assessment, sources and limitations.
