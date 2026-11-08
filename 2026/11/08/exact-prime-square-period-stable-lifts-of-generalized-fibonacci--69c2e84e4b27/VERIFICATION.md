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

The exact-integer Python 3 program `artifacts/verify.py` exhausts all coefficient lifts over each \(p\in\{3,5,7,11,13,17\}\), checks the matrix-order condition \(M^h=I\pmod{p^2}\), verifies the alternative \(M^{ph}=I\), and checks every predicted regular and singular fiber count. For primes three, five, and seven, it independently iterates every recurrence state to verify that its least period coincides with the matrix order at the lift.

Replayed output:
```
p=3 regular_bases=4 singular_bases=2 stable_lifts=10
p=5 regular_bases=16 singular_bases=4 stable_lifts=16
p=7 regular_bases=36 singular_bases=6 stable_lifts=36
p=11 regular_bases=100 singular_bases=10 stable_lifts=100
p=13 regular_bases=144 singular_bases=12 stable_lifts=144
p=17 regular_bases=256 singular_bases=16 stable_lifts=256
VERIFY_OK matrix_lifts=120894 recurrence_checks=2612 primes=(3, 5, 7, 11, 13, 17)
```
These tests are finite and are not a proof for arbitrary primes. The unrestricted proof uses only elementary finite-field and prime-square ring arguments, plus uniqueness of the simple-root lift for a polynomial with unit derivative. No independent audit has been performed.
