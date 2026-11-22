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

# Mathematical verification
The analytic proof is fully contained in RESULT.md. `checker.py` is a supplementary, finite numerical check. It independently compares the exact rational speed-variance expression against an independently sampled angular Poisson integral and an independently truncated Fourier sum. It also checks that the unique root is in the prescribed interval and beats the equal-radius and zero-radius endpoints, and compares the two asymptotic endpoint expressions numerically. These tests do not certify the theorem for infinitely many radii; the proof establishes that part by strict monotonicity and algebra. No independent audit was performed.
