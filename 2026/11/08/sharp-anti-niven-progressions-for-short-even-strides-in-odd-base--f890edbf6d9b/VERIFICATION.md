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

The accompanying `check.py` uses only the Python 3 standard library and may be executed with `python3 check.py`. Its actual stdout is recorded verbatim in `check_output.txt`. It checks the CRT selection condition, the two-digit range, the digit sums, and simultaneous modular witness conditions for all 1343 admissible pairs with odd bases from 3 to 301 and even differences from 2 to 42. For the parameter pairs (11,4) and (21,4), it additionally calculates the full integers and independently checks their digit sums and gcds.

The proof needs no numerical search: the CRT existence argument is valid for arbitrarily many prime factors, simultaneous prime congruences follow from Fermat's theorem, and the two-digit bound eliminates all possible extra prime factors of the number-minus-digit-sum discrepancy. These are universal algebraic steps, not extrapolations from the checker. The verification does not establish originality, an independent audit, or the conjecture beyond the claimed inequality.
