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

# Reproducibility and limits

Run `python3 verify.py` in the folder containing the standalone checker. It uses only the Python standard library. The expected output from the saved checker is:

```
VERIFY_OK prime_rows= 54 interior_entries= 6228 Lucas_odd_witnesses= 530 Lucas_binary_witnesses= 298 Fermat_exponents=1,2,4,8,16 exact_gcd=PASS
```

The checker reconstructs Narayana numbers by integer binomial arithmetic and computes each prime-row gcd directly for all odd primes at most \(257\). It also tests the Lucas witness for every relevant prime factor of \(p-1\) with \(p\le2000\), and checks binary valuations of the specific extremizing indices for \(p=2^r+1\), with \(r\in\{1,2,4,8,16\}\). For the very large final example, only the exact valuation identities are checked; its entire row is not enumerated. Finite enumeration is not a proof for arbitrary primes: the unrestricted result rests on the Lucas-theorem argument and the complete 2-adic valuation bounds in `RESULT.md`. No independent audit has been performed.
