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

# Verification and limitations

Reproduce from the embedded standalone file: `python3 verify_palindrome.py`. The test enumerates all starts for the longest length and the next two lengths in substitution prefixes, bases \(3\) through \(10\), including direct comparison with the claimed occurrence formula. It also checks modular arithmetic cases for bases \(3\) through \(250\). Observed output: `VERIFY_OK bases=3..10 palindrome_window_tests=2363532 modular_cases=1488`.

The proof is in `RESULT.md`. The certificate is not an exhaustive computation over bases or the infinite word. The decisive nonstandard ingredients are the transition recurrence, the residue-reflection obstruction, the exceptional \(b=3\) parity check, and the primitive substitution's transition density. No independent scientific audit has been performed.
