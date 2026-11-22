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
The included `checker.py` was run against the packaged mathematical definitions. Its exact results were \(4\), \(36\), and \(3900\) progression-count comparisons at \(p=2,3,5\), respectively, covering **every** nonzero spacing in the corresponding period. The direct Bell recurrence agreed with Touchard's recurrence for the first thirty entries in each case; full-period first-block consistency and the known \(p=5\) consecutive start \(587\) were also checked.

These finite checks cannot prove the result for larger primes or arbitrarily large periods. The unrestricted argument is given in the proof using field degree, nondegenerate trace pairing, and a projective-point count. Full least period is an explicit hypothesis; existing literature verifies it for a substantial collection of primes but not universally. Independent mathematical audit has not been performed.
