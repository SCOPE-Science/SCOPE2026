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

# Computational verification and mathematical limits

Run `python3 verify.py` from the directory containing the standalone included source. It uses Python 3's standard library and no external data. For each even \(n\) in \(\{6,8,10,12,14\}\), the program enumerates every rotation orbit of weight-two length-\(n\) words, every subset of those rotation orbits, and tests connectivity and balance in the length-\((n-1)\) overlap graph after inclusion of all weight-three edges. It confirms that exactly one minimum-size optional edge set exists, and that this set consists of same-parity pairs. It then constructs an Eulerian cycle, computes all length-\(n\) factors cyclically and compares the resulting counted multiset against the target edge multiset.

Expected output summaries, giving weight-three factors / minimum added weight-two factors / total circle length: \(n=6\): \(20/6/26\); \(n=8\): \(56/12/68\); \(n=10\): \(120/20/140\); \(n=12\): \(220/30/250\); \(n=14\): \(364/42/406\). The final output line is `ALL_CHECKS_PASSED`. For example, the cycle `11001010100110100011100010` works at \(n=6\).

Finite enumeration verifies only the stated finite cases. It does not establish all orders; the unbounded theorem is proved in `RESULT.md` using balance, rotation orbits, a triangle-free complement, Mantel's bound and the explicit parity construction. Code does not compare novelty with unindexed or unavailable literature, does not independently audit the mathematics, and does not validate claims for odd orders or different allowable auxiliary window weights.
