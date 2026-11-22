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

Run `python3 verify.py` in the directory containing this file. The check uses Python's exact integers and standard library only. Its actual recorded output is `verification-output.txt`.

The verifier constructs the Thue–Morse word by binary-digit parity and evaluates the mathematically derived square-suffix recursion at one million successive endpoints. It independently performs an exhaustive all-period square test for the first 2048 nonempty prefixes (every possible square-root length for each such prefix). It also matches the first 32 terms of the historic curling transform with the documented one-initial-term convention and verifies the exact dyadic theorem and its intermediate equal-pair and four-letter-factor counting identities for each integer exponent from 2 through 20. Comparisons of separate proof steps are described in `RESULT.md`.

The exhaustive all-period tests end at prefix length 2048 and do not prove the theorem at unbounded lengths. The all-index proof relies on the published Pansiot–Brlek classification in Brown et al. (2006), not on a finite test. Natural density is proved by the stated recurrences and their asymptotic estimates, not inferred from sampled proportions. No independent audit has been performed.
