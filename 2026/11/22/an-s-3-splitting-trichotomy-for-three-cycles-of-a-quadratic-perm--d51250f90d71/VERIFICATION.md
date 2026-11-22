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

# Verification and scope

Run `python3 verify.py` with standard Python 3 from the extracted directory. The checker independently evaluates both integral polynomial-elimination identities (equivalent to the two rational equations with denominators cleared), the sextic square decomposition, the original-to-Hénon conjugacy over small prime fields, and exhaustive third-iterate/fixed-point enumeration for every odd prime at most 139. It checks 194081 prime-field input pairs. It also computes root counts of the sextic over every degree 1 through 6 extension, using polynomial gcd with the Frobenius equation, and confirms the 1-, 2-, 3-order trichotomy for those primes.

This verifies finite instances only. The proof of degree-six regular \(S_3\) action uses Eisenstein irreducibility, the cubic-discriminant criterion, and a cubic factorization over \(\mathbb Q(\sqrt{-6})\). The infinite natural densities follow from Chebotarev's theorem. No independent audit has been performed, and no broader long-cycle claim is made.
