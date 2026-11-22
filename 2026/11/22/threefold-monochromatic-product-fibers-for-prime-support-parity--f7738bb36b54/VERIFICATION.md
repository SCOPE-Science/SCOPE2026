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

Run `python3 verify.py` with no third-party packages. This compares the closed prime-exponent formula and the exceptional set with direct enumeration of ordered triples having all factors greater than one, for every positive integer through 2,500 and eight additional larger instances. Its successful output is `PASS: 2508 independently enumerated integers; support and counts agree`.

The mathematical argument in `RESULT.md` uses a sign-projector identity and an inclusion–exclusion that handles units, local prime-power convolutions, casewise constructive prime-support partitions, and the standard fixed-order Landau theorem. Infinite correctness relies on the argument and classical input, not on finite enumeration. No independently performed mathematical audit is claimed.
