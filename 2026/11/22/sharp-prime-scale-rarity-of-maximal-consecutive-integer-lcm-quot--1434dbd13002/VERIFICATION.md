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

The proof separates a finite exact carry identity from the asymptotic prime sum. The attached standalone checker computes local maxima by two independent exact integer methods for every prime \(p\le k<300\) and checks direct full periods for \(2\le k\le12\). It also prints numerical scaled log-densities at four window lengths up to one million. A successful run supports the algebraic normalization but does not certify the analytic prime-number-theorem and Brun–Titchmarsh arguments; these must be assessed from the written proof.

Run `python3 artifacts/verify.py` after extracting the exact embedded checker file. Standard Python 3 only, no external packages or network. No independent mathematical audit has been performed.
