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

The theorem is proved by exact algebra and an explicitly cited unrestricted-base gcd theorem (Kane–Sanna–Shallit, Theorem 1). The script `verify.py` uses only Python's integer arithmetic; run it with `python3 verify.py`. It compares the odd-width formula to the two-width exact gcd, then to the direct gcd over the first \(k+1\) odd widths, for bases \(2\) through \(10\) and repetition counts \(2\) through \(40\). Even-width calculations are compared to the base-\(b^2\) formula over the first \(k+1\) even widths. Finite enumeration does not establish the universal statement; the factorization, modular argument, and published unrestricted-base lemma do. No external independent verification has been performed.
