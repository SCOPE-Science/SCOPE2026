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

The theorem is proved for fixed \(m\) using the exact rooted count, a decreasing consecutive-term ratio, a uniform saddle estimate, and a telescoping target-capacity sensitivity estimate. The additional endpoint \((u+1)^{N-u-1}\) in the one-step identity is accounted for and shown negligible at the asymptotic scale. The proof distinguishes finite formulas from asymptotic statements, and its error term retains the total number of source points \(N\) when block sizes differ by \(o(n)\).

Run `python3 checker.py` using only Python's standard library. The provided `checker_output.txt` is the recorded output of the run. Six direct full-map enumerations compare exact image-block-root counts against independent rooted-fiber counting. Thirty finite checks compare the exact consecutive-target-size binomial identity, including the endpoint term. The enumeration is exhaustive only for those listed finite instances; it neither proves uniqueness in the literature nor certifies any infinite limit.

Scientific limitations: fixed block count, asymptotically equal block sizes, conditional nonuniform-priority uncertainty. The all-size finite idempotent enumeration is attributed to earlier work. Independent audit: not performed.
