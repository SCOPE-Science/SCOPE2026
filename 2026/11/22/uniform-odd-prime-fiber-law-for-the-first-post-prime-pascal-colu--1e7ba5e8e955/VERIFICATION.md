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

# Verification

From this directory, execute `python3 CHECK.py`. This uses only the standard Python library and computes complete targetwise fibers for every odd prime \(p\in\{3,5,7,11\}\) and exponent \(h\in\{1,2,3\}\). For each case it enumerates a complete block of \(p^{h+1}\) values of \(\binom{n}{p+1}\), computes the rational critical value \(\alpha_p\), and compares every target's count with the quadratic-root formula. It also tests a witness proving the smaller period \(p^h\) fails. Twelve complete cases passed; the largest period had 14,641 indices, covering 1,331 targets.

The proof for unrestricted primes and exponents is the symbolic factorization into regular isometries plus an exactly conjugated square branch in RESULT.md; finite enumeration is not an exhaustive proof. Bibliographic originality remains subject to independent comparison and independent mathematical audit has not been performed.
