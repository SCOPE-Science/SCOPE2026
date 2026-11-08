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

# Reproduction

Run `python verify.py` using Python 3.8+ with no nonstandard packages. The script reports exact exhaustive graph enumeration for all integers \(1\le N\le16\), checks the combinatorial count of maximizers, compares it against independently computed kernel-component maximum sizes, and computes the finite tie-count formula for \(N=10^2,10^3,10^4,10^5,10^6,10^7\). The final printed predicted constant uses a prime-product truncation below 100000 and therefore is numeric, not a proof of product convergence or a certified interval.

All finite outputs are in `verify_output.txt`; compare them directly with a fresh run. The infinite theorem is proved in RESULT.md using graph decomposition, a local squarefree sieve, area integration, and tail bounds. No finite extrapolation establishes the asymptotic. Independent mathematical validation has not been performed.
