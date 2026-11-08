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
# Verification of exact interval online ranks

The independent Python program `verify_intervals.py` uses only the standard library. Running `python3 verify_intervals.py` prints the exact marker:

`INTERVAL_ONLINE_PASS dp_n=1..40 brute_n=1..10 vc_n=1..10 all_histories_n=1..8 checked=5110 dyadic_k=0..5`

The dynamic programming state is a sorted tuple of positive unqueried-run lengths. It computes a positive child's threshold-product rank with integer floor logarithms and a negative child's rank by removing the queried point and inserting the two residual runs. Empty negative children use rank -1, so one-sided queries cannot spuriously raise the Littlestone dimension. Independently, a brute-force bitmask recurrence enumerates all nonempty intervals and computes the general rank of every reachable version-space mask without relying on the normal forms. These methods agree for all domains of sizes one through ten. Every realizable three-valued point-query history through eight sites was also compared against the general version-space rank (5,110 cases), covering the positive and negative normal forms separately.

The program also independently enumerates all shattered point subsets for domains of size up to ten, checks the predicted VC dimensions, evaluates the exact state recurrence for sizes one through forty, and verifies dyadic equality for all cases within that range. It validates the cardinality inequality separately for the reported dyadic exponents.

No computation is used as a certificate for infinitely many domain sizes. The unrestricted claims rely on the induction, threshold-product argument, and cardinality proof in `RESULT.md`.
