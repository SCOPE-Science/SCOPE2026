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

# Verification evidence and limits

Run `python3 check_modular_cusps.py` using Python 3 and the standard library. The checker uses exact integer arithmetic to test the polynomial factorization defining the two elliptic branch points; compares the classical eta-product and Rogers–Ramanujan identity after multiplication by \(q\), through degree \(15\) of their power series; and exhaustively enumerates the \(42\) divisors of \(4800\) using Euler's totient function. It asserts that the base has \(144\) geometric cusps, that the covering cusp-orbit degrees have counts \((16,16,24,10,4)\) in degrees \((1,2,4,8,16)\), and that the cover has \(70\) closed and \(288\) geometric cusps. It reports `PASS` when all assertions hold.

The finite formal-series test cannot establish an identity of full modular functions. The proof instead invokes the classical infinite modular identity in the cited literature; the isomorphism of modular covers, local ramification and cyclotomic residue-field arguments are mathematical deductions recorded in `RESULT.md`. The code is a reproducibility check, not an exhaustive algorithm for all rational points, a proof of publication priority, or independent certification.
