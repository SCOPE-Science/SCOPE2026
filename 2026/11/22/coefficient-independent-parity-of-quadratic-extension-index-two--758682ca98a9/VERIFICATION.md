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

# Verification record

The proof is fully symbolic and covers all odd prime powers and every positive exponent difference with gcd two. The program `verify_sign.py` is a separate direct finite-field evaluation using explicit polynomial quotient fields, not a proof of the infinite theorem.

Command: `python3 verify_sign.py`

Observed output:

```text
PASS q=3; modulus=[1, 0, 1]; indices=2; exponents=4; permutations=16
PASS q=5; modulus=[1, 1, 1]; indices=4; exponents=12; permutations=288
PASS q=7; modulus=[1, 0, 1]; indices=4; exponents=9; permutations=288
PASS q=11; modulus=[1, 0, 1]; indices=4; exponents=10; permutations=480
PASS q=9; modulus=[1, 0, 1, 1, 1]; indices=8; exponents=13; permutations=1060
PASS total_parameter_checks=16064; permutation_instances=2132; even_and_odd_seen=true
```

The test checks group arithmetic, permutation bijectivity and cycle parity independently of the proof formula. Exhaustion is only over the finite displayed parameter ranges; no numerical check establishes uniqueness or originality in the literature.
