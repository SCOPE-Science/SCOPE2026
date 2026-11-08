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
The independent-in-implementation, same-package exact-integer checker `checks/check_theta.py` enumerates all trees of \(K_{2,n}\), constructs all Walsh coefficients by butterfly transform, and compares them with the closed three-case spectrum for every integer \(2\le n\le8\). It also checks the \(n2^{n-1}\) tree count, the formula for Fourier support, the exact absolute first moment and the Parseval second moment. All cases passed with marker `THETA_K2N_FULL_FOURIER_CERTIFICATE_PASS`. The all-depth proof in `RESULT.md` uses combinatorial counting and a telescoping binomial identity; exhaustive finite enumeration is not claimed as an infinite proof. Independent mathematical audit: not performed.
