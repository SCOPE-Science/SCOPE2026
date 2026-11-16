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

# Verification and reproducibility

The proof in `RESULT.md` is analytic and addresses *every* integer Taylor degree and every complex analytic-Wiener competitor. The essential certificate is the real exponential sequence \(h_j=\lambda u^j+\mu v^j\): its one-turning-point property proves the unbounded tail inequality, and exact interpolation of each candidate trinomial proves the complementary inequality.

Run `python3 CHECK.py` with Python 3.9+ and no third-party dependencies. It checks 45 rational radius pairs with exact fractions, all candidate vanishing identities, the first transition equation, the exact tie \((u,v)=(1/5,2/3)\), and the high-degree case \((u,v)=(4/5,9/10)\). The finite coefficient-prefix checks are illustrative and are not presented as proof of an infinite assertion. The source date comes from arXiv:2611.02159v1 (2026-11-01); the source's primary MSC 30C15 matches the present zeros-and-interpolation topic.

Originality was compared to the inspected primary texts and to topical mathematical-result searches. An exhaustive historical equivalence search has not been performed. No independent audit has been conducted.
